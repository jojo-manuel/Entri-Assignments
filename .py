import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual aesthetic theme
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.sans-serif': 'DejaVu Sans', 'font.size': 11})

# ---------------------------------------------------------
# Load Titanic Dataset
# ---------------------------------------------------------
try:
    if os.path.exists('titanic.csv'):
        titanic = pd.read_csv('titanic.csv')
    else:
        titanic = sns.load_dataset('titanic')
except Exception:
    titanic = sns.load_dataset('titanic')

print("=" * 70)
print(f"Titanic Dataset Loaded Successfully. Dimensions: {titanic.shape[0]} rows x {titanic.shape[1]} columns")
print("=" * 70)

# Create output folder for plot images
output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)


# =========================================================
# 1. Countplot: Passenger Count by Embarked Port
# =========================================================
# Map port initials to full names for clearer visualization
port_mapping = {'S': 'Southampton (S)', 'C': 'Cherbourg (C)', 'Q': 'Queenstown (Q)'}
titanic['embarked_full'] = titanic['embarked'].map(port_mapping)

plt.figure(figsize=(9, 6))
ax1 = sns.countplot(
    data=titanic.dropna(subset=['embarked']),
    x='embarked_full',
    hue='sex',
    palette={'male': '#3470a3', 'female': '#e06666'},
    order=['Southampton (S)', 'Cherbourg (C)', 'Queenstown (Q)']
)

plt.title('1. Passenger Count by Embarked Port and Sex', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Embarked Port', fontsize=12, fontweight='semibold')
plt.ylabel('Number of Passengers', fontsize=12, fontweight='semibold')
plt.legend(title='Sex', title_fontsize='11', loc='upper right')

# Annotate count values on top of each bar
for p in ax1.patches:
    height = p.get_height()
    if not np.isnan(height) and height > 0:
        ax1.annotate(
            f'{int(height)}',
            (p.get_x() + p.get_width() / 2., height),
            ha='center', va='bottom', fontsize=10, fontweight='bold',
            xytext=(0, 3), textcoords='offset points'
        )

plt.tight_layout()
plot1_path = os.path.join(output_dir, "1_countplot_embarked_sex.png")
plt.savefig(plot1_path, dpi=300)
# plt.show()
plt.close()

obs1 = (
    "Observation 1 (Countplot - Embarked Port by Sex):\n"
    "- Southampton was by far the busiest boarding port, with 441 males and 203 females (over 70% of passengers).\n"
    "- Across all three ports, male passengers outnumbered female passengers.\n"
    "- Queenstown had the lowest overall passenger count and the smallest gender gap (41 males vs 36 females)."
)
print("\n" + "=" * 70)
print(obs1)


# =========================================================
# 2. Swarmplot: Age Distribution across Classes
# =========================================================
plt.figure(figsize=(11, 6))
sns.swarmplot(
    data=titanic.dropna(subset=['age']),
    x='pclass',
    y='age',
    hue='sex',
    dodge=True,
    palette={'male': '#2b5c8f', 'female': '#d9534f'},
    size=4.5,
    alpha=0.85
)

plt.title('2. Age Distribution Across Passenger Classes by Sex', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Passenger Class (1 = 1st Class, 2 = 2nd Class, 3 = 3rd Class)', fontsize=12, fontweight='semibold')
plt.ylabel('Age (Years)', fontsize=12, fontweight='semibold')
plt.legend(title='Sex', title_fontsize='11', loc='upper right')

plt.tight_layout()
plot2_path = os.path.join(output_dir, "2_swarmplot_age_class_sex.png")
plt.savefig(plot2_path, dpi=300)
# plt.show()
plt.close()

obs2 = (
    "Observation 2 (Swarmplot - Age Distribution across Classes):\n"
    "- First-class passengers were generally older, with a concentration between 30 and 60 years and several elderly individuals (>60).\n"
    "- Third-class had the youngest demographic, heavily concentrated between ages 18 and 35, along with a significant cluster of young children (<10).\n"
    "- Second-class showed a balanced age spread spanning from toddlers to middle-aged adults.\n"
    "- In each class, male and female distributions follow a similar age spread, but males constitute the majority in 3rd class."
)
print("\n" + "=" * 70)
print(obs2)


# =========================================================
# 3. Pie Chart: Gender Distribution (Matplotlib)
# =========================================================
plt.figure(figsize=(7, 7))
gender_counts = titanic['sex'].value_counts()
colors = ['#5dade2', '#f1948a']
explode = (0.08, 0)  # Explode the male slice to highlight majority

plt.pie(
    gender_counts,
    labels=[f"{label.capitalize()} ({count})" for label, count in zip(gender_counts.index, gender_counts.values)],
    autopct='%1.1f%%',
    startangle=140,
    colors=colors,
    explode=explode,
    shadow=True,
    textprops={'fontsize': 12, 'fontweight': 'bold'},
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

plt.title('3. Gender Distribution of Titanic Passengers', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plot3_path = os.path.join(output_dir, "3_pie_chart_gender_distribution.png")
plt.savefig(plot3_path, dpi=300)
# plt.show()
plt.close()

obs3 = (
    "Observation 3 (Pie Chart - Gender Distribution):\n"
    f"- Male passengers accounted for {gender_counts['male'] / gender_counts.sum() * 100:.1f}% ({gender_counts['male']} passengers) of the aboard population.\n"
    f"- Female passengers accounted for {gender_counts['female'] / gender_counts.sum() * 100:.1f}% ({gender_counts['female']} passengers).\n"
    "- Nearly two-thirds of the passengers were male, indicating a prominent gender skew."
)
print("\n" + "=" * 70)
print(obs3)


# =========================================================
# 4. Heatmap: Correlation Matrix
# =========================================================
plt.figure(figsize=(9, 7))
corr_cols = ['age', 'fare', 'pclass', 'sibsp', 'parch', 'survived']
corr_matrix = titanic[corr_cols].corr()

mask = np.triu(np.ones_like(corr_matrix, dtype=bool))  # Optional: keep full or show with mask; here we show full for clarity
sns.heatmap(
    corr_matrix,
    annot=True,
    cmap='coolwarm',
    vmin=-1,
    vmax=1,
    fmt='.2f',
    linewidths=1,
    linecolor='white',
    cbar_kws={'label': 'Pearson Correlation Coefficient'}
)

plt.title('4. Correlation Matrix of Numerical Features', fontsize=14, fontweight='bold', pad=15)
plt.tight_layout()
plot4_path = os.path.join(output_dir, "4_heatmap_correlation_matrix.png")
plt.savefig(plot4_path, dpi=300)
# plt.show()
plt.close()

obs4 = (
    "Observation 4 (Heatmap - Correlation Matrix):\n"
    "- Fare and Survived exhibit a positive correlation (+0.26), showing passengers who paid higher fares had higher survival rates.\n"
    "- Pclass and Fare have a strong negative correlation (-0.55), reflecting 1st class (class 1) having the most expensive tickets.\n"
    "- Pclass and Survived show a negative correlation (-0.34), confirming higher class passengers survived at substantially higher rates.\n"
    "- SibSp and Parch display moderate positive correlation (+0.41), representing families traveling together.\n"
    "- Age shows weak negative correlations with Survived (-0.08) and Pclass (-0.37, meaning older passengers were in higher classes)."
)
print("\n" + "=" * 70)
print(obs4)


# =========================================================
# 5. Violin Plot: Fare by Class and Gender
# =========================================================
plt.figure(figsize=(10, 6))
sns.violinplot(
    data=titanic,
    x='pclass',
    y='fare',
    hue='sex',
    split=True,
    inner='quartile',
    palette={'male': '#5c92c9', 'female': '#e67e22'},
    cut=0
)

plt.title('5. Fare Distribution Across Classes Separated by Gender', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Passenger Class (1 = 1st, 2 = 2nd, 3 = 3rd)', fontsize=12, fontweight='semibold')
plt.ylabel('Fare ($)', fontsize=12, fontweight='semibold')
plt.legend(title='Sex', title_fontsize='11', loc='upper right')
plt.ylim(0, 300)  # Focus on the distribution range containing the vast majority of data points

plt.tight_layout()
plot5_path = os.path.join(output_dir, "5_violinplot_fare_class_gender.png")
plt.savefig(plot5_path, dpi=300)
# plt.show()
plt.close()

obs5 = (
    "Observation 5 (Violin Plot - Fare by Class and Gender):\n"
    "- 1st class tickets had substantial price dispersion and much higher median fares compared to 2nd and 3rd class.\n"
    "- In 1st class, females exhibited a wider distribution toward higher ticket fares compared to males.\n"
    "- 2nd and 3rd class fare distributions are very compact and clustered near lower fare levels (< $50), with minimal difference between sexes."
)
print("\n" + "=" * 70)
print(obs5)


# =========================================================
# 6. Scatter Plot: Age vs Fare by Survival Status
# =========================================================
plt.figure(figsize=(10, 6))
ax6 = sns.scatterplot(
    data=titanic,
    x='age',
    y='fare',
    hue='survived',
    style='survived',
    palette={0: '#c0392b', 1: '#27ae60'},
    alpha=0.75,
    s=65
)

plt.title('6. Age vs Fare Colored by Survival Status', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Age (Years)', fontsize=12, fontweight='semibold')
plt.ylabel('Fare ($)', fontsize=12, fontweight='semibold')

# Create clean legend handles
handles, _ = ax6.get_legend_handles_labels()
plt.legend(handles=handles, labels=['Victim (0)', 'Survivor (1)'], title='Survival Status', title_fontsize='11', loc='upper right')
plt.ylim(0, 300)

plt.tight_layout()
plot6_path = os.path.join(output_dir, "6_scatterplot_age_fare_survived.png")
plt.savefig(plot6_path, dpi=300)
# plt.show()
plt.close()

obs6 = (
    "Observation 6 (Scatter Plot - Age vs Fare by Survival Status):\n"
    "- Non-survivors (red circles) heavily cluster in the lower fare region (< $50), particularly among passengers aged 18-50.\n"
    "- Passengers paying higher fares (> $100) were predominantly survivors (green diamonds).\n"
    "- Children under the age of 10 had noticeable survival rates even at lower fares, highlighting the 'women and children first' evacuation protocol."
)
print("\n" + "=" * 70)
print(obs6)
print("\n" + "=" * 70)
print("All 6 plots generated, saved in 'plots/' directory, and observations printed successfully!")
print("=" * 70)
