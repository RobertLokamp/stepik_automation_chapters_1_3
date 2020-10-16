from selenium import webdriver
import time
import math

def calc(treasure):
    return str(math.log(abs(12*math.sin(int(treasure)))))  # функция для расчёта х

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)


    treasure = browser.find_element_by_id('treasure')  # поиск сундука
    treasure = treasure.get_attribute('valuex')  # взятие значение х
    x = calc(treasure)  # расчёт х
    textbox = browser.find_element_by_id('answer')  # поиск текстового поля
    textbox.send_keys(x)  # ввод х в поле
    robotCheckbox = browser.find_element_by_id('robotCheckbox')  # поиск чекбокса "I'm the robot"
    robotCheckbox.click()  # активация чекбокса
    robotRadio = browser.find_element_by_id('robotsRule')  # поиск радиобаттона "Robots rule!"
    robotRadio.click()  # активация радиобаттона

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
