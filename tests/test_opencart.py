import time
import allure
from page_objects.AdminPage import AdminPage
from page_objects.CatalogPage import CatalogPage
from page_objects.MainPage import MainPage
from page_objects.RegisterPage import RegisterPage
from page_objects.ProductPage import ProductPage


@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_slideshow(browser):
    slideshow = MainPage(browser).click_slideshow()
    assert slideshow

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_search(browser):
    button_search = MainPage(browser).click_button_search()
    assert button_search

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_cart(browser):
    button_cart = MainPage(browser).click_button_cart()
    assert button_cart

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_site_map(browser):
    site_map = MainPage(browser).click_site_map()
    assert site_map

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_currency(browser):
    currency = MainPage(browser).click_currency()
    assert currency

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_currency(browser):
    currency = MainPage(browser).click_currency()
    assert currency

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_catalog_sort(browser):
    MainPage(browser).go_to_catalog_page()
    sort_catalog = CatalogPage(browser).click_sort_catalog()
    assert sort_catalog

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_catalog_show(browser):
    MainPage(browser).go_to_catalog_page()
    show_catalog = CatalogPage(browser).click_show_catalog()
    assert show_catalog

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_wishlist(browser):
    MainPage(browser).go_to_catalog_page()
    add_wishlist = CatalogPage(browser).click_add_wishlist()
    assert add_wishlist

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_add_to_cart(browser):
    MainPage(browser).go_to_catalog_page()
    add_in_cart = CatalogPage(browser).click_add_in_cart()
    assert add_in_cart

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_list_catalog(browser):
    MainPage(browser).go_to_catalog_page()
    grid_catalog = CatalogPage(browser).click_grid_catalog()
    assert grid_catalog

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_product_in_cart(browser):
    MainPage(browser).go_to_product_page()
    product_cart = ProductPage(browser).click_product_cart()
    assert product_cart

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_write_review(browser):
    MainPage(browser).go_to_product_page()
    review = ProductPage(browser).click_review()
    assert review

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_compare_product(browser):
    MainPage(browser).go_to_product_page()
    product_compare = ProductPage(browser).click_product_compare()
    assert product_compare

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_share_product(browser):
    MainPage(browser).go_to_product_page()
    product_share = ProductPage(browser).click_product_share()
    assert product_share

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_product_image(browser):
    MainPage(browser).go_to_product_page()
    image_tap = ProductPage(browser).click_image_tap()
    assert image_tap

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_registration_continue(browser):
    MainPage(browser).go_to_register_page()
    continue_registration = RegisterPage(browser).click_continue_registration()
    assert continue_registration

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_privacy(browser):
    MainPage(browser).go_to_register_page()
    privacy_policy = RegisterPage(browser).click_privacy_policy()
    assert privacy_policy

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_login_page(browser):
    MainPage(browser).go_to_register_page()
    login_to_page = RegisterPage(browser).click_login_to_page()
    assert login_to_page

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_forgot_password(browser):
    MainPage(browser).go_to_register_page()
    password_forgotten = RegisterPage(browser).click_password_forgotten()
    assert password_forgotten

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_homepage(browser):
    MainPage(browser).go_to_register_page()
    to_homepage = RegisterPage(browser).click_to_homepage()
    assert to_homepage

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_login_admin(browser):
    MainPage(browser).go_to_admin_page()
    admin_login = AdminPage(browser).click_admin_login()
    assert admin_login

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_admin_password_forget(browser):
    MainPage(browser).go_to_admin_page()
    admin_login = AdminPage(browser).click_admin_password_forget()
    assert admin_login

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_admin_catalog(browser):
    MainPage(browser).go_to_admin_page()
    admin_login = AdminPage(browser).click_admin_login()
    catalog_admin = AdminPage(browser).click_catalog_admin()
    assert catalog_admin

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_admin_to_main(browser):
    MainPage(browser).go_to_admin_page()
    admin_login = AdminPage(browser).click_admin_login()
    main_page = AdminPage(browser).click_main_page()
    assert main_page

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_add_new_product_in_admin(browser):
    MainPage(browser).go_to_admin_page()
    AdminPage(browser).click_admin_login()
    AdminPage(browser).click_catalog_admin()
    AdminPage(browser).click_products_link()
    AdminPage(browser).click_button_plus()
    AdminPage(browser).fill_new_product_form(name='Test1',
                                             description='Test1',
                                             meta_title='Test1',
                                             meta_description='Test1',
                                             meta_keywords='Test1',
                                             tags='test1,my_test1')
    alert = AdminPage(browser).warning_alert()
    assert alert

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_delete_product_in_admin(browser):
    MainPage(browser).go_to_admin_page()
    AdminPage(browser).click_admin_login()
    AdminPage(browser).click_catalog_admin()
    AdminPage(browser).click_products_link()
    AdminPage(browser).check_product()
    AdminPage(browser).click_delete_button()
    AdminPage(browser).confirm_alert()
    alert = AdminPage(browser).warning_alert()
    assert alert

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_register_new_user(browser):
    MainPage(browser).go_to_register_page()
    AdminPage(browser).fill_register_user_form(firstname='Max',
                                               lastname='Maximov',
                                               email='max@gmail.com',
                                               telephone=555012345,
                                               password='password',
                                               password2='password')
    alert = AdminPage(browser).warning_alert()
    assert alert

@allure.suite('MainPage')
@allure.epic("2022Q1")
@allure.feature("MainPage")
@allure.story("slideshow")
def test_currency_change(browser):
    MainPage(browser).click_currency()
    button_dollar = MainPage(browser).click_button_dollar()
    assert button_dollar