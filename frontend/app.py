
# import streamlit as st
# import pandas as pd
# from backend.ai_processor import generate_summary
# from backend.chatbot import chatbot_response
# from backend.pdf_generator import save_summary_to_pdf

# st.title("📊 AI-Powered Business Insights")

# uploaded_file = st.file_uploader("📂 Upload Business Data (CSV)", type="csv")
# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.write(df.head())

#     if st.button("🔍 Generate AI Insights"):
#         summary = generate_summary(df)
#         st.write("### 📜 AI-Generated Summary")
#         st.write(summary)

#     user_query = st.text_input("💬 Ask about your data:")
#     if user_query:
#         answer = chatbot_response(user_query, df)
#         st.write(f"**AI Response:** {answer}")

#     if st.button("📄 Download Report"):
#         save_summary_to_pdf(summary)
#         st.success("✅ Report saved as PDF!")


# import streamlit as st
# import pandas as pd
# from backend.analyzer import load_data, generate_insight_graphs, save_graphs, generate_ai_insights
# from backend.chatbot import chatbot_response
# from backend.pdf_generator import save_summary_to_pdf

# # Configure page size
# st.set_page_config(page_title="📊 AI-Powered Business Dashboard", layout="wide")

# # Sidebar for file upload
# st.sidebar.title("🔍 Upload Dataset")
# uploaded_file = st.sidebar.file_uploader("Upload CSV File", type="csv")

# if uploaded_file:
#     df = load_data(uploaded_file)

#     # Sidebar Filters
#     st.sidebar.subheader("🔎 Filters")
#     category_filter = st.sidebar.selectbox("Select Category", ["All"] + list(df["Category"].unique()))
#     region_filter = st.sidebar.selectbox("Select Region", ["All"] + list(df["Region"].unique()))

#     # Apply filters
#     if category_filter != "All":
#         df = df[df["Category"] == category_filter]
#     if region_filter != "All":
#         df = df[df["Region"] == region_filter]

#     # Generate AI Insights
#     st.title("📊 AI-Powered Business Insights Dashboard")
    
#     # AI Summary Section
#     if st.button("🔍 Generate AI Insights"):
#         st.subheader("🤖 AI-Generated Insights")
#         ai_insights = generate_ai_insights(df)
#         st.write(ai_insights)

#     # Chatbot Interaction
#     user_query = st.text_input("💬 Ask about your data:")
#     if user_query:
#         answer = chatbot_response(user_query, df)
#         st.write(f"**AI Response:** {answer}")

#     # Data Visualizations
#     figures = generate_insight_graphs(df)
#     images = save_graphs(figures)

#     # Dashboard Layout (900x600px)
#     st.subheader("📊 Data Visualizations")
#     col1, col2 = st.columns(2)

#     with col1:
#         st.image(images["Revenue Trend"], caption="📈 Revenue Trend Over Time", use_column_width=True)
#         st.image(images["Sales by Category"], caption="📊 Sales by Category", use_column_width=True)

#     with col2:
#         st.image(images["Profit Margin by Region"], caption="📦 Profit Margin by Region", use_column_width=True)
#         st.image(images["Customer Age Distribution"], caption="👤 Customer Age Distribution", use_column_width=True)
#         st.image(images["Payment Method Usage"], caption="💳 Payment Method Usage", use_column_width=True)

#     # Downloadable Report
#     if st.button("📄 Download AI Report"):
#         save_summary_to_pdf(ai_insights)
#         st.success("✅ AI-Generated Report saved as PDF!")

# else:
#     st.warning("📂 Please upload a CSV file to generate insights.")


import streamlit as st
import pandas as pd
from backend.analyzer import load_data, generate_insight_graphs, save_graphs, generate_ai_insights

# Configure page size
st.set_page_config(page_title="📊 AI-Powered Business Dashboard", layout="wide")

# Sidebar for file upload
st.sidebar.title("🔍 Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload CSV File", type=["csv", "xlsx"])

if uploaded_file:
    # Load data
    df = load_data(uploaded_file)

    # Display dataset summary
    st.sidebar.subheader("📌 Dataset Overview")
    st.sidebar.write(f"🔢 Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    st.sidebar.write("📋 Columns:", df.columns.tolist())

    # Identify column types
    categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()
    numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    datetime_cols = df.select_dtypes(include=["datetime64"]).columns.tolist()

    # Sidebar Filters (Automatically created based on dataset)
    st.sidebar.subheader("🔎 Filters")

    filters = {}
    for col in categorical_cols:
        selected_value = st.sidebar.selectbox(f"Filter by {col}", ["All"] + list(df[col].dropna().unique()))
        if selected_value != "All":
            filters[col] = selected_value

    # Apply filters
    for col, value in filters.items():
        df = df[df[col] == value]

    # Generate AI insights
    st.title("📊 AI-Powered Business Insights Dashboard")
    
    if st.button("🤖 Generate AI Insights"):
        st.subheader("📜 AI-Generated Insights")
        ai_insights = generate_ai_insights(df)
        st.write(ai_insights)

    # Generate dynamic visualizations
    figures = generate_insight_graphs(df)
    images = save_graphs(figures)

    # Display visualizations dynamically
    st.subheader("📊 Data Visualizations")
    cols = st.columns(2)

    index = 0
    for key, img in images.items():
        with cols[index % 2]:  # Alternate between two columns
            st.image(img, caption=key, use_column_width=True)
        index += 1

else:
    st.warning("📂 Please upload a CSV file to generate insights.")

