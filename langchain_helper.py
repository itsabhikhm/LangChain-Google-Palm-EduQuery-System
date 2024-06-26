from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
# from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
# from langchain.vectorstores import FAISS
from langchain_community.vectorstores import FAISS
# from langchain.document_loaders import CSVLoader
from langchain_community.document_loaders import CSVLoader
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA

import os


load_dotenv()


llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest",google_api_key=os.getenv("GOOGLE_API_KEY"),temprature=0)

# Create Embedding and Vector Database
instructor_embeddings = HuggingFaceInstructEmbeddings()
vectordb_file_path = "faiss_index"

def create_vector_db():
    loader = CSVLoader("codebasics_faqs.csv",source_column="prompt", encoding="latin-1") # Try loading with Latin-1 encoding
    docs = loader.load()
    vectordb = FAISS.from_documents(documents= docs, embedding = instructor_embeddings)
    vectordb.save(vectordb_file_path)

def get_qa_chain():
    # Load the vector database from the file
    vectordb = FAISS.load_local(vectordb_file_path,instructor_embeddings,allow_dangerous_deserialization=True)

    # Create a retriever from the vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "Sorry, I do not have answer for this question." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
        )

    chain = RetrievalQA.from_chain_type(llm = llm, 
            chain_type = "stuff", # There are two types of chain stuff and map-reduce
            retriever = retriever,
            input_key = "query",
            return_source_documents = True, # When you get an answer, return source from the csv file
            chain_type_kwargs = {"prompt" : prompt}) 
    
    return chain

if __name__ == "__main__":
    # create_vector_db()
    chain = get_qa_chain()
    # chain("Do you have emi option")