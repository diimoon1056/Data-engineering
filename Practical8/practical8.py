import pandas as pd
import dask.dataframe as dd
from IPython.display import display
file_path = "/content/sample_data/college_comparing_matrix.xlsx"

open_f = pd.read_excel(file_path, sheet_name=None)

for sheet_name, letter in open_f.items():
  print(f"перші 5 рядків кожкого пркуша '{sheet_name}': ")
  display(letter.head())
  print("-" * 50)

for sheet_name, letter in open_f.items():
  print(f"пропущені значення в аркуші: '{sheet_name}': ")
  display(letter.isnull().sum())
  print("-" * 50)

unique_colleges = set()
for letter in open_f.values():
    if 'Навчальний заклад' in letter.columns:
        unique_colleges.update(df['Навчальний заклад'].dropna().unique())
print(f"Кількість унікальних навчальних закладів: {len(unique_colleges)}")

vstup = open_f.get('Вступ')
vypusk = open_f.get('Випуск')

if vstup is not None and vypusk is not None:
    vstup_summary = vstup.groupby('Заклад освіти')['Вступ'].sum()
    vypusk_summary = vypusk.groupby('Заклад освіти')['Випуск'].sum()

    summary = pd.DataFrame({
        'Вступники': vstup_summary,
        'Випускники': vypusk_summary
    }).fillna(0)

    print("Загальна кількість вступників та випускників по закладах:")
    display(summary)
else:
    print("Аркуші 'Вступ' та 'Випуск' не знайдені.")

vstup = open_f.get('Вступ')
vypusk = open_f.get('Випуск')

if vstup is not None and vypusk is not None:
    vstup_speciality_summary = vstup.groupby('Спеціальність')['Вступ'].sum()
    vypusk_speciality_summary = vypusk.groupby('Спеціальність')['Випуск'].sum()

    speciality_summary = pd.DataFrame({
        'Вступники': vstup_speciality_summary,
        'Випускники': vypusk_speciality_summary
    }).fillna(0) 

    speciality_summary['Загальна кількість'] = speciality_summary['Вступники'] + speciality_summary['Випускники']

    max_speciality = speciality_summary['Загальна кількість'].idxmax()
    max_count = speciality_summary['Загальна кількість'].max()

    print(f"Спеціальність з найбільшою кількістю студентів: {max_speciality}")
    print(f"Загальна кількість студентів: {max_count}")
else:
    print("Аркуші 'Вступ' та 'Випуск' не знайдені.")

import matplotlib.pyplot as plt
vstup = open_f.get('Вступ')
vypusk = open_f.get('Випуск')
pedagogi = open_f.get('Педагоги')

if vstup is not None and vypusk is not None:
    vstup_speciality_summary = vstup.groupby('Спеціальність')['Вступ'].sum()
    vypusk_speciality_summary = vypusk.groupby('Спеціальність')['Випуск'].sum()

    speciality_summary = pd.DataFrame({
        'Вступники': vstup_speciality_summary,
        'Випускники': vypusk_speciality_summary
    }).fillna(0)

    speciality_summary['Загальна кількість'] = speciality_summary['Вступники'] + speciality_summary['Випускники']

    plt.figure(figsize=(10, 6))
    speciality_summary['Загальна кількість'].plot(kind='bar', color='skyblue')
    plt.title('Кількість студентів за спеціальностями')
    plt.xlabel('Спеціальність')
    plt.ylabel('Загальна кількість студентів')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if vstup is not None:
    vstup_yearly = vstup.groupby('Рік')['Вступ'].sum()

    plt.figure(figsize=(10, 6))
    vstup_yearly.plot(kind='line', marker='o', color='green')
    plt.title('Зміни кількості вступників за роками')
    plt.xlabel('Рік')
    plt.ylabel('Кількість вступників')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if pedagogi is not None:
    pedagogi_stage_distribution = pedagogi.groupby('Тип стажу')['Кількість'].sum()

    plt.figure(figsize=(8, 8))
    pedagogi_stage_distribution.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen', 'lightskyblue'])
    plt.title('Розподіл викладачів за типом стажу')
    plt.ylabel('') 
    plt.tight_layout()
    plt.show()
