import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt



# Инициализируем браузер
driver = webdriver.Chrome()

# Указываем сайт
url = 'https://www.divan.ru/category/stoly-i-stulya'

# Открываем веб-страницу
driver.get(url)

# Задаём время ожидания
time.sleep(3)

# Находим все карточки с названиями по классу
stolies = driver.find_elements(By.CLASS_NAME, 'WdR1o')

# Создаём список для хранения данных
parsed_data = []

# Перебираем коллекцию столов
for stoly in stolies:
    try:
        # Находим элементы внутри карточек

        price = stoly.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    # Вносим информацию в список
    parsed_data.append([price])

# Закрываем браузер
driver.quit()

# Записываем данные в CSV файл
with open("stol.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow([ 'Цена изделия'])
    writer.writerows(parsed_data)

# Чтение данных из CSV файла и преобразование цен в числа
prices = []
with open("stol.csv", 'r', newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Пропускаем заголовок
    for row in reader:
        price_str = row[0].replace('руб.', '').replace(' ', '')
        # Преобразование строки в число
        try:
            price_num = int(price_str)
            prices.append(price_num)
        except ValueError:
            print(f"Ошибка преобразования цены: {price_str}")

# Построение гистограммы
plt.hist(prices, bins=20, edgecolor='black')
plt.title('Гистограмма цен на столы и стулья')
plt.xlabel('Цена (рубли)')
plt.ylabel('Количество')
plt.grid(True)
plt.show()

