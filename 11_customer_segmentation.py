# Assignment: Customer Segmentation (11/03/2026 & 18/03/2026)
# K-Means clustering on mall dataset and describe customer groups

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

print("=" * 55)
print("     🛍️  Customer Segmentation — K-Means Clustering")
print("=" * 55)

# ── Simulated Mall Customer Dataset ───────────────
np.random.seed(42)

# Annual Income (k$) and Spending Score (1–100)
data = np.array([
    *np.random.multivariate_normal([25, 79], [[20,0],[0,15]], 40),   # Low income, high spenders
    *np.random.multivariate_normal([55, 55], [[10,0],[0,10]], 50),   # Middle class, moderate
    *np.random.multivariate_normal([85, 20], [[15,0],[0,10]], 35),   # High income, low spenders
    *np.random.multivariate_normal([85, 82], [[15,0],[0,10]], 35),   # High income, high spenders
    *np.random.multivariate_normal([30, 20], [[10,0],[0,8]],  40),   # Low income, low spenders
])

X = data

# ── Scale Data ────────────────────────────────────
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# ── KMeans with 5 Clusters ────────────────────────
kmeans = KMeans(n_clusters=5, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)
centers = scaler.inverse_transform(kmeans.cluster_centers_)

# ── Print Cluster Summary ─────────────────────────
cluster_names = {
    "Cluster A": "Careful Spenders (Low Income, Low Spending)",
    "Cluster B": "Target Customers (Low Income, High Spending)",
    "Cluster C": "Standard Customers (Middle Income, Moderate Spending)",
    "Cluster D": "Conservative Rich (High Income, Low Spending)",
    "Cluster E": "Premium Customers (High Income, High Spending)",
}

print("\n📊 Cluster Centroids:")
print(f"{'Cluster':>9} | {'Annual Income ($k)':>18} | {'Spending Score':>14}")
print("-" * 50)
for i, (name, desc) in enumerate(cluster_names.items()):
    inc = centers[i][0]
    score = centers[i][1]
    print(f"{name:>9} | {inc:>18.1f} | {score:>14.1f}")

print("\n🧑‍🤝‍🧑 Customer Group Descriptions:")
for name, desc in cluster_names.items():
    print(f"  • {name}: {desc}")

# ── Plot ──────────────────────────────────────────
colors = ['#E63946','#457B9D','#2A9D8F','#F4A261','#9B5DE5']
fig, ax = plt.subplots(figsize=(9, 6))
for cluster_id in range(5):
    mask = labels == cluster_id
    ax.scatter(X[mask, 0], X[mask, 1], c=colors[cluster_id],
               label=f'Cluster {chr(65+cluster_id)}', s=60, alpha=0.75, edgecolors='white')
ax.scatter(centers[:, 0], centers[:, 1], c='black', marker='X', s=200, zorder=10, label='Centroids')
ax.set_title('Customer Segmentation via K-Means', fontsize=14, fontweight='bold')
ax.set_xlabel('Annual Income ($k)')
ax.set_ylabel('Spending Score (1–100)')
ax.legend()
ax.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('11_customer_segmentation.png', dpi=150)
plt.show()
print("\n✅ Plot saved as '11_customer_segmentation.png'")
print("=" * 55)
