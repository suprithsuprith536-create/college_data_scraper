import pandas as pd
from utils import fetch_webpage_text, fetch_wikipedia_text, extract_pdf_text
from rag import extract_info_rag

def process_college(row):
    college_name = row["College Name"]
    
    text_data = ""

    # Website
    if pd.notna(row["Website URL"]):
        text_data += fetch_webpage_text(row["Website URL"])

    # Wikipedia
    if pd.notna(row["WIKI Page URL"]):
        text_data += fetch_wikipedia_text(row["WIKI Page URL"])

    # PDF
    if pd.notna(row.get("PDF Path", None)):
        text_data += extract_pdf_text(row["PDF Path"])

    # RAG extraction
    result = extract_info_rag(college_name, text_data)

    return {
        "College Name": college_name,
        "Location": result.get("location", "NA"),
        "NBA": result.get("nba", "NA"),
        "NAAC": result.get("naac", "NA"),
        "NIRF": result.get("nirf", "NA"),
        "Year of Foundation": result.get("year", "NA"),
        "Type": result.get("type", "NA"),
        "Category": result.get("category", "NA")
    }


def run_pipeline(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    results = []
    for _, row in df.iterrows():
        try:
            res = process_college(row)
            results.append(res)
        except Exception as e:
            print(f"Error processing {row['College Name']}: {e}")

    out_df = pd.DataFrame(results)
    out_df.to_csv(output_csv, index=False)
