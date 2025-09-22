from flask import Flask, request, render_template
from transformers import pipeline

app = Flask(__name__)
sentiment = pipeline("sentiment-analysis")

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        text = request.form.get("text")
        if text:
            result = sentiment(text)[0]
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
