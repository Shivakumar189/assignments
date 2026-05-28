# Assignment: Build a Text Cleaner (21/03/2026)
# Remove punctuation, lowercase text, remove stopwords and test it

import re
import string

# Minimal stopwords list (install nltk for full list)
STOPWORDS = {
    "i","me","my","myself","we","our","you","your","he","him","his","she","her",
    "it","its","they","them","their","what","which","who","this","that","these",
    "those","am","is","are","was","were","be","been","being","have","has","had",
    "do","does","did","will","would","could","should","may","might","shall","can",
    "a","an","the","and","but","if","or","because","as","of","at","by","for",
    "with","about","into","through","during","to","from","in","out","on","off",
    "over","under","again","then","once","here","there","when","where","why",
    "how","all","both","each","few","more","most","other","some","such","no",
    "not","only","same","so","than","too","very","just","s","t","don","ve","ll","re"
}

def clean_text(text: str, remove_stopwords: bool = True) -> str:
    """Full text cleaning pipeline."""
    # 1. Lowercase
    text = text.lower()

    # 2. Remove URLs
    text = re.sub(r'http\S+|www\S+', '', text)

    # 3. Remove emojis & special unicode
    text = text.encode('ascii', 'ignore').decode('ascii')

    # 4. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # 5. Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    # 6. Remove stopwords
    if remove_stopwords:
        words = text.split()
        words = [w for w in words if w not in STOPWORDS]
        text = ' '.join(words)

    return text

# ── Test Sentences ────────────────────────────────
test_sentences = [
    "OMG!! This movie was AMAZING 😍🔥 totally worth it!!!",
    "I   can't believe how gr8 the product is... 100% recommend!!!",
    "Check this out: https://example.com — it's really cool stuff!",
    "lol u shud totally go 2 the event its gonna b lit 🎉",
    "The food was ok, but service was BAD. Will not return. 😤",
]

print("=" * 60)
print("        🧹 Text Cleaner — NLP Preprocessing")
print("=" * 60)

for i, sentence in enumerate(test_sentences, 1):
    cleaned = clean_text(sentence)
    print(f"\n📝 Original  [{i}]: {sentence}")
    print(f"✅ Cleaned   [{i}]: {cleaned}")

print("\n" + "=" * 60)
print("🔧 Steps Applied:")
print("  1. Lowercased all text")
print("  2. Removed URLs (http/https/www)")
print("  3. Stripped emojis & unicode")
print("  4. Removed all punctuation")
print("  5. Collapsed extra whitespace")
print("  6. Removed common stopwords")
print("=" * 60)
