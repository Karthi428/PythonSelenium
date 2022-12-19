import pytest
from selenium import webdriver

from Config.config import TestData


@pytest.fixture()
def setup(request):
    print("initiating chrome driver")
    driver = webdriver.Chrome(TestData.CHROME_PATH)
    request.instance.driver = driver
    driver.get(TestData.BASE_URL)
    driver.maximize_window()

    yield driver
    driver.close()
