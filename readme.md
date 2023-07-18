# Langchain Ask App (Tutorial)

This code represents a language agent that utilizes ChatGPT and LLM models for a calculator, general language queries, and searching in PDF files. 
The program enables user interaction with the agent and can be executed using Streamlit, allowing users to access agent functions through a web interface. 
The code creates a simple application that offers interactive and user-friendly utilization of the language agent's features.

## Installation

To install the repository, please clone this repository and install the requirements:

```
pip install -r requirements.txt
```

You will also need to change your OpenAI API key to the `.env` file in `source_code` folder.

```
OPENAI_API_KEY = "your_api_key_from_openai"
```

## Usage

Run the Streamlit application using the following command:
```
streamlit run app.py
```
Streamlit will start a local development server and open a new tab in your default web browser with the application running. You can view information in the terminal:
``` 
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://10.0.2.15:8501
```
You can now interact with the application through the web interface provided by Streamlit.


## How to use it properly
When you start the program with command `streamlit run app.py`, you should see:

![1](https://github.com/piotek8/PowerBI_projects/assets/82182989/dee0f109-090e-4f03-979a-1a2acc86119d)

`Now you have 3 ways to use the app:`

The first option is to query the langchain of the calculator:

![2](https://github.com/piotek8/PowerBI_projects/assets/82182989/89de87f5-d51e-4eb6-b91e-48c1adebd6df)

The second option is to query the agent's langchain LLM:

![3](https://github.com/piotek8/PowerBI_projects/assets/82182989/e711984a-dc0d-408b-a1a7-e7b199cbe5be)

The third option is to import the path and query of the pdf file:

![5](https://github.com/piotek8/PowerBI_projects/assets/82182989/3da671a0-2de9-4e4c-95e0-2a660335cd8f)

## Contact

If you have any questions or comments, please contact me on github

