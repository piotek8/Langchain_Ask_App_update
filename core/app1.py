from agent import Agent, Program
import warnings
import streamlit as st

# Ignore the specific warning
warnings.filterwarnings("ignore", message="Directly instantiating an LLMMathChain with an llm is deprecated.")

def main():
    agent = Agent()

    # create an instance of Program
    program = Program(agent)

    # run the program
    program.run()


if __name__ == "__main__":
    main()

