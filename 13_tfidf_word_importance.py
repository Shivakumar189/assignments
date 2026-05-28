# Assignment: Word Importance Explorer (24/03/2026)
# Use TF-IDF on 5 documents and identify top keywords with explanation

from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

print("=" * 60)
print("      📖 Word Importance Explorer — TF-IDF")
print("=" * 60)

# ── 5 Sample Documents ────────────────────────────
documents = [
    "Machine learning is a type of artificial intelligence that enables computers to learn from data.",
    "Deep learning uses neural networks with many layers to solve complex problems in computer vision.",
    "Natural language processing helps computers understand human language and extract meaning from text.",
    "Data science combines statistics, programming, and machine learning to analyze large datasets.",
    "Computer vision allows machines to interpret images and videos, used in self-driving cars and robotics.",
]

doc_labels = [
    "Doc 1 — Machine Learning",
    "Doc 2 — Deep Learning",
    "Doc 3 — NLP",
    "Doc 4 — Data Science",
    "Doc 5 — Computer Vision",
]

# ── Compute TF-IDF ────────────────────────────────
vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = vectorizer.fit_transform(documents)
feature_names = np.array(vectorizer.get_feature_names_out())

# ── Top 5 Keywords per Document ───────────────────
print("\n🔑 Top Keywords per Document (by TF-IDF Score):\n")
for i, label in enumerate(doc_labels):
    row = tfidf_matrix[i].toarray().flatten()
    top_indices = row.argsort()[-5:][::-1]
    top_keywords = [(feature_names[j], round(row[j], 4)) for j in top_indices]
    print(f"📄 {label}")
    for word, score in top_keywords:
        bar = '█' * int(score * 30)
        print(f"   {word:<20} {score:.4f}  {bar}")
    print()

# ── Explanation ───────────────────────────────────
print("=" * 60)
print("""💡 What is TF-IDF?

  TF  (Term Frequency)     = How often a word appears in a document.
  IDF (Inverse Doc Freq)   = How rare the word is across all documents.
  TF-IDF Score             = TF × IDF

  High TF-IDF → Word is FREQUENT in this doc but RARE in others
                → It is a distinctive keyword for that document.

  Example: "neural" appears only in Doc 2, so it has high IDF
  and a high TF-IDF score — making it a key identifying word.

  Use cases: Search engines, document classification, keyword
  extraction, content recommendation systems.
""")
print("=" * 60)
