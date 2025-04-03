from pages.search_page import SearchPage
import time 
from selenium.webdriver.common.by import By

def test_checkout_multiple_users(driver):
    
    driver.get("https://magento.softwaretestingboard.com/") 
    driver.find_element(By.LINK_TEXT, 'Sign In').click() 
    driver.find_element(By.NAME, "login[username]").send_keys("arunseleniumpython@gmail.com") 
    driver.find_element(By.NAME, "login[password]").send_keys("Arun#selenium") 
    driver.find_element(By.XPATH, "/html/body/div[2]/main/div[3]/div/div[2]/div[1]/div[2]/form/fieldset/div[4]/div[1]/button").click() 
    time.sleep(5)
    assert "Products" in driver.page_source 
    
 
def test_search_product(driver): 
    driver.get("https://magento.softwaretestingboard.com/") 
    search = SearchPage(driver) 
    search.search_product("Fusion Backpack")
    assert "Fusion Backpack" in driver.page_source 