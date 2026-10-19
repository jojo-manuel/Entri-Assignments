<<<<<<< HEAD
"""
================================================================================
Assignment: Visualization with Seaborn and Matplotlib
Dataset: Titanic dataset (Seaborn / titanic.csv)
================================================================================
Tasks Covered:
1. Countplot: Passenger Count by Embarked Port separated by Sex
2. Swarmplot: Age Distribution across Classes categorized by Sex
3. Pie Chart: Gender Distribution (Matplotlib) with autopct and slice explode
4. Heatmap: Correlation Matrix of numerical features with annotations
5. Violin Plot: Fare by Class and Gender
6. Scatter Plot: Age vs Fare colored by Survival Status (hue='survived')
With short observations and insights explaining each plot.
================================================================================
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual aesthetic theme
sns.set_theme(style="whitegrid", palette="muted")
plt.rcParams.update({'font.sans-serif': 'DejaVu Sans', 'font.size': 11})

# Create output folder for saving generated plots
output_dir = "plots"
os.makedirs(output_dir, exist_ok=True)

# ------------------------------------------------------------------------------
# Load Titanic Dataset
# ------------------------------------------------------------------------------
try:
    if os.path.exists('titanic.csv'):
        titanic = pd.read_csv('titanic.csv')
    else:
        titanic = sns.load_dataset('titanic')
except Exception:
    titanic = sns.load_dataset('titanic')

print("=" * 75)
print(f"Titanic Dataset Loaded Successfully: {titanic.shape[0]} rows x {titanic.shape[1]} columns")
print("=" * 75)


# ==============================================================================
# 1. Countplot: Passenger Count by Embarked Port
# Task: Create a countplot to display the number of passengers who boarded from
#       each port (embarked), separated by sex.
# ==============================================================================
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

# Add direct value annotations on top of each bar
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
plot1_file = os.path.join(output_dir, "1_countplot_embarked_sex.png")
plt.savefig(plot1_file, dpi=300)
# plt.show()
plt.close()

obs1 = (
    "Observation 1 (Countplot - Embarked Port by Sex):\n"
    "- Southampton (S) was the primary embarkation port, accounting for over 72% of all passengers (441 males, 203 females).\n"
    "- Cherbourg (C) saw 168 passengers (95 males, 73 females), showing a relatively balanced gender proportion.\n"
    "- Queenstown (Q) had the lowest overall passenger volume (77 passengers: 41 males, 36 females) with near parity in gender."
)
print("\n" + "=" * 75)
print(obs1)


# ==============================================================================
# 2. Swarmplot: Age Distribution across Classes
# Task: Create a swarmplot to visualize the distribution of age across passenger
#       classes (pclass), categorized by sex.
# ==============================================================================
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
plot2_file = os.path.join(output_dir, "2_swarmplot_age_class_sex.png")
plt.savefig(plot2_file, dpi=300)
# plt.show()
plt.close()

obs2 = (
    "Observation 2 (Swarmplot - Age Distribution across Classes):\n"
    "- 1st Class passengers had an older demographic, primarily spanning between 30 and 60 years, with several passengers over 65.\n"
    "- 2nd Class shows a balanced, uniform age distribution across all age brackets from toddlers up to mature adults.\n"
    "- 3rd Class had the youngest demographic overall, heavily concentrated between ages 18 and 35, along with a distinct cluster of young children.\n"
    "- Male passengers outnumber females substantially in 3rd class, whereas the gender ratio is much more balanced in 1st and 2nd class."
)
print("\n" + "=" * 75)
print(obs2)


# ==============================================================================
# 3. Pie Chart: Gender Distribution (Matplotlib)
# Task: Create a pie chart using Matplotlib to show the percentage of male vs.
#       female passengers. Add percentage labels using autopct. Use explode for
#       one slice to highlight it.
# ==============================================================================
plt.figure(figsize=(7, 7))
gender_counts = titanic['sex'].value_counts()
colors = ['#5dade2', '#f1948a']
explode = (0.08, 0)  # Explode male slice to highlight majority

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
plot3_file = os.path.join(output_dir, "3_pie_chart_gender_distribution.png")
plt.savefig(plot3_file, dpi=300)
# plt.show()
plt.close()

obs3 = (
    "Observation 3 (Pie Chart - Gender Distribution):\n"
    f"- Male passengers formed the majority at {gender_counts['male'] / gender_counts.sum() * 100:.1f}% ({gender_counts['male']} passengers).\n"
    f"- Female passengers accounted for {gender_counts['female'] / gender_counts.sum() * 100:.1f}% ({gender_counts['female']} passengers).\n"
    "- Almost two-thirds of all passengers on board the Titanic were male."
)
print("\n" + "=" * 75)
print(obs3)


# ==============================================================================
# 4. Heatmap: Correlation Matrix
# Task: Create a heatmap to show correlations between age, fare, pclass, sibsp,
#       parch, and survived. (Use seaborn.heatmap with annotations)
# ==============================================================================
plt.figure(figsize=(9, 7))
corr_cols = ['age', 'fare', 'pclass', 'sibsp', 'parch', 'survived']
corr_matrix = titanic[corr_cols].corr()

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
plot4_file = os.path.join(output_dir, "4_heatmap_correlation_matrix.png")
plt.savefig(plot4_file, dpi=300)
# plt.show()
plt.close()

obs4 = (
    "Observation 4 (Heatmap - Correlation Matrix):\n"
    "- Fare and Survived show a positive correlation (+0.26): passengers who purchased higher-priced tickets had noticeably higher survival rates.\n"
    "- Pclass and Fare have a strong negative correlation (-0.55): class 1 tickets were significantly more expensive than class 2 and 3.\n"
    "- Pclass and Survived show a negative correlation (-0.34): 1st class passengers survived at much higher rates than 3rd class passengers.\n"
    "- SibSp and Parch have a moderate positive correlation (+0.41): passengers traveling with siblings/spouses frequently also traveled with parents/children.\n"
    "- Age shows weak negative correlation with Survived (-0.08) and moderate negative correlation with Pclass (-0.37), indicating older individuals tended to travel in higher classes."
)
print("\n" + "=" * 75)
print(obs4)


# ==============================================================================
# 5. Violin Plot: Fare by Class and Gender
# Task: Create a violin plot to visualize fare distribution across classes,
#       separated by gender.
# ==============================================================================
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
plt.ylim(0, 300)  # Focus on the distribution range covering >95% of passengers

plt.tight_layout()
plot5_file = os.path.join(output_dir, "5_violinplot_fare_class_gender.png")
plt.savefig(plot5_file, dpi=300)
# plt.show()
plt.close()

obs5 = (
    "Observation 5 (Violin Plot - Fare by Class and Gender):\n"
    "- 1st class fares display extreme dispersion with a much higher median and long right tail compared to 2nd and 3rd class.\n"
    "- Within 1st class, females had a notably higher median and upper quartile fare distribution than males.\n"
    "- 2nd and 3rd class fare distributions are tightly condensed below $50, with virtually no difference between male and female fare distributions."
)
print("\n" + "=" * 75)
print(obs5)


# ==============================================================================
# 6. Scatter Plot: Age vs Fare
# Task: Create a scatter plot to explore the relationship between age and fare,
#       colored by survival status. Use a seaborn scatterplot with hue='survived'.
#       Include titles, labels, and legends where needed.
# ==============================================================================
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

# Format legend labels cleanly
handles, _ = ax6.get_legend_handles_labels()
plt.legend(handles=handles, labels=['Victim (0)', 'Survivor (1)'], title='Survival Status', title_fontsize='11', loc='upper right')
plt.ylim(0, 300)

plt.tight_layout()
plot6_file = os.path.join(output_dir, "6_scatterplot_age_fare_survived.png")
plt.savefig(plot6_file, dpi=300)
# plt.show()
plt.close()

obs6 = (
    "Observation 6 (Scatter Plot - Age vs Fare by Survival Status):\n"
    "- Most fatalities (red circles) cluster in the low-fare region (below $50), especially among adult passengers aged 18-50.\n"
    "- High-fare passengers (above $100) had an overwhelmingly high survival rate (green markers), corroborating class privilege during evacuation.\n"
    "- Young children (under age 10) had very high survival rates across various fare levels, reflecting the 'women and children first' maritime protocol."
)
print("\n" + "=" * 75)
print(obs6)

print("\n" + "=" * 75)
print("All 6 visualization tasks completed successfully!")
print(f"High-resolution figures saved to: '{os.path.abspath(output_dir)}'")
print("=" * 75)
=======
import numpy as np
import pandas as pd

# ==========================================
# Question 1: Reshape 1D array to 2x5 Matrix
# ==========================================
# Create a numpy array containing numbers from 1 to 10
arr1 = np.arange(1, 11)
matrix1 = arr1.reshape(2, 5)

print("=== QUESTION 1 ===")
print("Original 1D Array:")
print(arr1)
print("\nReshaped 2x5 Matrix:")
print(matrix1)
print("\n" + "="*40 + "\n")


# ==========================================
# Question 2: Extract elements by index range
# ==========================================
# Create a numpy array containing numbers from 1 to 20
arr2 = np.arange(1, 21)

# Extract elements between 5th and 15th index (indices 5 to 14)
extracted = arr2[5:15]

print("=== QUESTION 2 ===")
print("Original Array (1 to 20):")
print(arr2)
print("\nExtracted elements (from index 5 to 15):")
print(extracted)
print("\n" + "="*40 + "\n")


# ==========================================
# Question 3: Compute Mean, Median, and Standard Deviation
# ==========================================
print("=== QUESTION 3 ===")
# Computing statistics for the extracted array from Q2
mean_val = np.mean(extracted)
median_val = np.median(extracted)
std_val = np.std(extracted)

print("For the Extracted Array from Q2:")
print(f"Mean: {mean_val}")
print(f"Median: {median_val}")
print(f"Standard Deviation: {std_val:.4f}")

# Computing statistics for the full Q2 array (1 to 20)
print("\nFor the Full Array (1 to 20):")
print(f"Mean: {np.mean(arr2)}")
print(f"Median: {np.median(arr2)}")
print(f"Standard Deviation: {np.std(arr2):.4f}")
print("\n" + "="*40 + "\n")


# ==========================================
# Question 4: Subtract 1D array from 2D array using Broadcasting
# ==========================================
x = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
y = np.array([1, 2, 3, 4])

# Subtracting y from each row of x using broadcasting
result = x - y

print("=== QUESTION 4 ===")
print("2D Array x (shape 3x4):")
print(x)
print("\n1D Array y (shape 4,):")
print(y)
print("\nResult of (x - y) via Broadcasting:")
print(result)
print("\n" + "="*40 + "\n")


# ==========================================
# Question 5: Pandas DataFrame Operations
# ==========================================
# Base DataFrame with 10 rows: name, age, gender
data = {
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack'],
    'age': [25, 32, 28, 45, 29, 35, 40, 24, 38, 27],
    'gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male', 'Female', 'Female', 'Male', 'Male']
}
df = pd.DataFrame(data)

print("=== QUESTION 5 (Initial DataFrame) ===")
print(df)

# 1) Add 'occupation' column
occupations = ['Programmer', 'Manager', 'Analyst', 'Programmer', 'Manager', 'Analyst', 'Programmer', 'Manager', 'Analyst', 'Programmer']
df['occupation'] = occupations

print("\n=== QUESTION 5.1 (Added Occupation Column) ===")
print(df)

# 2) Select rows where age >= 30
df_age_30 = df[df['age'] >= 30]

print("\n=== QUESTION 5.2 (Rows where age >= 30) ===")
print(df_age_30)

# 3) Convert to CSV, read CSV, display contents
csv_filename = "people_data.csv"
df.to_csv(csv_filename, index=False)
print(f"\nDataFrame successfully saved to '{csv_filename}'.")

# Reading the CSV file back into pandas
df_read = pd.read_csv(csv_filename)

print("\n=== QUESTION 5.3 (DataFrame Read from CSV File) ===")
print(df_read)
>>>>>>> 58f3836c901929e1ae2dd3abde8ac2fde10b9ed0
