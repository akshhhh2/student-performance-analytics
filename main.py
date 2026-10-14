import pandas as pd
import numpy as np

# Load student dataset
df = pd.read_csv("students.csv")

# Subjects included in the analysis
subjects = ["Maths", "Python", "Statistics"]

# Function to calculate total marks
def calculate_total(row):
    return row[subjects].sum()

# Function to calculate average marks
def calculate_average(row):
    return row[subjects].mean()

# Function to assign grades
def calculate_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

# Calculate total and average
df["Total"] = df.apply(calculate_total, axis=1)
df["Average"] = df.apply(calculate_average, axis=1)

# Assign grades using a loop
grades = []
for avg in df["Average"]:
    grades.append(calculate_grade(avg))

df["Grade"] = grades

# Pass or fail: at least 40 in every subject
df["Result"] = np.where(
    (df[subjects] >= 40).all(axis=1),
    "Pass",
    "Fail"
)

# Display student results
print("\n===== STUDENT PERFORMANCE ANALYTICS =====")
print(df.to_string(index=False))

# Overall statistics
print("\n===== CLASS SUMMARY =====")
print("Total Students:", len(df))
print("Class Average:", round(df["Average"].mean(), 2))
print("Highest Average:", round(df["Average"].max(), 2))
print("Lowest Average:", round(df["Average"].min(), 2))
print("Students Passed:", (df["Result"] == "Pass").sum())
print("Students Failed:", (df["Result"] == "Fail").sum())

# Subject-wise analysis
print("\n===== SUBJECT-WISE AVERAGE =====")
for subject in subjects:
    print(subject, ":", round(np.mean(df[subject]), 2))

# Top-performing students
print("\n===== TOP PERFORMERS =====")
top_students = df.nlargest(3, "Average")
print(top_students[["Name", "Average", "Grade"]].to_string(index=False))
