from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select 
import time
 
class ProductPage: 
    def __init__(self, driver): 
        self.driver = driver 
        time.sleep(10)
    size=(By.ID,"option-label-size-143-item-166") 
    color=(By.ID,"option-label-color-93-item-52") 
    add_to_cart_button = (By.ID, "product-addtocart-button") 
 
    def add_to_cart(self): 
        self.driver.find_element(*self.size).click() 
        time.sleep(5)
        self.driver.find_element(*self.color).click()
        time.sleep(5)
        self.driver.find_element(*self.add_to_cart_button).click()
        time.sleep(5) 