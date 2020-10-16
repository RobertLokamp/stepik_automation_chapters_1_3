from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(y):
    return str(math.log(abs(12*math.sin(int(x)))))  # функция для расчёта х

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    button = browser.find_element_by_id("book")
    # говорим Selenium ждать в течение 12 секунд, пока цена не будет 100$
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button.click()

# Поиск значения x, его перевод в текст и расчёт функции
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    # Ввод результата расчёта функции в текстовое поле
    input = browser.find_element_by_id('answer')  # Поиск поля ввода результата расчёта
    input.send_keys(y)

    # Отправляем заполненную форму
    solve_button = browser.find_element_by_id('solve')
    solve_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
