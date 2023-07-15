from core.agent import Agent
import warnings

# Ignore the specific warning
warnings.filterwarnings("ignore", message="Directly instantiating an LLMMathChain with an llm is deprecated.")

if __name__ == "__main__":
    # create an instance of Agent
    agent = Agent()

'''
    while True:
        # prompt user for choice
        choice = input("Enter:\n - '1' to use Calculator\n - '2' to use Language Model \n - 'exit' to quit \n"
                       "What is your choice?")

        if choice == '1':
            calculation = input("Enter the question for the Calculator: ")
            result = agent.get_agent_response(calculation)
        elif choice == '2':
            query = input("Enter the question for the Language Model: ")
            result = agent.get_agent_response(query)
        elif choice.lower() == 'exit':
            break
        else:
            print("\nInvalid choice. Please enter 1, 2, or 'exit'.")
            continue  # Go back to the beginning of the loop

        # prompt user to continue or exit
        continue_choice = input("Enter 1 or 2 to continue using the respective tool, or 'exit' to quit: ")

        if continue_choice.lower() == 'exit':
            break
        elif continue_choice not in ['1', '2']:
            print("Invalid choice. Please enter 1, 2, or 'exit'.")
            break
'''













#from core.agent import Agent
#
#if __name__ == "__main__":
#    # create an instance of Agent
#    agent = Agent()
#
#    # run the agent
#    question = input('''Write informations \nEnter your question: ''')
#    agent.get_agent_response(question)



    # what is (6.53*14.1)^6.22?
    # "if Mary has four apples and Giorgio brings two and a half apple "
    #               "boxes (apple box contains eight apples), how many apples do we "
    #               "have?")
#The famr consists of a house,
# a shack and a barn. How many dogs are on the farm?
# If 2 dogs are in the kennel and 2 other dogs are standing next to the house.

