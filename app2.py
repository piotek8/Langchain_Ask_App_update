import os

from dotenv import load_dotenv, find_dotenv
from langchain.agents import Tool
from langchain.agents import initialize_agent
from langchain.chains import LLMMathChain, LLMChain
from langchain.chat_models import ChatOpenAI


class Agent:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.llm = ChatOpenAI(
            openai_api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0,
            model_name="gpt-3.5-turbo-16k"
        )

        # initialize the math tool
        self.llm_math = LLMMathChain(llm=self.llm)
        self.math_tool = Tool(
            name='Calculator',
            func=self.llm_math.run,
            description='Useful for when you need to answer questions about math.'
        )

        # when giving tools to LLM, we must pass as a list of tools
        self.tools = [self.math_tool]

        # initialize the LLM tool
        self.llm_chain = LLMChain(llm=self.llm)
        self.llm_tool = Tool(
            name='Language Model',
            func=self.llm_chain.run,
            description='Use this tool for general purpose queries and logic.'
        )
        self.tools.append(self.llm_tool)

        # initialize the zero-shot agent
        self.zero_shot_agent = initialize_agent(
            agent="zero-shot-react-description",
            tools=self.tools,
            llm=self.llm,
            verbose=True,
            max_iterations=3
        )

    def run_agent(self):
        response = input('''Write information related to mathematics only\nEnter your question: ''')
        result = self.zero_shot_agent(response)
        print(result)


# create an instance of Agent
agent = Agent()

# run the agent
agent.run_agent()
