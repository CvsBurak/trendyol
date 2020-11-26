from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser = request.config.getoption("browser")
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        options.add_experimental_option("prefs", prefs)
        options.add_argument("start-maximized")
        options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(
                executable_path="/Users/cvsburak/Desktop/chromedriver", options=options)
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path="/Users/cvsburak/Desktop/chromedriver")
    driver.get("https://www.trendyol.com")
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[8]/div/div/a")))
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
    except:
        pass
    try:
        element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[7]/div/div/a")))
        actions = ActionChains(driver)
        actions.move_to_element(element).click().perform()
    except:
        pass
    request.cls.driver = driver
    yield
    driver.close()
