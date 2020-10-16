# stepik_automation
tasks from the course on automation testing https://stepik.org/course/575/


###Полезные ссылки


####Общее

[Установка Python, Selenium и WebDriver](https://stepik.org/lesson/25969/step/1)
<https://selenium-python.com/>
<http://selenium-python.readthedocs.io>
<http://chromedriver.chromium.org/getting-started>
[Туториал на английском, ориентирован на Java.](https://www.guru99.com/selenium-tutorial.html)
[Можно попробовать писать автотесты для демо-сайта банка. Тоже Java.](https://www.guru99.com/live-selenium-project.html)
[что такое хорошие селекторы](http://barancev.github.io/good-locators/)
[что за PATH переменная? ](http://barancev.github.io/what-is-path-env-var/)
[1.4 Поиск элементов](https://stepik.org/lesson/102555/step/1?unit=196193)
[2. Полезные методы Selenium](https://stepik.org/lesson/165493/step/1?unit=140087)


####Ожидания в Selenium WebDriver

<https://docs.seleniumhq.org/docs/04_webdriver_advanced.jsp>
<https://selenium-python.readthedocs.io/waits.html>
<https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_condition...>
<https://stackoverflow.com/questions/15122864/selenium-wait-until-document-is-ready>
<https://blog.codeship.com/get-selenium-to-wait-for-page-load/>
<http://barancev.github.io/slow-loading-pages/>
<http://barancev.github.io/page-loading-complete/>


####Git

[отличный интерактивный туториал](https://learngitbranching.js.org/)
[лучшая книга вообще](https://git-scm.com/book/ru/v2/) 
<https://hyperskill.org/learn/topic/257/>
<https://stepik.org/course/4138/>
<http://www-cs-students.stanford.edu/~blynn/gitmagic/intl/ru/index.html>
<https://habr.com/company/intel/blog/344962/>
<https://githowto.com/ru>
[как писать хорошие сообщения о коммитах](http://frontiermag.ru/commit-message.html)


####Тестирование веб-приложений

[инструменты для тестирования кода в Python](https://realpython.com/python-testing/)
[Пирамида тестов на практике](https://habr.com/ru/post/358950/)
[Документация unittest](https://docs.python.org/3/library/unittest.html)


####Использование фикстур в PyTest

[Фикстуры - определения](https://en.wikipedia.org/wiki/Test_fixture#Software)
[Фикстуры в PyTest](https://docs.pytest.org/en/latest/fixture.html#pytest-fixtures-explicit-modular-scalable)
[setup и teardowm методы](https://docs.pytest.org/en/latest/xunit_setup.html#module-level-setup-teardown)
<https://habr.com/ru/company/yandex/blog/242795/>
<https://medium.com/@dmrlx/%D0%B2%D0%B2%D0%B5%D0%B4%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B2-pytest-cc6175c7d0dc>
<https://docs.pytest.org/en/latest/fixture.html>
[Skip and xfail: dealing with tests that cannot succeed](https://docs.pytest.org/en/latest/skipping.html)


####Параметризация, конфигурирование, плагины

[Parametrizing fixtures and test functions](https://docs.pytest.org/en/latest/parametrize.html)
[Инструкции по установке geckodriver](https://selenium-python.com/install-geckodriver)
[Передача параметров в PyTest из командной строки](https://docs.pytest.org/en/latest/example/simple.html?highlight=addoption)
[Список плагинов PyTest](http://docs.pytest.org/en/latest/plugins.html)
[Полный список доступных плагинов с описаниями](https://plugincompat.herokuapp.com/)
[Настройка вывода PyTest](https://docs.pytest.org/en/latest/usage.html#modifying-python-traceback-printing)


####ООП
 
<https://stepik.org/lesson/24461/step/1?unit=6767>
<https://tproger.ru/translations/oop-principles-cheatsheet/>


####Code Style

<https://docs.python-guide.org/writing/style/>
<https://www.python.org/dev/peps/pep-0008/>
<https://habr.com/ru/post/266969/>
<https://habr.com/ru/post/206868/>
<https://pep8.ru/doc/pep8/>
<https://pythonworld.ru/osnovy/pep-8-rukovodstvo-po-napisaniyu-koda-na-python.html>


####POM
 
<https://page-objects.readthedocs.io>
<https://selenium-python.readthedocs.io/page-objects.html>
<https://github.com/SeleniumHQ/selenium/wiki/PageObjects>
<https://martinfowler.com/bliki/PageObject.html>
<https://medium.com/tech-tajawal/page-object-model-pom-design-pattern-f9588630800b>


####Исключения
 
<http://pythonworld.ru/tipy-dannyx-v-python/isklyucheniya-v-python-konstrukciya-try-except-dlya-obrabotki-isklyuchenij.html>


####Splinter

[Документация](https://splinter.readthedocs.io/en/latest/index.html)
[Код](https://github.com/cobrateam/splinter)
[Код и документация pytest-splinter](https://github.com/pytest-dev/pytest-splinter)


####Selene

[Документация](https://selene-docs-test.readthedocs.io/en/latest/introduction.html)
[Код](https://github.com/yashaka/selene)
[Презентация](https://www.youtube.com/watch?v=BzfOeHJrguQ)


####PyPOM

[Документация](https://pypom.readthedocs.io/en/latest/)
[Код](https://github.com/mozilla/PyPOM)


####Webium

[Документация](http://wgnet.github.io/webium/)
[Код](https://github.com/wgnet/webium)
[Презентация](https://www.youtube.com/watch?v=XrL1BLgkKyA) 




###Pytest как использовать несколько фикстур, вспомогательные функции и классы вместе (взято [отсюда](https://github.com/JakUi/stepik-auto-tests-course/blob/master/%D0%A4%D0%B8%D0%BA%D1%81%D1%82%D1%83%D1%80%D1%8B%20%D0%B8%20%D0%BA%D0%BB%D0%B0%D1%81%D1%81%D1%8B.txt)

Предусловия: браузер открываем и закрываем фикстурой, используются вспомогательные функции (например для входа в аккаунт)

Алгоритм работы:

1. Подключить библиотеки и модули
2. Объявить функции-фикстуры
  2.1 Пример фикстуры запуска и закрытия браузера 

    @pytest.fixture(scope='class') #объявляем, что функция является фикстурой
    def browser(): #название функции может быть любым
        driver = webdriver.Chrome() #инициализируем браузер
        #driver.set_window_size(2000, 1200) #Изменяем размер окна до 2000*1200 пикселей
        driver.implicitly_wait(25)
        yield #весь код внутри функции под этой командой будет выполнятся по завершении всех тестов в классе 
        #(если scope у фикстуры = class) иначе - после каждого теста
        print('teardown')
        driver.quit() #закрываем браузер

!!!Если браузер инициализируется и открывается при помощи фикстуры - название функции-фикстуры, в которой инициализировали браузер 
нужно передать в качестве аргумента для всех остальных фикстур. 

2.2 Объявляем другие фикстуры (например следующий код удаляет товары из корзины магазина в моём тесте)

@pytest.yield_fixture #выполняется для каждой функции
def clean_cart(browser): #в функцию передаём имя функции-фикстуры, в которой инициализировали браузер (здесь эта фикстура “browser”)
    yield #по завершении теста выполняется код, который идет после этой команды
    print('yield')
    browser.get('https://******.com/ru/cabinet/') #Возвращаемся в ЛК
    #Открываем окно магазина
    time.sleep(5.0) #ждём загрузки страницы
    store = browser.find_element_by_css_selector('[data-test="widget__button-store"]')#ищем кнопку "магазин"
    browser.execute_script("return arguments[0].scrollIntoView(true);", store) #Скроллим страницу до кнопки "магазин"
    store.click()
    browser.find_element_by_css_selector('[data-test="sidebar__button-REVIEW"]') #Проверяем, что магазин загружен (ищем раздел "Обзор")
    try:
        remove = browser.find_elements_by_css_selector('[data-test="cart__item-remove"]') #Ищем все иконки удалить в корзине
        #Удаляем все товары из корзины       
        for delete in remove:
            delete.click() #Кликаем на каждую иокнку удалить
            time.sleep(1.0)
    except:
        pass
    finally:
        browser.find_element_by_css_selector('[data-test="button-close"]').click() #Находим иконку "Закрыть" и кликаем на нее
        
3. Объявить вспомогательные функции. По такой же схеме как и в пункте 2.2 за исключением того, что в декоратор @pytest.fixture 
функции не оборачиваются. 

4. Создать класс. Внутри класса создать функции-тесты (в них и будет код тестов). Вспомогательные функции можно вызвать внутри 
класса без приставки self., если они объявлены вне класса. При объявлении функций внутри класса в каждую функцию в качестве параметра 
обязательно! нужно передать следующее: self, browser (название фикстуры, в которой инициализируем браузер), название остальных фикстур 
(если они применяются не к классу целиком и должны выполняться для этой функции)

4.1 Дополнительные функции (которые объявлены вне тела класса) внутри класса вызываются так: имя_функции(имя_фикстуры_инициализации_браузера)
Например:
    open_store(browser)
4.2 Внутри функций-тестов все команды selenium теперь должны начинаться не с переменной в которой объявлен браузер 
(например driver.find_element_by_css_selector()), а с названия фикстуры в которой выполняется инициализация браузера (для фикстуры 
browser - с "browser."), при этом self. перед командами ставить не нужно

Пример реализации:

@pytest.fixture(scope='class')
def browser():
    driver = webdriver.Chrome()
    driver.set_window_size(2000, 1200) #Изменяем размер окна до 2000*1200 пикселей
    driver.get(link)
    driver.implicitly_wait(25)
    yield driver
    print('teardown')
    driver.quit()


@pytest.yield_fixture #выполняется для каждой функции
def clean_cart(browser):
    yield #по завершении теста выполняется код, который идет после этой команды
    print('yield')
    browser.get('https://*******.com/ru/cabinet/') #Возвращаемся в ЛК
    #Открываем окно магазина
    time.sleep(5.0) #ждём загрузки страницы
    store = browser.find_element_by_css_selector('[data-test="widget__button-store"]')#ищем кнопку "магазин"
    browser.execute_script("return arguments[0].scrollIntoView(true);", store) #Скроллим страницу до кнопки "магазин"
    store.click()
    browser.find_element_by_css_selector('[data-test="sidebar__button-REVIEW"]') #Проверяем, что магазин загружен (ищем раздел "Обзор")
    try:
        remove = browser.find_elements_by_css_selector('[data-test="cart__item-remove"]') #Ищем все иконки удалить в корзине
        #Удаляем все товары из корзины       
        for delete in remove:
            delete.click() #Кликаем на каждую иокнку удалить
            time.sleep(1.0)
    except:
        pass
    finally:
        browser.find_element_by_css_selector('[data-test="button-close"]').click() #Находим иконку "Закрыть" и кликаем на нее

def enter_on_start(browser): #Логинимся
    browser.get(link)
    #Выполняем вход в аккаунт
    browser.find_element_by_css_selector('[data-template="#login_box"]').click() #ищем кнопку "Войти" и кликаем на неё
    browser.login = browser.find_element_by_id('login_mail')
    browser.login.send_keys('*******@gmail.com')
    browser.password = browser.find_element_by_id('login_pass')
    browser.password.send_keys('*********')
    browser.find_element_by_id('agreementSocial').click()
    browser.find_element_by_id('login_submit').click()

def enter_on_pro_plus(browser): #Логинимся в *******.com пользователь с ТП Про+
    browser.get(link)
    #Выполняем вход в аккаунт
    browser.find_element_by_css_selector('[data-template="#login_box"]').click() #ищем кнопку "Войти"
    browser.login = browser.find_element_by_id('login_mail')
    browser.login.send_keys('******_1@*******.com')
    browser.password = browser.find_element_by_id('login_pass')
    browser.password.send_keys('******')
    browser.find_element_by_id('agreementSocial').click()
    browser.find_element_by_id('login_submit').click()

def open_store(browser): #Функция открывает магазин
    time.sleep(5.0) #ждём загрузки страницы
    store = browser.find_element_by_css_selector('[data-test="widget__button-store"]')#ищем кнопку "магазин"
    browser.execute_script("return arguments[0].scrollIntoView(true);", store) #Скроллим страницу до кнопки "магазин"
    store.click()
    browser.find_element_by_css_selector('[data-test="sidebar__button-REVIEW"]') #Проверяем, что магазин загружен (ищем раздел "Обзор")

def close_store(browser): #Функция будет закрывать магазин
    browser.find_element_by_css_selector('[data-test="button-close"]').click() #Находим иконку "Закрыть" и кликаем на нее
    
def delete_all(browser): #Функция отменяет оплату, удаляет все товары из корзины и закрывает магазин
    browser.get('https://*******.com/ru/cabinet/') #Возвращаемся в ЛК
    open_store(browser) #Открываем окно магазина
    browser.goods = browser.find_elements_by_css_selector('[data-test="cart__item-remove"]') #Ищем все иконки удалить в корзине
    #Удаляем все товары из корзины       
    for browser.good in browser.goods:
        browser.good.click() #Кликаем на каждую иокнку удалить
        time.sleep(1.0)
    close_store(browser)

def logout(browser): #Функция осуществляет выход из аккаунта
    browser.avatar = browser.find_element_by_css_selector('[data-test="widget__button-user"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.avatar) #Скроллим страницу так, чтобы был виден аватар профиля
    browser.avatar.click() #клик на аватар профиля
    browser.escape = browser.find_element_by_xpath('//button[contains(text(), "Выход")]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", browser.escape) #Скроллим страницу так, чтобы была видна кнопка "Выйти"
    time.sleep(2.0)
    browser.escape.click() #Выходим из аккаунта
    time.sleep(2.0)
    
class TestGlobal():
    def test_go_to_tab_vidget(self, browser): #Пользователь с ТП Старт/ПРО. Переход в вкладку "Виджет"
        enter_on_start(browser) #здесь в функцию enter_on_start передаём имя фикстуры, в которой инициализирован браузер
        open_store(browser)
        browser.find_element_by_css_selector('[data-test="sidebar__button-WIDGET"]').click()
        browser.find_element_by_css_selector('[src="https://files.*******.com/upload/projects/images/*******/201710/thumb100x100_w_9db657467f8fe87796e1c7405a57824e_668f48d6.jpg"]')
        browser.find_element_by_css_selector('[data-test="widget__go-over"]').click() #Ищем кнопку "Перейти" и кликаем на нее
        browser.new_window = browser.window_handles[1] #Второй открытой вкладке (после клика на "Перейти" открывается новая вкладка) присваиваем имя "new_window"
        browser.window = browser.window_handles[0]
        browser.switch_to.window(browser.new_window) #Переходим на вторую вкладку
        browser.find_element_by_class_name('header__Back-sc-1ws5ve8-2.ikSpXv')
        browser.close()
        browser.switch_to.window(browser.window)
        close_store(browser)

    def test_basket_delete_goods(self, browser, clean_cart): #Корзина. Удалить товар
        open_store(browser)
        browser.find_element_by_css_selector('[data-test="sidebar__button-RENDERS"]').click() #Переходим в раздел "Рендеры"
        browser.find_element_by_css_selector('[data-test="card_products-0"] [data-test="card__button-in-cart"]').click() #Добавляем пробный рендер в корзину
        browser.find_element_by_css_selector('[data-test="card_products-0"] [data-test="card__button-go-over"]').click() #Переходм в корзину с карточки "Пробный рендер"
        browser.find_element_by_css_selector('[data-test="cart__item-remove"]').click() #Клик на иконку корзины (удаляем товар из корзины)
        close_store(browser)

    def test_payment_with_card(self, browser, clean_cart): #Оплата товара банковской картой
        open_store(browser)
        browser.find_element_by_css_selector('[data-test="sidebar__button-RENDERS"]').click() #Переходим в раздел "Рендеры"
        browser.find_element_by_css_selector('[data-test="card_products-0"] [data-test="card__button-in-cart"]').click() #Добавляем пробный рендер в корзину
        browser.find_element_by_css_selector('[data-test="card_products-0"] [data-test="card__button-go-over"]').click() #Переходм в корзину с карточки "Пробный рендер"
        #browser.find_element_by_css_selector('[data-test="cart__agreement"]').click() #Соглашаемся с условиями
        browser.find_element_by_css_selector('[for="agreement"]').click()
        browser.find_element_by_css_selector('[data-test="cart__go-to-pay"]').click() #Переходим к оплате
        browser.find_element_by_css_selector('[aria-label="Google Pay"]') #Ждем загрузки страницы оплаты
        delete_all(browser)


