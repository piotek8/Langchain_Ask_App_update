from langchain.agents import Tool, initialize_agent
from langchain.chains import LLMMathChain, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback
from PyPDF2 import PdfReader
from dotenv import load_dotenv, find_dotenv
import os
import streamlit as st


class Agent:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.llm = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0,
            model_name="gpt-3.5-turbo-16k"
        )

        self.llm_math = LLMMathChain(llm=self.llm)
        self.math_tool = Tool(
            name='Calculator',
            func=self.llm_math.run,
            description='Useful for when you need to answer questions about math.'
        )

        self.tools = [self.math_tool]

        prompt = PromptTemplate(
            input_variables=["query"],
            template="{query}"
        )

        self.llm_chain = LLMChain(llm=self.llm, prompt=prompt)

        # initialize the LLM tool
        self.llm_tool = Tool(
            name='Language Model',
            func=self.llm_chain.run,
            description='Use this tool for general purpose queries and logic')
        self.tools.append(self.llm_tool)

        # initialize the zero-shot agent
        self.zero_shot_agent = initialize_agent(
            agent="zero-shot-react-description",
            tools=self.tools,
            llm=self.llm,
            verbose=True,
            max_iterations=3
        )

    def get_agent_response(self, question):
        result = self.zero_shot_agent(question)
        return result

    def use_calculator(self, calculation):
        result = self.get_agent_response(calculation)
        return result

    def use_language_model(self, query):
        result = self.get_agent_response(query)
        return result

    def search_pdf(self, pdf_path, question):
        if pdf_path.strip() == "":
            return None

        if not os.path.exists(pdf_path):
            return "File not found. Please enter a valid PDF file path."

        try:
            pdf_reader = PdfReader(pdf_path)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text()

            text_splitter = CharacterTextSplitter(
                separator="\n",
                chunk_size=1000,
                chunk_overlap=200,
                length_function=len
            )
            chunks = text_splitter.split_text(text)

            embeddings = OpenAIEmbeddings()
            knowledge_base = FAISS.from_texts(chunks, embeddings)

            docs = knowledge_base.similarity_search(question)

            llm = OpenAI()
            chain = load_qa_chain(llm, chain_type="stuff")
            with get_openai_callback() as cb:
                response = chain.run(input_documents=docs, question=question)
                print(cb)

            return response

        except Exception as e:
            return f"An error occurred while processing the PDF: {str(e)}"


class Program:
    def __init__(self, agent):
        self.agent = agent

    def calculator(self):
        calculation = st.text_input("Enter the question for the Calculator:", key="1")
        if len(calculation) > 0:
            result = self.agent.use_calculator(calculation)
            st.write(result)

    def language_model(self):
        query = st.text_input("Enter the question for the Language Model:", key="2")
        if len(query) > 0:
            result = self.agent.use_language_model(query)
            st.write(result)

    def search_pdf(self):
        pdf_path = st.text_input("Enter the path to the PDF file:", key="3")
        question = st.text_input("Enter the question for PDF search:", key="4")
        if len(pdf_path) > 0 and len(question) > 0:
            result = self.agent.search_pdf(pdf_path, question)
            st.markdown(result)
            # st.write(result)

    def run(self):
        st.title("Langchain Ask App ")
        st.write("Enter:\n - '1' to use Calculator\n - '2' to use Language Model\n"
                 " - '3' to search PDF")

        self.choice = st.text_input("What is your choice?", key="5")
        if len(self.choice) == 0:
            pass
        elif self.choice == '1':
            self.calculator()
        elif self.choice == '2':
            self.language_model()
        elif self.choice == '3':
            self.search_pdf()
        else:
            st.write("Invalid choice.")
            st.write("Please enter: 1 or 2 or 3")
