import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver_path = r"chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
service = Service(driver_path)
@pytest.fixture(scope="function")
def driver():
  driver = webdriver.Chrome(service=service)
  driver.maximize_window()
  yield driver
  driver.quit()

