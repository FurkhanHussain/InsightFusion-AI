from ingest.pdf_loader import load_pdf
from ingest.csv_loader import load_csv
from rag.vectorstore import build_vectorstore
from rag.qa_chain import build_qa_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

def run_insightrag(pdf_path, csv_path, query):
    # Load data
    pdf_text = load_pdf(pdf_path)
    csv_text = load_csv(csv_path)

    full_text = pdf_text + "\n" + csv_text

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(full_text)

    # Build vector store
    vectordb = build_vectorstore(chunks)

    # QA chain
    qa_chain = build_qa_chain(vectordb)
   
    response = qa_chain.invoke({"query": query})
    return response["result"]


if __name__ == "__main__":
    query = input("Ask InsightRAG something: ")
    answer = run_insightrag("data/sample.pdf", "data/sample.csv", query)
    print("\nAnswer:", answer)