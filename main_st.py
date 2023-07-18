from source_code.app_st import Agent,Program
import warnings

warnings.filterwarnings("ignore", message="Directly instantiating an LLMMathChain with an llm is deprecated. Please instantiate with llm_chain argument or using the from_llm class method.")

if __name__ == '__main__':
    agent = Agent()
    program = Program(agent)
    program.run()