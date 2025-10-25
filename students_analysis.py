import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("StudentsPerformance.csv")
print("First 5 Rows:")
print(df.head())
df["average_score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)
print("\nAverage Score Summary:\n", df["average_score"].describe())
sns.histplot(df["average_score"], bins=10, kde=True)
plt.title("Distribution of Average Scores")
plt.show()
numeric_df = df.select_dtypes(include='number')  # Select only numeric columns
sns.heatmap(numeric_df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap of Scores")
plt.show()
sns.boxplot(x="gender", y="average_score", data=df)
plt.title("Average Score by Gender")
plt.show()
sns.barplot(x="test preparation course", y="average_score", data=df)
plt.title("Effect of Test Preparation on Performance")
plt.show()


