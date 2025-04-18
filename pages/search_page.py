from selenium.webdriver.common.by import By 
import time
 
class SearchPage: 
    def __init__(self, driver): 
        self.driver = driver
        
 
    search_box = (By.ID, "search") 
    search_button = (By.CSS_SELECTOR, "button.search")
   
    def search_product(self,product_name):
        self.driver.find_element(*self.search_box).send_keys(product_name) 
        self.driver.find_element(*self.search_button).click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, product_name).click()
        time.sleep(2)
        
