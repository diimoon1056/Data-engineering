!pip install streamz pandas matplotlib

import pandas as pd
file_path = "/content/sample_data/college_comparing_matrix.xlsx"

df = pd.read_excel(file_path, sheet_name="Здобувачі")
df.head()

from streamz.dataframe import DataFrame

sdf = DataFrame(example=df.iloc[:0]) 
for i in range(0, len(df), 100):
    batch = df.iloc[i:i+100]
    sdf.emit(batch)  

df_filtered = df[df['Заклад освіти'] == 'РФКІТ']
df_counts = df.groupby('Заклад освіти').size()
print(df_counts)

df_specialties_counts = df.groupby('Спеціальність').size()

max_specialty = df_specialties_counts.idxmax()
min_specialty = df_specialties_counts.idxmin()
print(f"Спеціальність з найбільшою кількістю здобувачів: {max_specialty}")
print(f"Спеціальність з найменшою кількістю здобувачів: {min_specialty}")

import matplotlib.pyplot as plt

df_specialties_counts.plot(kind='bar', figsize=(10,6))
plt.title("Кількість здобувачів за спеціальностями")
plt.xlabel("Спеціальність")
plt.ylabel("Кількість здобувачів")
plt.show()

df_rfkit = df[df['Заклад освіти'] == '732 Рівненський фаховий коледж інформаційних технологій']
df_rfkit_specialties_counts = df_rfkit.groupby('Спеціальність').size()

df_rfkit_specialties_counts.plot(kind='pie', figsize=(8,8), autopct='%1.1f%%')
plt.title("Розподіл здобувачів за спеціальностями в РФКІТ")
plt.ylabel("")  
plt.show()
