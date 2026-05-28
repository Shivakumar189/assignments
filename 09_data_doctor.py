# Assignment: Data Doctor (26/02/2026)
# Clean a dataset: handle missing values, remove duplicates, standardize text

import pandas as pd
import numpy as np

print("=" * 55)
print("          🩺 Data Doctor — Dataset Cleaner")
print("=" * 55)

# ── Create a Messy Dataset ────────────────────────
raw_data = {
    "Name":    ["alice", "BOB", "Charlie", "bob", "DIANA", "Eve", None, "Frank", "grace", "DIANA"],
    "Age":     [22, None, 25, 22, 28, None, 30, 35, 27, 28],
    "City":    ["mumbai", "DELHI", "Chennai", "delhi", "Pune", "MUMBAI", "Kolkata", "pune", "Chennai", "Pune"],
    "Score":   [85, 90, None, 90, 78, 88, 72, None, 95, 78],
    "Gender":  ["female", "Male", "MALE", "male", "Female", "female", "M", "F", "female", "Female"],
}

df_raw = pd.DataFrame(raw_data)
print("\n🔴 BEFORE CLEANING:")
print(df_raw.to_string(index=False))
print(f"\nShape: {df_raw.shape} | Missing: {df_raw.isnull().sum().sum()} | Duplicates: {df_raw.duplicated().sum()}")

# ── Step 1: Standardize text columns ──────────────
df = df_raw.copy()
df['Name'] = df['Name'].str.strip().str.title()
df['City'] = df['City'].str.strip().str.title()
df['Gender'] = df['Gender'].str.strip().str.lower()
df['Gender'] = df['Gender'].replace({'m': 'male', 'f': 'female'})

# ── Step 2: Handle missing values ─────────────────
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Score'].fillna(df['Score'].mean().round(1), inplace=True)
df['Name'].fillna('Unknown', inplace=True)

# ── Step 3: Remove duplicates ─────────────────────
df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

print("\n\n✅ AFTER CLEANING:")
print(df.to_string(index=False))
print(f"\nShape: {df.shape} | Missing: {df.isnull().sum().sum()} | Duplicates: {df.duplicated().sum()}")

# ── Why Cleaning Matters ───────────────────────────
print("""
📝 WHY DATA CLEANING MATTERS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. MISSING VALUES: ML models crash or produce wrong results
   when given NaN/null. Filling with mean or median preserves
   statistical integrity.

2. DUPLICATES: Duplicate rows skew model training — the model
   sees certain patterns more often, creating bias in predictions.

3. INCONSISTENT TEXT: 'mumbai', 'MUMBAI', 'Mumbai' are treated
   as 3 different cities by an algorithm. Standardizing ensures
   correct grouping and encoding.

4. DIRTY DATA = WRONG MODELS: "Garbage in, garbage out" — no
   algorithm can fix fundamentally broken input data.

5. REAL DATASETS are almost always messy. Cleaning is often
   70–80% of actual ML project work.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
