import streamlit as st
import pandas as pd
from openai import OpenAI

# 🔑 Add your OpenAI API key here
client = OpenAI(api_key="enter your open AI API Key")

st.title("📊 Product Feedback Intelligence Dashboard")
st.info("Upload customer feedback data to generate AI-powered product insights.")

# Upload file
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("📄 Data Preview")
    st.write(df.head())

    if st.button("Generate Insights"):

        # --------- TEXT EXTRACTION ---------
        if 'review' in df.columns:
            text_series = df['review']
        else:
            text_series = df.iloc[:, 0]

        # --------- CLEANING ---------
        text_series = text_series.dropna()
        text_series = text_series.astype(str)
        text_series = text_series.str.strip()
        text_series = text_series[text_series != ""]

        # --------- JOIN TEXT ---------
        feedback_text = " ".join(text_series.tolist())

        # --------- LIMIT SIZE ---------
        feedback_text = feedback_text[:5000]

        # --------- PROMPT ---------
        prompt = f"""
You are a senior product manager analyzing customer feedback.

Based on the following user reviews:

1. Identify the TOP 5 most critical issues (group similar ones)
2. Explain WHY these issues matter (impact on user experience, churn, revenue)
3. Suggest concrete product improvements (specific, actionable)
4. Highlight quick wins vs long-term fixes

Keep the answer structured and concise.

User Reviews:
{feedback_text}
"""

        # --------- OPENAI API CALL ---------
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        # --------- OUTPUT ---------
        st.subheader("🤖 AI Insights")
        st.write(response.choices[0].message.content)
        st.success("Insights generated successfully!")