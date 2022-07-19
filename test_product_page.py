from pages.main_page import MainPage
from pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.add_product()  # выполняем метод страницы — переходим на страницу логина
    #login_page = LoginPage(browser, browser.current_url)
    #login_page.should_be_login_page()
