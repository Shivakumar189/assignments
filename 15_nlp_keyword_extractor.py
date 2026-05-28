# Assignment: NLP Mini App — Keyword Extractor (03/04/2026)
# Build a keyword extractor NLP app

import re
import string
from collections import Counter

STOPWORDS = {
    "i","me","my","we","our","you","your","he","him","she","her","it","its",
    "they","them","what","this","that","these","those","am","is","are","was",
    "were","be","been","have","has","had","do","does","did","will","would",
    "could","should","a","an","the","and","but","if","or","as","of","at","by",
    "for","with","about","to","from","in","on","no","not","so","very","just",
    "also","can","more","use","used","using","one","two","three","many","much"
}

def clean_and_tokenize(text: str) -> list:
    """Lowercase, remove punctuation, tokenize, remove stopwords."""
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = text.split()
    return [w for w in tokens if w not in STOPWORDS and len(w) > 2]

def extract_keywords(text: str, top_n: int = 8) -> list:
    """Extract top N keywords by frequency."""
    tokens = clean_and_tokenize(text)
    freq = Counter(tokens)
    return freq.most_common(top_n)

def summarize(text: str, num_sentences: int = 2) -> str:
    """Simple extractive summary: pick sentences with most keywords."""
    keywords = {w for w, _ in extract_keywords(text, 15)}
    sentences = re.split(r'(?<=[.!?])\s+', text.strip())
    scored = []
    for sent in sentences:
        tokens = clean_and_tokenize(sent)
        score = sum(1 for t in tokens if t in keywords)
        scored.append((score, sent))
    scored.sort(reverse=True)
    return ' '.join(s for _, s in scored[:num_sentences])

# ── Test Article ──────────────────────────────────
article = """
Artificial intelligence is transforming healthcare by enabling faster and more accurate diagnoses.
Machine learning algorithms can analyze medical images such as X-rays and MRI scans to detect
diseases like cancer at early stages. Natural language processing helps doctors extract insights
from patient records and clinical notes. AI-powered robots are being used in surgery to assist
surgeons with precision tasks. Drug discovery is also accelerating thanks to AI models that can
predict how molecules will interact. Hospitals are using AI dashboards to manage patient flow
and reduce waiting times. The technology is also improving mental health care through chatbots
that provide support and therapy suggestions. Despite these advances, experts emphasize the
importance of human oversight in all AI-driven medical decisions.
"""

print("=" * 65)
print("         🔍 NLP Mini App — Keyword Extractor")
print("=" * 65)
print(f"\n📄 Input Article ({len(article.split())} words):\n{article.strip()}\n")

keywords = extract_keywords(article, top_n=8)
print("🔑 Top Keywords:")
for word, freq in keywords:
    bar = '█' * freq
    print(f"   {word:<18} {freq:>2}x  {bar}")

summary = summarize(article, num_sentences=2)
print(f"\n📝 Auto-Summary:\n   {summary}")

print("\n" + "=" * 65)
print("✅ App Complete! Demonstrates: tokenization, stopword removal,")
print("   frequency analysis, and extractive summarization.")
print("=" * 65)
