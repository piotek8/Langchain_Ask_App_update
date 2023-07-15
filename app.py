from core.agent import Agent

if __name__ == "__main__":
    # create an instance of Agent
    agent = Agent()

    # run the agent
    question = input('''Write informations \nEnter your question: ''')
    agent.get_agent_response(question)

    # what is (6.53*14.1)^6.22?
    # "if Mary has four apples and Giorgio brings two and a half apple "
    #               "boxes (apple box contains eight apples), how many apples do we "
    #               "have?")
#The famr consists of a house,
# a shack and a barn. How many dogs are on the farm?
# If 2 dogs are in the kennel and 2 other dogs are standing next to the house.




'''
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

prompt = PromptTemplate(
    input_variables=["query"],
    template="{query}"
)

llm_chain = LLMChain(llm=llm, prompt=prompt)

# initialize the LLM tool
llm_tool = Tool(
    name='Language Model',
    func=llm_chain.run,
    description='use this tool for general purpose queries and logic'
'''