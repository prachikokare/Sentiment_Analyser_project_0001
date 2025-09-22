

# AI-Based Sentiment Analyzer

## 📌 Project Overview
The **AI-Based Sentiment Analyzer** is a beginner-friendly Python project that uses **Hugging Face Transformers** to analyze the sentiment of any text.  
It can classify text as **Positive, Negative, or Neutral** and provides both a **command-line interface (CLI)** and a **web interface using Flask**.  

This project is ideal for beginners learning **NLP, Python web development, and machine learning deployment**.

---

## 🚀 Features
- Analyze **positive, negative, or neutral sentiment** from any text.  
- **Command-Line Interface** for quick testing.  
- **Interactive Flask Web App** for easy text input and visualization.  
- Beginner-friendly and **fully functional locally**.  
- Easily extendable to handle **multiple texts** or **batch analysis**.  

---

## 🛠️ Technologies Used
| Technology | Purpose |
|------------|---------|
| Python     | Core programming language |
| Hugging Face Transformers | Pre-trained NLP models for sentiment analysis |
| Torch      | Backend for Transformers |
| Flask      | Web application framework |
| HTML/CSS   | Web interface design |

---

## 📂 Folder Structure

sntimentAnalyser/ │── app_sentiment.py       # Flask web application │── sentiment.py           # Command-line sentiment analysis script │── templates/ │   └── index.html         # HTML template for Flask UI │── venv/                  # Python virtual environment (excluded from GitHub via .gitignore)

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/<YourUsername>/SentimentAnalyzer.git
cd SentimentAnalyzer

2. Create and Activate Virtual Environment

python -m venv venv
# Windows CMD
venv\Scripts\activate
# PowerShell
.\venv\Scripts\Activate.ps1
# macOS/Linux
source venv/bin/activate

3. Install Required Packages

pip install transformers torch flask


---

🏃 Usage

1️⃣ Command-Line Script

Run the CLI script to analyze sentiment directly from Python:

python sentiment.py

Change the text in sentiment.py or add multiple sentences.

Example Output:


Sentiment: POSITIVE, Score: 0.999
Sentiment: NEGATIVE, Score: 0.872

2️⃣ Web App (Flask)

Run the Flask web application:

python app_sentiment.py

Open your browser at http://127.0.0.1:5000/

Enter text in the input box → Click Analyze Sentiment → View results on the page.



---

🎨 Optional Enhancements

Add color-coded results for Positive/Negative/Neutral sentiment.

Enable batch analysis by uploading multiple texts at once.

Improve UI with Bootstrap or Tailwind CSS for a modern look.

Add charts or graphs to visualize sentiment trends.



---

📚 References

Hugging Face Transformers Documentation

Flask Documentation

PyTorch Documentation



---

👩‍💻 Author

Prachi Kokare


---

📝 License

This project is open-source and free to use.



