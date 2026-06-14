import streamlit as st

from auth import auth
from pdf_loader import load_pdfs
from chunking import chunk_text
from embedding import create_embedding
from vector_db import build_vector_db
from retriever import retrieve
from gemini_service import ask_gemini


name,status,user=auth.login()

if status:

    st.title(
    "RAG Code Review"
    )

    files=st.file_uploader(

        "Upload PDFs",

        type=["pdf"],

        accept_multiple_files=True
    )

    if files:
        st.success("PDF Uploaded")

    if st.button("Process PDFs"):

        with st.spinner("Processing PDF..."):

            text = load_pdfs(files)

            st.write(
                "Characters:",
                len(text)
            )

            chunks = chunk_text(text)

            st.write(
                "Chunks:",
                len(chunks)
            )

            vectors = [
                create_embedding(c)
                for c in chunks
            ]

            build_vector_db(
                vectors,
                chunks
            )

        st.success(
            "Index Created Successfully"
        )
    

query = st.text_input(
    "Ask Question"
)

if query:

    docs = retrieve(query)

    context = "\n".join(docs)

    result = ask_gemini(
        query,
        context
    )

    st.subheader(
        "Answer"
    )

    st.write(result)
