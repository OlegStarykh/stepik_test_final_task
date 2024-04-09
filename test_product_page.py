from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(driver):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(driver, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.correct_cost_in_cart()
    page.correct_product_added()
