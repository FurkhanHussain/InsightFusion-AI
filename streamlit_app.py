import streamlit as st
from main import run_insightrag

st.title("📊 InsightRAG: Business Q&A Assistant")

pdf = st.file_uploader("Upload a PDF", type="pdf")
csv = st.file_uploader("Upload a CSV", type="csv")
query = st.text_input("Ask a question about your data")

if pdf and csv and query:
    with open("data/uploaded.pdf", "wb") as f:
        f.write(pdf.read())
    with open("data/uploaded.csv", "wb") as f:
        f.write(csv.read())

    response = run_insightrag("data/uploaded.pdf", "data/uploaded.csv", query)
    st.success(response)