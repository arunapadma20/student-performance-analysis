import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Create average score column
df["average_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)

# Basic statistics
print("\nAverage Score Summary:\n", df["average_score"].describe())

# Distribution plot
sns.histplot(df["average_score"], bins=10, kde=True)
plt.title("Distribution of Average Scores")
plt.show()

# Correlation heatmap (only numeric columns)
numeric_df = df.select_dtypes(include='number')  # Select only numeric columns
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Scores")
plt.show()

# Gender-wise performance
sns.boxplot(x="gender", y="average_score", data=df)
plt.title("Average Score by Gender")
plt.show()

# Test preparation effect
sns.barplot(x="test preparation course", y="average_score", data=df)
plt.title("Effect of Test Preparation on Performance")
plt.show()

