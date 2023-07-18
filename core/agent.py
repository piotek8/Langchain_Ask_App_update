import os
from dotenv import load_dotenv, find_dotenv
from langchain.agents import Tool
from langchain.agents import initialize_agent
from langchain.chains import LLMMathChain, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback


class Agent:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.llm = ChatOpenAI(
            openai_api_key=os.getenv("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"),
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

    def use_calculator(self):
        calculation = input("Enter the question for the Calculator: ")
        result = self.get_agent_response(calculation)
        return result

    def use_language_model(self):
        query = input("Enter the question for the Language Model: ")
        result = self.get_agent_response(query)
        return result

    def search_pdf(self, pdf_path, question):
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


class Program:
    def __init__(self, agent):
        self.agent = agent

    def calculator(self):
        result = self.agent.use_calculator()
        print(result)

    def language_model(self):
        result = self.agent.use_language_model()
        print(result)

    def search_pdf(self):
        pdf_path = input("Enter the path to the PDF file: ")
        question = input("Enter the question for PDF search: ")
        result = self.agent.search_pdf(pdf_path, question)
        print(result)

    def run(self):
        while True:
            choice = input("Enter:\n - '1' to use Calculator\n - '2' to use Language Model\n - '3' to search PDF\n"
                           " - 'exit' to quit\nWhat is your choice? ")

            if choice == '1':
                self.calculator()
            elif choice == '2':
                self.language_model()
            elif choice == '3':
                self.search_pdf()
            elif choice.lower() == 'exit':
                break
            else:
                print("\nInvalid choice. Please enter 1, 2, 3, or 'exit'.")
                continue



'''
import os

from dotenv import load_dotenv, find_dotenv
from langchain.agents import Tool
from langchain.agents import initialize_agent
from langchain.chains import LLMMathChain, LLMChain
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate


# from utils.constants import OPENAI_KEY

class Agent:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.llm = ChatOpenAI(
            openai_api_key=os.getenv("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"),
            # (OPENAI_KEY),
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
            description='use this tool for general purpose queries and logic')
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


class Program:
    def __init__(self, agent):
        self.agent = Agent()

    def run(self):
        while True:
            choice = input("Enter:\n - '1' to use Calculator\n - '2' to use Language Model\n - 'exit' to quit\n"
                           "What is your choice? ")

            if choice == '1':
                calculation = input("Enter the question for the Calculator: ")
                result = self.agent.get_agent_response(calculation)
            elif choice == '2':
                query = input("Enter the question for the Language Model: ")
                result = self.agent.get_agent_response(query)
            elif choice == '3':
                pass
            elif choice.lower() == 'exit':
                break
            else:
                print("\nInvalid choice. Please enter 1, 2, or 'exit'.")
                continue
'''