import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from types import SimpleNamespace
from page_selectors.home_page import HomePage
from page_selectors.inventory_page import InventoryPage

def pytest_addoption(parser):
    parser.addoption(
        '--xtra', action='store_true', default=False, help='Print extra information during test run'
    )

@pytest.fixture()
def xtra(request):
    xtra = request.config.getoption("--xtra")
    if xtra:
        print(f"\n***{request.function.__doc__}***")
    return xtra

@pytest.fixture()
def controller(xtra):
    controller = SimpleNamespace()
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    controller.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    controller.home_page = HomePage(controller.driver, xtra)
    controller.inventory_page = InventoryPage(controller.driver, xtra)
    controller.driver.get("https://www.saucedemo.com")
    yield controller

    controller.driver.quit()