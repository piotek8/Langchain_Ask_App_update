from core.agent import Agent

if __name__ == "__main__":
    # create an instance of Agent
    agent = Agent()

    # run the agent
    question = input('''Write information related to mathematics only\nEnter your question: ''')
    agent.get_agent_response(question)

    # what is (6.53*14.1)^6.22?
    # "if Mary has four apples and Giorgio brings two and a half apple "
    #               "boxes (apple box contains eight apples), how many apples do we "
    #               "have?")
