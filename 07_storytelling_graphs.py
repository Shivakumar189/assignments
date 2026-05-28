# Assignment: Storytelling with Graphs (28/02/2026)
# Create bar chart, pie chart, histogram and write a data story

import matplotlib.pyplot as plt
import numpy as np

# ── Sample Data ───────────────────────────────────
subjects = ['Math', 'Science', 'English', 'History', 'CS']
avg_scores = [72, 68, 80, 65, 88]

city_students = {'Mumbai': 35, 'Delhi': 28, 'Chennai': 20, 'Pune': 17}

np.random.seed(0)
all_scores = np.random.normal(loc=74, scale=12, size=200).clip(0, 100)

fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle('📊 Student Performance Story', fontsize=16, fontweight='bold', y=1.02)

# ── 1. Bar Chart: Average Score by Subject ────────
colors = ['#4C72B0','#DD8452','#55A868','#C44E52','#8172B2']
bars = axes[0].bar(subjects, avg_scores, color=colors, edgecolor='white', width=0.6)
axes[0].set_title('Average Score by Subject', fontsize=13, fontweight='bold')
axes[0].set_xlabel('Subject')
axes[0].set_ylabel('Average Score')
axes[0].set_ylim(0, 100)
for bar, score in zip(bars, avg_scores):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 str(score), ha='center', fontsize=10, fontweight='bold')
axes[0].axhline(y=np.mean(avg_scores), color='red', linestyle='--', linewidth=1.2,
                label=f'Avg: {np.mean(avg_scores):.1f}')
axes[0].legend()

# ── 2. Pie Chart: City Distribution ───────────────
pie_colors = ['#4C72B0','#DD8452','#55A868','#C44E52']
wedge_props = {'linewidth': 2, 'edgecolor': 'white'}
axes[1].pie(city_students.values(), labels=city_students.keys(),
            autopct='%1.1f%%', colors=pie_colors,
            wedgeprops=wedge_props, startangle=140,
            textprops={'fontsize': 10})
axes[1].set_title('Student Distribution by City', fontsize=13, fontweight='bold')

# ── 3. Histogram: Score Distribution ─────────────
axes[2].hist(all_scores, bins=15, color='#4C72B0', edgecolor='white', alpha=0.85)
axes[2].set_title('Score Distribution (200 Students)', fontsize=13, fontweight='bold')
axes[2].set_xlabel('Score')
axes[2].set_ylabel('Number of Students')
axes[2].axvline(all_scores.mean(), color='red', linestyle='--', linewidth=1.5,
                label=f'Mean: {all_scores.mean():.1f}')
axes[2].legend()

plt.tight_layout()
plt.savefig('07_graphs_story.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ Graph saved as '07_graphs_story.png'")

# ── Data Story ─────────────────────────────────────
print("""
📖 DATA STORY
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. BAR CHART — Computer Science leads with 88 avg,
   while History lags at 65. This suggests students
   are more engaged with tech-related subjects.

2. PIE CHART — Mumbai dominates with 35% of students,
   followed by Delhi (28%). Smaller cities like Pune
   have fewer students, possibly reflecting unequal
   access to resources.

3. HISTOGRAM — Scores follow a roughly normal distribution
   centered around 74. Most students score between 60–90,
   indicating a moderate performance level across the class.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
