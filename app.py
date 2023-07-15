from core.agent import Agent, Program
import warnings

# Ignore the specific warning
warnings.filterwarnings("ignore", message="Directly instantiating an LLMMathChain with an llm is deprecated.")

if __name__ == "__main__":
    # create an instance of Agent
    agent = Agent()

    # create an instance of Program
    program = Program(agent)

    # run the program
    program.run()

# Calculator:

# What is (6.53*14.1)^6.22?
# What is cosine of 90 degrees?
# What is 15 raised to the power x? given x equals 1/5?

# Language Model:

# In the backyard, there are 7 cows: one is white, the second one is black, and the rest are white-black in color. How many cows are white-black?
# The farm consists of a house, a shack and a barn. How many dogs are on the farm? If 2 dogs are in the kennel and 2 other dogs are standing next to the house.
# if Mary has four apples and Giorgio brings two and a half apple boxes (apple box contains eight apples), how many apples do we have?")
