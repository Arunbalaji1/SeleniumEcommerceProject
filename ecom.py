from pages.search_page import SearchPage
from pages.cart_page import CartPage 
from pages.product_page import ProductPage 
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
    search = SearchPage(driver) 
    search.search_product("Argus All-Weather Tank")
    assert 'Argus All-Weather Tank' in driver.page_source  
    product = ProductPage(driver) 
    product.add_to_cart() 
    success_message = driver.find_element(By.CLASS_NAME,"message-success").text
    assert "You added" in success_message
    driver.find_element(By.CLASS_NAME,"showcart").click()
    time.sleep(5)
    cart = CartPage(driver) 
    cart.proceed_to_checkout() 
    success_message = driver.find_element(By.CLASS_NAME,"opc-block-summary").text
    assert "Order Summary" in success_message 
