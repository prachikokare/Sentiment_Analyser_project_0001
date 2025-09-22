# AI-Based Sentiment Analyzer

A beginner-friendly Python project that analyzes the sentiment of text using **Hugging Face Transformers**.  
You can run it as a **Python script** or as a **web app using Flask**.

---

## Features

- Analyze **positive, negative, or neutral** sentiment from any text.  
- Simple **Python script** for command-line usage.  
- Interactive **web interface** using Flask for easy testing.  
- Beginner-friendly and fully functional locally.  

---

## Folder Structure

sntimentAnalyser/
│
├─ app_sentiment.py # Flask web app
├─ sentiment.py # Python script for CLI sentiment analysis
├─ venv/ # Virtual environment (excluded from GitHub via .gitignore)
└─ templates/
└─ index.html # HTML template for Flask web interface

yaml
Copy code

---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/<YourUsername>/SentimentAnalyzer.git
cd SentimentAnalyzer
Create and activate virtual environment:

bash
Copy code
python -m venv venv
venv\Scripts\activate      # CMD
# or
.\venv\Scripts\Activate.ps1  # PowerShell

##Install required packages:
bash
Copy code
pip install transformers torch flask
Usage
1️⃣ Command-Line Script
bash
Copy code
python sentiment.py
Change the text in sentiment.py or add multiple texts.

##Output example:

yaml
Copy code
Sentiment: POSITIVE, Score: 0.999
2️⃣ Web App (Flask)
bash
Copy code
python app_sentiment.py
Open browser: http://127.0.0.1:5000/

Enter text → Click Analyze Sentiment → See results on the page.

##Optional Enhancements
Color-coded results for Positive/Negative/Neutral sentiment.

Upload multiple texts at once and display results in a table.

Use Bootstrap or Tailwind CSS for a modern UI.

Author
Prachi Kokare

License
This project is open-source and free to use.
