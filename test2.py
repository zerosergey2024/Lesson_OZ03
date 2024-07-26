from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import matplotlib.pyplot as plt


from selenium.webdriver.chrome.service import Service
import time

# Импортируем модуль CSV
import csv

driver = webdriver.Chrome()
# URL страницы
url = 'https://www.divan.ru/category/stoly-i-stulya'

# Открытие страницы
driver.get(url)

time.sleep(5)

# Парсинг цен
#prices = driver.find_elements(By.XPATH, "//span[@data-mark='MainPrice']/span")
prices = driver.find_elements(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH')
#prices = driver.find_elements(By.XPATH, "//span.ui-LD-ZU.Mtl24.pjHOU")
# Открытие CSV файла для записи
with open('prices.csv', mode='w', newline='', encoding='utf-8') as file:
 writer = csv.writer(file)
 writer.writerow(['Price'])  # Записываем заголовок столбца

 # Записываем цены в CSV файл
 for price in prices:
  writer.writerow([price.text])

# Закрытие драйвера
driver.quit()