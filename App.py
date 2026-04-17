import streamlit as st
from pipeline import run_pipeline

st.title("🎓 College RAG Data Pipeline")

uploaded_file = st.file_uploader("Upload Input CSV", type=["csv"])

if uploaded_file:
    with open("data/input.csv", "wb") as f:
        f.write(uploaded_file.read())

    if st.button("Run Pipeline"):
        run_pipeline("data/input.csv", "data/output.csv")

        with open("data/output.csv", "rb") as f:
            st.download_button("Download Output CSV", f, "output.csv")
