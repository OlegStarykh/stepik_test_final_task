from .pages.product_page import ProductPage
import pytest
from .pages.lokators import ProductPageLocators


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
# pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(driver, link):
#     # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
#     page = ProductPage(driver, link)
#     page.open()
#     page.add_to_cart()
#     page.solve_quiz_and_get_code()
#     page.correct_cost_in_cart()
#     page.correct_product_added()
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_cart()
    assert page.is_not_element_present(
        *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


def test_guest_cant_see_success_message(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(driver, link)
    page.open()
    assert page.is_not_element_present(
        *ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_cart()
    assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), 'Sucsess messege isnt disappeared'
