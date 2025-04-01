import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
y = x**2
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='y = x^2', color='b')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Лінійний графік: y = x^2')
plt.grid(True)
plt.legend()
plt.show()

groups = ['ІПЗ-1/1', 'ІПЗ-2/1', 'ІПЗ-3/1', 'ІПЗ-4/1']
students = [23, 45, 12, 30]
plt.figure(figsize=(8, 5))
plt.bar(groups, students, color=['r', 'g', 'b', 'c'])
plt.xlabel('Групи')
plt.ylabel('Кількість студентів')
plt.title('Кількість студентів у групах')
for i, v in enumerate(students):
    plt.text(i, v + 1, str(v), ha='center')
plt.show()

categories = ['Апельсини', 'Яблука', 'Банани', 'Виноград']
percentages = [25, 30, 20, 25]
plt.figure(figsize=(6, 6))
plt.pie(percentages, labels=categories, autopct='%1.1f%%', colors=['orange', 'green', 'yellow', 'purple'])
plt.title('Розподіл фруктів')
plt.show()

np.random.seed(0)
x = np.random.rand(50) * 10
y = np.random.rand(50) * 10
sizes = np.random.rand(50) * 300
colors = np.random.rand(50)
plt.figure(figsize=(8, 5))
plt.scatter(x, y, s=sizes, c=colors, cmap='viridis', alpha=0.7, edgecolors='k')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Діаграма розсіювання')
plt.colorbar(label='Колір')
plt.show()
