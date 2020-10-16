from selenium import webdriver
import time
import math

def calc(y):
    return str(math.log(abs(12*math.sin(int(x)))))  # функция для расчёта х

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Нажатие на кнопку
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

    # Нажатие на ОК в конфирме
    confirm = browser.switch_to.alert
    confirm.accept()

    # Поиск значения x, его перевод в текст и расчёт функции
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    # Ввод результата расчёта функции в текстовое поле
    input = browser.find_element_by_id('answer')  # Поиск поля ввода результата расчёта
    input.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
