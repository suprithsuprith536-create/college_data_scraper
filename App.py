import streamlit as st
import pandas as pd
from scraper import scrape_nirf

st.title("🎓 College Data Scraper")

if st.button("Fetch College Data"):
    with st.spinner("Scraping data..."):
        data = scrape_nirf()
        
        if not data:
            st.error("Failed to fetch data")
        else:
            df = pd.DataFrame(data)
            st.dataframe(df)

            csv = df.to_csv(index=False).encode("utf-8")

            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name="colleges.csv",
                mime="text/csv"
            )
