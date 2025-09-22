from transformers import pipeline

sentiment = pipeline("sentiment-analysis")

text = "I love Codec Technologies!"
result = sentiment(text)[0]
print(f"Sentiment: {result['label']}, Score: {result['score']:.2f}")
