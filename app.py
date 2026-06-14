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

        text=load_pdfs(
            files
        )

        chunks=chunk_text(
            text
        )

        vectors=[

        create_embedding(
        c
        )

        for c
        in chunks
        ]

        build_vector_db(
            vectors,
            chunks
        )

