import pandas as pd

file_path = '/content/sample_data/education_career_success.csv'
df = pd.read_csv(file_path)

df.info()
df.isnull().sum()
df.describe()

import seaborn as sns
import matplotlib.pyplot as plt

sns.histplot(df["High_School_GPA"], bins=20, kde=True)
plt.title('Distribution of High School GPA')
plt.show()

sns.histplot(df["University_GPA"], bins=20, kde=True)
plt.title('Distribution of University GPA')
plt.show()

sns.histplot(df["Starting_Salary"], bins=20, kde=True)
plt.title('Distribution of Starting Salary')
plt.show()

sns.histplot(df["Career_Satisfaction"], bins=20, kde=True)
plt.title('Distribution of Career Satisfaction')
plt.show()

sns.scatterplot(x=df["University_Ranking"], y=df["Starting_Salary"])
plt.title('University Ranking vs Starting Salary')
plt.show()

sns.boxplot(x=df["Field_of_Study"], y=df["Starting_Salary"])
plt.title('Starting Salary by Field of Study')
plt.xticks(rotation=45)
plt.show()

import seaborn as sns
import matplotlib.pyplot as plt

numeric_df = df.select_dtypes(include=['float64', 'int64'])

correlation_matrix = numeric_df.corr()

correlation_with_salary = correlation_matrix["Starting_Salary"].sort_values(ascending=False)
print(correlation_with_salary)

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

sns.boxplot(x=df["Soft_Skills_Score"], y=df["Job_Offers"])
plt.title('Job Offers by Soft Skills Score')
plt.show()

sns.regplot(x=df["Networking_Score"], y=df["Job_Offers"])
plt.title('Networking Score vs Job Offers')
plt.show()

sns.violinplot(x=df["Field_of_Study"], y=df["Career_Satisfaction"])
plt.title('Career Satisfaction by Field of Study')
plt.xticks(rotation=45)
plt.show()

sns.barplot(x=df["Years_to_Promotion"], y=df["Soft_Skills_Score"])
plt.title('Soft Skills Score vs Years to Promotion')
plt.show()
