# Assignment: Movie Review Analyzer (26/03/2026)
# Build a simple sentiment analyzer and test on 5 reviews

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
import numpy as np

print("=" * 60)
print("     🎬 Movie Review Sentiment Analyzer")
print("=" * 60)

# ── Training Data ─────────────────────────────────
train_reviews = [
    "This movie was absolutely fantastic and thrilling",
    "I loved every moment of this beautiful film",
    "Outstanding performance by all the actors",
    "A masterpiece of storytelling and direction",
    "One of the best movies I have ever seen",
    "Brilliant cinematography and wonderful music",
    "Completely boring and a total waste of time",
    "Terrible acting and a very confusing plot",
    "I hated this movie it was awful and dull",
    "Worst film I have ever seen do not watch",
    "Very disappointing and poorly written script",
    "Nothing made sense the story was a mess",
]
train_labels = [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0]

# ── Train Model ───────────────────────────────────
model = Pipeline([
    ('tfidf', TfidfVectorizer(ngram_range=(1, 2), stop_words='english')),
    ('clf',   LogisticRegression(max_iter=1000)),
])
model.fit(train_reviews, train_labels)

# ── 5 Test Reviews ────────────────────────────────
test_reviews = [
    "The film had amazing visuals and a gripping story",
    "I fell asleep halfway through it was so boring",
    "A decent movie with some good and bad moments",
    "Loved the chemistry between the lead actors",
    "Poor direction and very weak character development",
]

print("\n🎭 Sentiment Analysis Results:\n")
predictions = model.predict(test_reviews)
probabilities = model.predict_proba(test_reviews)

for review, pred, prob in zip(test_reviews, predictions, probabilities):
    sentiment = "😊 POSITIVE" if pred == 1 else "😞 NEGATIVE"
    confidence = max(prob) * 100
    print(f"  📝 Review    : {review}")
    print(f"  🏷️  Sentiment : {sentiment}  (Confidence: {confidence:.1f}%)")
    print()

print("=" * 60)
print("📌 How it works:")
print("""
  1. TF-IDF converts reviews to numerical feature vectors.
  2. Logistic Regression learns which words/phrases indicate
     positive vs negative sentiment from training examples.
  3. For new reviews, it calculates probability of each class
     and picks the higher one as the prediction.
""")
print("=" * 60)
