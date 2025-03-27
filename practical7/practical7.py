!pip install dask

import dask.dataframe as dd
import dask.array as da
from dask.delayed import delayed
from dask.distributed import Client
import time
client = Client()
client

!pip install pandas openpyxl

import pandas as pd
import dask.dataframe as dd
file_path = "/content/sample_data/college_comparing_matrix.xlsx"

df = pd.read_excel(file_path, sheet_name="Вступ")

ddf = dd.from_pandas(df, npartitions=1)
print(ddf.head())
print(ddf.info())

print(f"Кількість записів: {len(df)}")

number_specialties = df['Спеціальність'].nunique().compute()
print(f"Кількість спеціальностей: {number_specialties}")

stats = ddf['Вступ'].describe().compute()
print(stats)

grouped = ddf.groupby('Спеціальність')['Вступ'].sum().compute()
print(grouped)

top_specialties = grouped.sort_values(ascending=False).head(10)
print("Топ-10 спеціальностей за кількістю вступників:")
print(top_specialties)

from dask import delayed

@delayed
def compute_mean(df, column):
    return df[column].mean()

mean_value = compute_mean(df, 'Вступ')
print(f"Середнє значення вступників: {mean_value.compute()}")

from dask.distributed import Client

client = Client()
print(client)


result = ddf.groupby('Спеціальність')['Вступ'].sum().compute()
print(result)
