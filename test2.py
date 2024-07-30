import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0  # Среднее значение
std_dev = 1  # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.figure(figsize=(10, 5))
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Гистограмма для данных, распределенных по нормальному закону')
plt.xlabel('Значение')
plt.ylabel('Частота')
plt.grid(True)
plt.show()

# Генерация двух наборов случайных чисел для диаграммы рассеяния
x = np.random.rand(100)  # массив из 100 случайных чисел для оси X
y = np.random.rand(100)  # массив из 100 случайных чисел для оси Y

# Построение диаграммы рассеяния
plt.figure(figsize=(10, 5))
plt.scatter(x, y, alpha=0.7, color='red', edgecolor='black')
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()