import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Startup Funding Explorer", layout="centered")

# Title and instructions
st.title("💰 Startup Funding in India Explorer")
st.markdown("Analyze which startup sectors received the most funding in India.")

# Upload CSV
uploaded_file = st.file_uploader("Upload your startup funding CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Raw Data Preview")
    st.dataframe(df.head())

    # Rename columns if needed (adjust this if your column names are different)
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

    # Clean 'amount' column
    if 'amount' in df.columns and 'vertical' in df.columns:
        try:
            df['amount'] = df['amount'].astype(str).str.replace(',', '')
            df['amount'] = df['amount'].astype(float)

            # Group and summarize
            sector_funding = df.groupby('vertical')['amount'].sum().sort_values(ascending=False).head(10)

            # Plot
            st.subheader("📊 Top 10 Sectors by Total Funding")
            fig, ax = plt.subplots(figsize=(10, 5))
            sector_funding.plot(kind='bar', color='skyblue', ax=ax)
            plt.xlabel("Startup Sector")
            plt.ylabel("Total Funding (USD)")
            plt.xticks(rotation=45)
            plt.title("Top 10 Startup Sectors by Funding")
            st.pyplot(fig)

            # Show data
            st.subheader("📋 Funding Table")
            st.dataframe(sector_funding)

        except Exception as e:
            st.error("Error processing the amount column. Please check your CSV format.")
            st.code(str(e))
    else:
        st.warning("The dataset must contain at least the columns: 'vertical' and 'amount'")
