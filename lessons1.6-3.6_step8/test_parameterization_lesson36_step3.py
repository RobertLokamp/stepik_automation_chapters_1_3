import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

#создаём тест с параметризацией, передаём в текст линка нужные номера степов
@pytest.mark.parametrize('step_number', [236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905])
def test_ufo_messages(browser, step_number):
    link = f"https://stepik.org/lesson/{step_number}/step/1"
    browser.get(link)

    #ждём пока загрузится страница
    browser.implicitly_wait(10)

    # считаем функцию и переводим результат в строку
    answer = math.log(int(time.time()))
    answer = str(answer)

    # вводим результат в текстовое поле
    text_area = browser.find_element_by_class_name("textarea")
    text_area.send_keys(answer)

    # отправляем результат
    submit_button = browser.find_element_by_class_name("submit-submission")
    submit_button.click()

    # ждём пока загрузится страница
    browser.implicitly_wait(5)

    # проверяем, что сообщение содержит "Correct"
    message = browser.find_element_by_class_name("smart-hints__hint")
    assert "Correct" in message.text