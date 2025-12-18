import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("student_performance.csv")

print("Student Data:\n")
print(df)

# Calculate total and average marks
df["Total"] = df["Math"] + df["Science"] + df["English"]
df["Average"] = df["Total"] / 3

# Grade assignment
def grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"

df["Grade"] = df["Average"].apply(grade)

print("\nStudent Performance with Grades:\n")
print(df)

# Class average
print("\nClass Average Marks:")
print(df[["Math", "Science", "English"]].mean())

# Top performer
top_student = df.loc[df["Average"].idxmax()]
print("\nTop Performer:")
print(top_student[["Name", "Average", "Grade"]])

# Visualization: Average Marks
plt.figure()
plt.bar(df["Name"], df["Average"])
plt.title("Average Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Average Marks")
plt.xticks(rotation=45)
plt.show()

# Visualization: Subject-wise comparison
df.plot(x="Name", y=["Math", "Science", "English"], kind="bar")
plt.title("Subject-wise Performance")
plt.ylabel("Marks")
plt.xticks(rotation=45)
plt.show()
