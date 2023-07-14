from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain.agents import initialize_agent
import os
from dotenv import load_dotenv, find_dotenv

class Agent:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.llm = ChatOpenAI(
            openai_api_key = os.getenv("OPENAI_API_KEY"),
            temperature=0,
            model_name="gpt-3.5-turbo-16k"
        )

        self.llm_math = LLMMathChain(llm=self.llm)
        # initialize the math tool
        self.math_tool = Tool(
            name='Calculator',
            func=self.llm_math.run,
            description='Useful for when you need to answer questions about math.'
        )


        # when giving tools to LLM, we must pass as a list of tools
        self.tools = [self.math_tool]

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
        result = agent.zero_shot_agent(response)
        print(result)

# create an instance of Agent
agent = Agent()

# run the agent
agent.run_agent()


#what is (6.53*14.1)^6.22?
#"if Mary has four apples and Giorgio brings two and a half apple "
#               "boxes (apple box contains eight apples), how many apples do we "
#               "have?")