from selenium import webdriver
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    firstname = browser.find_element_by_name('firstname')
    firstname.send_keys('Ivan')
    lastname = browser.find_element_by_name('lastname')
    lastname.send_keys('Petrov')
    email = browser.find_element_by_name('email')
    email.send_keys('ivanpetrov@stepik.ru')

    file = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'l2.2_s8_test.txt')  # добавляем к этому пути имя файла
    file.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
