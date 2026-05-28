# Assignment: Build Your First Dataset (03/03/2026)
# Create a dataset (study hours vs marks), identify features & labels, predict relationship

import numpy as np
import matplotlib.pyplot as plt

print("=" * 50)
print("    📂 Build Your First Dataset")
print("=" * 50)

# ── Step 1: Create the Dataset ────────────────────
study_hours = [1, 2, 2.5, 3, 4, 4.5, 5, 6, 6.5, 7, 8, 9, 10]
marks        = [35, 42, 48, 55, 60, 65, 70, 75, 78, 82, 88, 93, 97]

print("\n📊 Dataset: Study Hours vs Marks")
print(f"{'Study Hours':>12} | {'Marks':>6}")
print("-" * 22)
for h, m in zip(study_hours, marks):
    print(f"{h:>12} | {m:>6}")

# ── Step 2: Features & Labels ─────────────────────
print("""
🔑 Feature (Input / X):
   → Study Hours — the variable we control or observe.

🎯 Label (Output / Y):
   → Marks — the outcome we want to predict.
""")

# ── Step 3: Predict Relationship (Simple Linear Regression manually)
X = np.array(study_hours)
Y = np.array(marks)

# Least squares formula
n = len(X)
m_slope = (n * np.dot(X, Y) - X.sum() * Y.sum()) / (n * (X**2).sum() - X.sum()**2)
b_intercept = (Y.sum() - m_slope * X.sum()) / n

print(f"📈 Linear Relationship: Marks = {m_slope:.2f} × StudyHours + {b_intercept:.2f}")
print(f"\n🔮 Prediction Examples:")
for hours in [3, 5, 8, 11]:
    predicted = m_slope * hours + b_intercept
    print(f"   Study {hours:>2} hours → Predicted Marks: {predicted:.1f}")

# ── Step 4: Plot ──────────────────────────────────
x_line = np.linspace(0, 11, 100)
y_line = m_slope * x_line + b_intercept

plt.figure(figsize=(8, 5))
plt.scatter(X, Y, color='royalblue', s=80, zorder=5, label='Actual Data')
plt.plot(x_line, y_line, color='tomato', linewidth=2, label='Best Fit Line')
plt.title('Study Hours vs Marks', fontsize=14, fontweight='bold')
plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('08_study_vs_marks.png', dpi=150)
plt.show()
print("\n✅ Plot saved as '08_study_vs_marks.png'")
print("=" * 50)
