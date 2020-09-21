link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

#на странице товара есть кнопка добавления в корзину
def test_product_has_a_baskets_button(browser):
    browser.get(link)
    assert browser.find_element_by_class_name('btn-add-to-basket').is_displayed(), \
        'Кнопка добавления товара в корзину отсутсвует'
