import pandas as pd
df = pd.read_csv(r"/content/StudentPerformanceFactors.csv")

#no of rows and columns in data
df.shape

# Remove unnecessary columns for analysis and insights
# Use errors='ignore' to prevent error if column not found (use with caution)
df.drop(columns=[
    'Distance_from_Home',
    'Gender',
    'Internet_Access',
    'Learning_Disabilities'
], inplace=True, errors='ignore')

#Value Count in column
# Example: Distribution of Parental Education Level
print(df['School_Type'].value_counts())

#Display columns
print(df.columns)

#information about data
df.info()

# Statistical Information of data
df.describe()

# Check for null values in each column
print(df.isnull().sum())

# Fill missing values in specific categorical columns with their mode
df['Teacher_Quality'].fillna(df['Teacher_Quality'].mode()[0], inplace=True)
df['Parental_Education_Level'].fillna(df['Parental_Education_Level'].mode()[0], inplace=True)

# Check number of duplicate rows
print(df.duplicated().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Confirm removal
print("Duplicate rows after removal:", df.duplicated().sum())

#first 5 rows of column
df.head()

#last 5 rows of column
df.tail()

"""Data Visualization to draw meaningful insights"""

import matplotlib.pyplot as plt

# 1. Bar Chart: Average Exam Score by Parental Education Level
plt.figure()
df.groupby('Parental_Education_Level')['Exam_Score'].mean().plot(kind='bar', color='coral')
plt.title('Avg Exam Score by Parental Education Level')
plt.xlabel('Parental Education Level')
plt.ylabel('Average Exam Score')
plt.tight_layout()

"""Bar Chart – Avg Exam Score by Parental Education Level

Insight: Students whose parents have higher education levels tend to perform better.
"""

# 2. Bar Chart: Average Exam Score by Teacher Quality
plt.figure()
df.groupby('Teacher_Quality')['Exam_Score'].mean().plot(kind='bar', color='skyblue')
plt.title('Avg Exam Score by Teacher Quality')
plt.xlabel('Teacher Quality')
plt.ylabel('Average Exam Score')
plt.tight_layout()

"""Bar Chart – Avg Exam Score by Teacher Quality

Insight: Higher teacher quality is positively associated with better exam performance.
"""

# 3. Scatter Plot: Sleep Hours vs Exam Score
plt.figure()
plt.scatter(df['Sleep_Hours'], df['Exam_Score'], color='mediumslateblue')
plt.title('Sleep Hours vs Exam Score')
plt.xlabel('Sleep Hours')
plt.ylabel('Exam Score')

"""Scatter Plot – Sleep Hours vs Exam Score

Insight: There may be a mild positive trend up to a point—students who get adequate sleep tend to perform better, but too much or too little sleep shows reduced performance.
"""

# 4. Scatter Plot: Family Income vs Exam Score
plt.figure()
plt.scatter(df['Family_Income'], df['Exam_Score'], color='darkorange')
plt.title('Family Income vs Exam Score')
plt.xlabel('Family Income')
plt.ylabel('Exam Score')

"""Scatter Plot – Family Income vs Exam Score

Insight: A weak positive correlation may exist—higher-income families are slightly associated with better scores.
"""

import matplotlib.pyplot as plt
import numpy as np

# Select only numeric columns
numeric_df = df.select_dtypes(include=[np.number])

# Calculate correlation matrix
correlation_matrix = numeric_df.corr()

# Get top 5 features most correlated with Exam_Score
top_features = correlation_matrix['Exam_Score'].abs().sort_values(ascending=False)[1:6].index.tolist()
top_features.append('Exam_Score')

# Extract correlation matrix for selected features
focused_corr = numeric_df[top_features].corr()

# Plot the heatmap using matplotlib
plt.figure(figsize=(8, 6))
im = plt.imshow(focused_corr, cmap='coolwarm', interpolation='none')
plt.colorbar(im, label='Correlation Coefficient')
plt.xticks(ticks=np.arange(len(focused_corr.columns)), labels=focused_corr.columns, rotation=45)
plt.yticks(ticks=np.arange(len(focused_corr.index)), labels=focused_corr.index)
plt.title('Top Correlated Features with Exam Score')
plt.tight_layout()
plt.show()

"""The most impactful factors on exam scores are past performance, study hours, and attendance — confirming that consistent habits and discipline are the strongest predictors of academic success."""

# 8. Line Chart: Exam Score vs Previous Scores
plt.figure()
df_sorted = df.sort_values('Previous_Scores')
plt.plot(df_sorted['Previous_Scores'], df_sorted['Exam_Score'], color='green')
plt.title('Exam Score Trend by Previous Scores')
plt.xlabel('Previous Scores')
plt.ylabel('Exam Score')

"""Line Chart – Exam Score Trend by Previous Scores

Insight: A clear upward trend indicates students who performed well previously continue to do so.
"""

# 9. Pie Chart: Tutoring Sessions Distribution
plt.figure()
counts = df['Tutoring_Sessions'].value_counts()
plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=90)
plt.title('Tutoring Sessions Distribution')

"""Pie Chart – Tutoring Sessions Distribution

Insight: A majority of students may fall into a few tutoring categories (e.g., 0–2 sessions), and fewer students have high tutoring engagement.
"""

# 10. Histogram: Hours Studied
plt.figure()
plt.hist(df['Hours_Studied'], bins=10, color='purple', edgecolor='black')
plt.title('Distribution of Hours Studied')
plt.xlabel('Hours Studied')
plt.ylabel('Frequency')

"""Histogram – Hours Studied

Insight: Most students cluster around a moderate number of study hours (e.g., 2–4), while fewer study for extreme durations.
"""

# 11. Histogram: Attendance
plt.figure()
plt.hist(df['Attendance'], bins=10, color='orange', edgecolor='black')
plt.title('Distribution of Attendance')
plt.xlabel('Attendance')
plt.ylabel('Frequency')

"""Histogram – Attendance

Insight: Students with higher attendance are more frequent, but there's some dropout toward lower ranges.
"""

















from google.colab import files
import pandas as pd

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))

# Assuming the uploaded file is 'StudentPerformanceFactors.csv'
df = pd.read_csv('StudentPerformanceFactors.csv')
display(df.head())