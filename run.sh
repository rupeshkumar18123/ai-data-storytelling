#!/bin/bash

echo "🔄 Installing dependencies..."
pip install -r requirements.txt

echo "🚀 Starting AI-Powered Data Storytelling App..."
streamlit run frontend/app.py

