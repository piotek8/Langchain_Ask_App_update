from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback

def main():
    load_dotenv()
    print("Ask your PDF")

    # upload file
    pdf_path = input("Enter the path to your PDF file: ")

    # extract the text
    pdf_reader = PdfReader(pdf_path)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()

    # split into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    # create embeddings
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    # ask a question
    user_question = input("Ask a question about your PDF: ")
    if user_question:
        docs = knowledge_base.similarity_search(user_question)

        llm = OpenAI()
        chain = load_qa_chain(llm, chain_type="stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=user_question)
            print(cb)

        print(response)


if __name__ == '__main__':
    main()
