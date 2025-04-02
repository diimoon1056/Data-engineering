import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

x = np.linspace(-10, 10, 100)
y = x**3 - 5*x
df = pd.DataFrame({'X': x, 'Y': y})
fig = px.line(df, x='X', y='Y', title='Інтерактивний графік y = x^3 - 5x')
fig.show()

regions = ['Північ', 'Південь', 'Схід', 'Захід']
sales = [120, 150, 100, 130]
df_bar = pd.DataFrame({'Регіон': regions, 'Продажі': sales})
fig = px.bar(df_bar, x='Регіон', y='Продажі', text='Продажі', title='Кількість продажів у регіонах')
fig.update_traces(textposition='outside')
fig.show()

categories = ['Апельсини', 'Яблука', 'Банани', 'Виноград']
percentages = [25, 30, 20, 25]
df_pie = pd.DataFrame({'Фрукт': categories, 'Відсоток': percentages})
fig = px.pie(df_pie, names='Фрукт', values='Відсоток', title='Розподіл фруктів', hover_data=['Відсоток'], labels={'Відсоток': 'Частка'})
fig.show()

np.random.seed(42)
categories = ['Електроніка', 'Одяг', 'Іграшки', 'Книги']
data = pd.DataFrame({
    'Ціна': np.random.randint(5, 100, 100),
    'Продажі': np.random.randint(20, 500, 100),
    'Категорія': np.random.choice(categories, 100)
})
fig = px.scatter(data, x='Ціна', y='Продажі', color='Категорія', size='Продажі', title='Аналіз взаємозв’язку між Ціна та Продажі')
fig.show()

years = list(range(2013, 2023))
data_anim = pd.DataFrame({
    'Рік': np.repeat(years, 4),
    'Регіон': ['Північ', 'Південь', 'Схід', 'Захід'] * 10,
    'Продажі': np.random.randint(50, 200, 40)
})
fig = px.bar(data_anim, x='Регіон', y='Продажі', animation_frame='Рік', color='Регіон', title='Динаміка продажів у регіонах')
fig.show()
