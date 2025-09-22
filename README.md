# Sentiment_Analyser00
AI-Based Sentiment Analyzer
Project Overview

The AI-Based Sentiment Analyzer is a web application that analyzes text input (such as product reviews, social media posts, or user feedback) to determine the sentiment of the text as Positive, Negative, or Neutral. The app uses pre-trained NLP models from Hugging Face Transformers and provides a real-time, interactive interface for users.

Features

Input text through a web interface.

Detects sentiment (Positive, Negative, Neutral) using AI.

Displays visual results for easy understanding.

Stores user inputs and sentiment results in MongoDB (optional).

Tech Stack

Backend: Python, Flask

AI/NLP: Transformers, Hugging Face

Database: MongoDB (optional)

Frontend: HTML, Bootstrap (for simple UI)

Installation Instructions

Clone the repository

git clone https://github.com/<your-username>/AI-Sentiment-Analyzer.git
cd AI-Sentiment-Analyzer


Create a virtual environment

python -m venv venv


Activate the environment

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

Install dependencies

pip install -r requirements.txt
python -m spacy download en_core_web_sm

Usage

Run the Flask app:

python app.py


Open the browser at:

http://127.0.0.1:5000/


Enter text in the input box and click Analyze.

The app will display the sentiment result.

Project Structure
AI-Sentiment-Analyzer/
│
├─ app.py          # Flask backend
├─ parser.py       # Sentiment analysis logic
├─ templates/
│   └─ index.html  # Web interface
├─ requirements.txt
├─ uploads/        # Optional folder for uploaded text files
└─ README.md       # Project documentation

Future Enhancements
Add real-time sentiment charts using Plotly or Chart.js.

Add multi-language support.

Deploy online for public access using Render or Streamlit Cloud.

Author

Prachi Kokare – GitHub Profile
