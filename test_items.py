import time


def test_find_basket(browser, request):
    language = request.config.getoption("language")
    browser.get(f"http://selenium1py.pythonanywhere.com/{language}/catalogue/coders-at-work_207/")
    time.sleep(10) # Для визуальной проверки, в задании сказано добавить (хотя там 30 сек)
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), f"Кнопка добавления в корзину не найдена для --{language} языка"
