# Assignment: Dataset Detective (24/02/2026)
# Load a dataset, display top rows, find highest value column, count missing values

import pandas as pd
import numpy as np

# ── Create a sample dataset ───────────────────────
np.random.seed(42)
data = {
    "StudentID":  range(1, 21),
    "Name":       ["Alice","Bob","Charlie","Diana","Eve","Frank","Grace","Henry",
                   "Iris","Jack","Karen","Leo","Mia","Nate","Olivia","Paul",
                   "Quinn","Rose","Sam","Tina"],
    "MathScore":  np.random.randint(40, 100, 20).tolist(),
    "SciScore":   [np.nan if i % 7 == 0 else int(np.random.randint(35, 100))
                   for i in range(20)],
    "EngScore":   np.random.randint(50, 100, 20).tolist(),
    "Attendance": [np.nan if i % 9 == 0 else round(np.random.uniform(60, 100), 1)
                   for i in range(20)],
    "City":       np.random.choice(["Mumbai","Delhi","Chennai","Kolkata","Pune"], 20).tolist(),
}

df = pd.DataFrame(data)

print("=" * 60)
print("              📊 Dataset Detective")
print("=" * 60)

# 1. Top 5 rows
print("\n🔍 Top 5 Rows of the Dataset:")
print(df.head().to_string(index=False))

# 2. Dataset shape
print(f"\n📐 Shape: {df.shape[0]} rows × {df.shape[1]} columns")

# 3. Column with highest mean value (numeric only)
numeric_cols = df.select_dtypes(include='number').columns.tolist()
numeric_cols = [c for c in numeric_cols if c != "StudentID"]
col_means = df[numeric_cols].mean()
highest_col = col_means.idxmax()
print(f"\n🏆 Column with Highest Average Value: '{highest_col}' ({col_means[highest_col]:.2f})")

# 4. Missing values
missing = df.isnull().sum()
print("\n❓ Missing Values per Column:")
for col, count in missing.items():
    pct = (count / len(df)) * 100
    status = f"  ⚠️ {count} missing ({pct:.0f}%)" if count > 0 else "  ✅ None"
    print(f"   {col:<14}: {status}")

# 5. Five Insights
print("\n" + "=" * 60)
print("💡 5 Insights from the Dataset:")
print(f"""
  1. The dataset has {df.shape[0]} students from {df['City'].nunique()} different cities.

  2. Average Math Score is {df['MathScore'].mean():.1f}, Science is {df['SciScore'].mean():.1f},
     and English is {df['EngScore'].mean():.1f}.

  3. '{highest_col}' has the highest average score at {col_means[highest_col]:.2f},
     suggesting students perform best in this subject.

  4. There are {missing.sum()} missing values in total, mostly in
     'SciScore' and 'Attendance' — these need cleaning before ML.

  5. City distribution is roughly uniform across {df['City'].nunique()} cities,
     meaning no strong geographic bias in this sample.
""")
print("=" * 60)
