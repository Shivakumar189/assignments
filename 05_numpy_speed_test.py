# Assignment: NumPy Speed Test (20/02/2026)
# Compare Python lists vs NumPy arrays with 1M numbers and measure execution time

import time
import numpy as np

N = 1_000_000  # 1 million numbers

print("=" * 50)
print("      ⚡ Python List vs NumPy Speed Test")
print(f"      Testing with {N:,} numbers")
print("=" * 50)

# ── Python List: Sum ──────────────────────────────
py_list = list(range(N))

start = time.time()
py_sum = sum(py_list)
py_time = time.time() - start
print(f"\n🐍 Python List sum : {py_sum:,}")
print(f"   Time taken      : {py_time:.5f} seconds")

# ── NumPy Array: Sum ─────────────────────────────
np_array = np.arange(N)

start = time.time()
np_sum = np_array.sum()
np_time = time.time() - start
print(f"\n🔢 NumPy Array sum : {int(np_sum):,}")
print(f"   Time taken      : {np_time:.5f} seconds")

# ── Speedup ──────────────────────────────────────
speedup = py_time / np_time if np_time > 0 else float('inf')
print(f"\n🚀 NumPy is ~{speedup:.1f}x faster than Python list")

# ── Python List: Mean ─────────────────────────────
start = time.time()
py_mean = sum(py_list) / len(py_list)
py_mean_time = time.time() - start

# ── NumPy Array: Mean ─────────────────────────────
start = time.time()
np_mean = np_array.mean()
np_mean_time = time.time() - start

print("\n" + "=" * 50)
print("📊 Mean Calculation Comparison:")
print(f"   Python List : {py_mean:.2f} ({py_mean_time:.5f}s)")
print(f"   NumPy Array : {np_mean:.2f} ({np_mean_time:.5f}s)")
print(f"   Speedup     : ~{py_mean_time/np_mean_time:.1f}x")

# ── 3 Observations ────────────────────────────────
print("\n" + "=" * 50)
print("📝 3 Key Observations:")
print("""
  1. NumPy is significantly faster than Python lists
     for large numerical operations because it uses
     optimized C code under the hood.

  2. NumPy arrays use fixed data types (dtype), which
     reduces memory overhead compared to Python lists
     that store objects with extra metadata.

  3. NumPy operations are vectorized — they apply to
     the entire array at once without explicit Python
     loops, making them ideal for data science tasks.
""")
print("=" * 50)
