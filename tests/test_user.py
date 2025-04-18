import pytest
import time 
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("username", [ "performance_glitch_user","problem_user", ]) 

def test_checkout_multiple_users(driver, username, password="secret_sauce"):
    
    driver.get("https://www.saucedemo.com/") 
    driver.find_element(By.ID, "user-name").send_keys(username) 
    driver.find_element(By.ID, "password").send_keys(password) 
    driver.find_element(By.ID, "login-button").click() 
    time.sleep(5)
    assert "Products" in driver.page_source