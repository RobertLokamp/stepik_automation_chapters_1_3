from selenium import webdriver
import time

try:
    link = 'http://suninjuly.github.io/selects1.html'
    #link = 'http://suninjuly.github.io/selects2.html' # работает на обеих ссылках
    browser = webdriver.Chrome()
    browser.get(link)

    # Число 1
    num1 = browser.find_element_by_id('num1')
    num1 = num1.text

    # Число 2
    num2 = browser.find_element_by_id('num2')
    num2 = num2.text

    # Сумма чисел
    num = int(num1) + int(num2)  # необходимо перевести в числа для верного сложения
    num = str(num)  # необходимо перевести в строку для поиска по value

    # Выбор элемента из списка
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_value(num)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
