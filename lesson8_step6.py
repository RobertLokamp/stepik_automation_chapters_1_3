from selenium import webdriver
import time
import math

def calc(y):
    return str(math.log(abs(12*math.sin(int(x)))))  # функция для расчёта х

try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Поиск значения x, его перевод в текст и расчёт функции
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    # Ввод результата расчёта функции в текстовое поле
    input1 = browser.find_element_by_id('answer')  # Поиск поля ввода результата расчёта
    browser.execute_script("return arguments[0].scrollIntoView(true);", input1)   # Подскрол до инпута
    input1.send_keys(y)

    option1 = browser.find_element_by_id('robotCheckbox')  # Поиск чекбокса "I'm the robot"
    option1.click()
    option2 = browser.find_element_by_id('robotsRule')  # Поиск радиобаттона "Robots rule!"
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
