from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from embeddings import get_embedding_function
from dotenv import load_dotenv
import os

load_dotenv()

CHROMA_PATH = "chroma"

def query_rag(query_text: str):
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)

    PROMPT_TEMPLATE = """
    You are an expert information security teacher.
    Use the following context from the provided PDFs as your primary source: {context}
    
    Based on the above context and your own knowledge, answer the following question in detail with clear examples:{question}
    
    Instructions:
    - Read the question carefully and match the response style to what the user is asking:
    - If they ask for a brief/short answer, respond concisely
    - If they ask for an explanation or details, provide a thorough explanation with subheadings
    - If they ask for an example, provide only a practical real world example
    - If they ask a yes/no question, answer directly then add a one line reason
    - Otherwise, give a balanced answer without over-explaining
    - Use the context as your primary source; supplement with your own knowledge only if the context is insufficient
    - Do not add sections the user did not ask for (e.g. skip examples if they only asked for a definition)
    
    Format your answer as follows:
    - Start with a clear ## Heading for the main topic
    - Use ### Subheadings to break down sections
    - Use bullet points (- ) for lists and key points
    - Highlight examples under a ### Example subheading
    - Bold important terms using **term**
    - Keep explanation clear
    """

    results = db.similarity_search_with_score(query_text, k=5)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, score in results])

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    
    model = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    response = model.invoke(prompt)
    return response.content

if __name__ == "__main__":
    import sys
    query = " ".join(sys.argv[1:])
    if not query:
        query = input("Enter your question: ")
    print(query_rag(query))


