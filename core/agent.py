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
            elif choice.lower() == 'exit':
                break
            else:
                print("\nInvalid choice. Please enter 1, 2, or 'exit'.")
                continue
