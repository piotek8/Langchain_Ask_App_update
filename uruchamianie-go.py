import streamlit as st
from zobaczymy_czy_zadziala.caly_program import Agent, Program

# Inicjalizacja agenta i programu
agent = Agent()
program = Program(agent)

def main():
    st.title("Language Model Program")
    st.write("Welcome to the Language Model Program!")

    # Główna pętla programu
    while True:
        choice = st.selectbox(
            "What would you like to do?",
            ("Use Calculator", "Use Language Model", "Search PDF", "Exit")
        )

        if choice == "Use Calculator":
            program.calculator()
        elif choice == "Use Language Model":
            program.language_model()
        elif choice == "Search PDF":
            program.search_pdf()
        elif choice == "Exit":
            break

if __name__ == "__main__":
    main()
