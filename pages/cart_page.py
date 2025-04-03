from selenium.webdriver.common.by import By 
import time
class CartPage: 
    def __init__(self, driver): 
        self.driver = driver 
 
    checkout_button = (By.CLASS_NAME, "checkout") 
 
    def proceed_to_checkout(self): 
        self.driver.find_element(*self.checkout_button).click()
        time.sleep(5)