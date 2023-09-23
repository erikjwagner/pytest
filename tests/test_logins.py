import pytest

def test_login_success(request, controller):
    """Successfully Log in to application"""
    controller.home_page.user_name.send_keys("standard_user")
    controller.home_page.password.send_keys("secret_sauce")
    controller.home_page.login_button.click()
    controller.inventory_page.burger_menu.assert_displayed()

# def test_login_failure(request, controller):
#     """Incorrect Password doesn't allow login"""
#     controller.home_page.user_name.send_keys("standard_user")
#     controller.home_page.password.send_keys("invalid_password")
#     controller.home_page.login_button.click()
#     controller.inventory_page.burger_menu.assert_not_displayed()
