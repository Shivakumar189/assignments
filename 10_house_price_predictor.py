# Assignment: House Price Predictor (09/03/2026)
# Train a Linear Regression model, predict prices, test with new input

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

print("=" * 55)
print("     🏠 House Price Predictor — Linear Regression")
print("=" * 55)

# ── Dataset (Area in sq ft → Price in Lakhs) ──────
np.random.seed(42)
area = np.array([500, 650, 750, 800, 900, 1000, 1100, 1200, 1350,
                 1500, 1600, 1800, 2000, 2200, 2500])
price = np.array([15, 20, 25, 28, 33, 38, 42, 47, 52,
                  60, 65, 75, 85, 95, 110])

# Add slight noise
price = price + np.random.normal(0, 2, len(price))

# Reshape for sklearn
X = area.reshape(-1, 1)
y = price

# ── Train/Test Split ──────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ── Train Model ───────────────────────────────────
model = LinearRegression()
model.fit(X_train, y_train)

# ── Evaluate ──────────────────────────────────────
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"\n📐 Model Equation:")
print(f"   Price = {model.coef_[0]:.4f} × Area + ({model.intercept_:.2f})")
print(f"\n📊 Model Performance:")
print(f"   R² Score : {r2:.4f}  (1.0 = perfect)")
print(f"   MSE      : {mse:.2f}")

# ── Predict New Inputs ────────────────────────────
print(f"\n🔮 Predictions for New Houses:")
new_areas = [700, 1300, 2000, 3000]
for a in new_areas:
    pred = model.predict([[a]])[0]
    print(f"   Area: {a:>5} sq ft → Predicted Price: ₹{pred:.1f} Lakhs")

# ── Plot ──────────────────────────────────────────
plt.figure(figsize=(8, 5))
plt.scatter(X_train, y_train, color='steelblue', label='Training Data', s=60)
plt.scatter(X_test, y_test, color='tomato', label='Test Data', s=60, zorder=5)
line_x = np.linspace(area.min(), area.max(), 100).reshape(-1, 1)
plt.plot(line_x, model.predict(line_x), color='green', linewidth=2, label='Regression Line')
plt.title('House Price Predictor', fontsize=14, fontweight='bold')
plt.xlabel('Area (sq ft)')
plt.ylabel('Price (Lakhs ₹)')
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('10_house_price_predictor.png', dpi=150)
plt.show()
print("\n✅ Plot saved as '10_house_price_predictor.png'")
print("=" * 55)
