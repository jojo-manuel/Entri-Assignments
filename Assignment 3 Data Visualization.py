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
