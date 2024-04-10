import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")

@pytest.fixture(scope="function")
def language(request):
    page_language = request.config.getoption("language")
    return page_language


@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test..")
    options = Options()
    options.page_load_strategy = 'normal'
    options.add_argument('--window-size=920,1080')
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument('--incognito')
    options.add_argument('--disable-cache')
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36")
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
    driver = webdriver.Chrome(options=options)
    yield driver
    print("\nquit browser..")
    driver.quit()

