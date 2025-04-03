from pages.product_page import ProductPage 
from selenium.webdriver.common.by import By

 
def test_add_product_to_cart(driver): 
    driver.get("https://magento.softwaretestingboard.com/argus-all-weather-tank.html") 
    product = ProductPage(driver) 
    product.add_to_cart() 
    success_message = driver.find_element(By.CLASS_NAME,"message-success").text
    
    assert "You added" in success_message

