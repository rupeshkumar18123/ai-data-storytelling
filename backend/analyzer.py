# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import io
# import google.generativeai as genai
# from backend.config import GEMINI_API_KEY

# # Configure Google Gemini AI
# genai.configure(api_key=GEMINI_API_KEY)

# def load_data(file_path):
#     """Loads the dataset from a CSV file."""
#     return pd.read_csv(file_path)

# def generate_ai_insights(df):
#     """Generates AI-powered insights based on the dataset using Gemini AI."""
#     model = genai.GenerativeModel("gemini-pro-1.5")
#     prompt = f"Analyze the following business dataset and provide key insights:\n\n{df.head(10).to_string()}"

#     response = model.generate_content(prompt)
#     return response.text if response else "No AI insights available."

# def generate_insight_graphs(df):
#     """Creates 5 different data visualizations and returns them as images."""
#     figures = {}

#     # Convert 'Date' column to datetime format if it exists
#     if "Date" in df.columns:
#         df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

#     # Insight 1: Revenue Trend Over Time
#     if "Date" in df.columns and "Revenue" in df.columns:
#         fig1, ax1 = plt.subplots()
#         sns.lineplot(x="Date", y="Revenue", data=df, ax=ax1)
#         ax1.set_title("📈 Revenue Trend Over Time")
#         figures["Revenue Trend"] = fig1

#     # Insight 2: Sales Distribution by Category
#     if "Category" in df.columns and "Sales" in df.columns:
#         fig2, ax2 = plt.subplots()
#         sns.barplot(x="Category", y="Sales", data=df, ax=ax2)
#         ax2.set_title("📊 Sales by Category")
#         figures["Sales by Category"] = fig2

#     # Insight 3: Profit Margin by Region (Fixed Argument Order)
#     if "Region" in df.columns and "Profit Margin" in df.columns:
#         fig3, ax3 = plt.subplots()
#         sns.boxplot(x="Region", y="Profit Margin", data=df, ax=ax3)  # Fixed `ax=ax3`
#         ax3.set_title("📦 Profit Margin by Region")
#         figures["Profit Margin by Region"] = fig3

#     # Insight 4: Customer Age Distribution
#     if "Customer Age" in df.columns:
#         fig4, ax4 = plt.subplots()
#         sns.histplot(df["Customer Age"], bins=10, kde=True, ax=ax4)
#         ax4.set_title("👤 Customer Age Distribution")
#         figures["Customer Age Distribution"] = fig4

#     # Insight 5: Payment Method Usage
#     if "Payment Method" in df.columns:
#         fig5, ax5 = plt.subplots()
#         df["Payment Method"].value_counts().plot.pie(autopct='%1.1f%%', ax=ax5)
#         ax5.set_title("💳 Payment Method Usage")
#         ax5.set_ylabel('')
#         figures["Payment Method Usage"] = fig5

#     return figures

# def save_graphs(figures):
#     """Converts figures to byte images and returns them."""
#     images = {}
#     for key, fig in figures.items():
#         img_io = io.BytesIO()
#         fig.savefig(img_io, format="png")
#         img_io.seek(0)
#         images[key] = img_io
#     return images


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import google.generativeai as genai
from backend.config import GEMINI_API_KEY

# Configure Google Gemini AI
genai.configure(api_key=GEMINI_API_KEY)

def load_data(file):
    """Loads the dataset from CSV or Excel."""
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    elif file.name.endswith(".xlsx"):
        return pd.read_excel(file)
    else:
        raise ValueError("Unsupported file format")

def generate_ai_insights(df):
    """Generates AI-powered insights based on the dataset using Gemini AI."""
    model = genai.GenerativeModel("gemini-pro-1.5")
    prompt = f"Analyze the following dataset and provide key insights:\n\n{df.head(10).to_string()}"

    response = model.generate_content(prompt)
    return response.text if response else "No AI insights available."

def generate_insight_graphs(df):
    """Dynamically generates insights based on available columns."""
    figures = {}

    # Convert Date columns
    for col in df.select_dtypes(include=["object"]).columns:
        try:
            df[col] = pd.to_datetime(df[col])
        except:
            pass  # Ignore if conversion fails

    numerical_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()
    categorical_cols = df.select_dtypes(include=["object"]).columns.tolist()
    datetime_cols = df.select_dtypes(include=["datetime64"]).columns.tolist()

    # Insight 1: Trend Over Time (if datetime & numerical exist)
    if datetime_cols and numerical_cols:
        fig, ax = plt.subplots()
        sns.lineplot(x=df[datetime_cols[0]], y=df[numerical_cols[0]], data=df, ax=ax)
        ax.set_title(f"📈 {numerical_cols[0]} Trend Over Time")
        figures[f"{numerical_cols[0]} Trend Over Time"] = fig

    # Insight 2: Bar Chart (if categorical & numerical exist)
    if categorical_cols and numerical_cols:
        fig, ax = plt.subplots()
        sns.barplot(x=df[categorical_cols[0]], y=df[numerical_cols[0]], data=df, ax=ax)
        ax.set_title(f"📊 {numerical_cols[0]} by {categorical_cols[0]}")
        figures[f"{numerical_cols[0]} by {categorical_cols[0]}"] = fig

    # Insight 3: Box Plot (if numerical exist)
    if categorical_cols and numerical_cols:
        fig, ax = plt.subplots()
        sns.boxplot(x=df[categorical_cols[0]], y=df[numerical_cols[0]], data=df, ax=ax)
        ax.set_title(f"📦 {numerical_cols[0]} Distribution by {categorical_cols[0]}")
        figures[f"{numerical_cols[0]} Distribution by {categorical_cols[0]}"] = fig

    # Insight 4: Histogram (if numerical exist)
    if numerical_cols:
        fig, ax = plt.subplots()
        sns.histplot(df[numerical_cols[0]], bins=10, kde=True, ax=ax)
        ax.set_title(f"🔢 Distribution of {numerical_cols[0]}")
        figures[f"Distribution of {numerical_cols[0]}"] = fig

    # Insight 5: Pie Chart (if categorical exist)
    if categorical_cols:
        fig, ax = plt.subplots()
        df[categorical_cols[0]].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
        ax.set_title(f"🍰 {categorical_cols[0]} Distribution")
        ax.set_ylabel("")
        figures[f"{categorical_cols[0]} Distribution"] = fig

    return figures

def save_graphs(figures):
    """Converts figures to byte images and returns them."""
    images = {}
    for key, fig in figures.items():
        img_io = io.BytesIO()
        fig.savefig(img_io, format="png")
        img_io.seek(0)
        images[key] = img_io
    return images
