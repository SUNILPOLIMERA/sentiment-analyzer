from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive"
    elif polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment

if __name__ == "__main__":
    print("=== AI Sentiment Analyzer ===")
    text = input("Enter a sentence: ")
    result = analyze_sentiment(text)
    print("Sentiment:", result)
