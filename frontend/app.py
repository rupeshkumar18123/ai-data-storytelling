
import streamlit as st
import pandas as pd
from backend.ai_processor import generate_summary
from backend.chatbot import chatbot_response
from backend.pdf_generator import save_summary_to_pdf

st.title("📊 AI-Powered Business Insights")

uploaded_file = st.file_uploader("📂 Upload Business Data (CSV)", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    if st.button("🔍 Generate AI Insights"):
        summary = generate_summary(df)
        st.write("### 📜 AI-Generated Summary")
        st.write(summary)

    user_query = st.text_input("💬 Ask about your data:")
    if user_query:
        answer = chatbot_response(user_query, df)
        st.write(f"**AI Response:** {answer}")

    if st.button("📄 Download Report"):
        save_summary_to_pdf(summary)
        st.success("✅ Report saved as PDF!")
