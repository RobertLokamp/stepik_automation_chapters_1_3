from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Код скрипта
    x_element = browser.find_element_by_id('input_value')   # Поиск значения x
    x = x_element.text
    y = calc(x)   # Расчёт значения функции исходя из значения x
    input1 = browser.find_element_by_id('answer')   # Поиск поля ввода результата расчёта
    input1.send_keys(y)
    option1 = browser.find_element_by_id('robotCheckbox')   # Поиск чекбокса "I'm the robot"
    option1.click()
    option2 = browser.find_element_by_id('robotsRule')   # Поиск радиобаттона "Robots rule!"
    option2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # не забываем оставить пустую строку в конце файла
