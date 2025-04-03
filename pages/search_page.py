from selenium.webdriver.common.by import By 
 
class SearchPage: 
    def __init__(self, driver): 
        self.driver = driver
        
 
    search_box = (By.ID, "search") 
    search_button = (By.CSS_SELECTOR, "button.search") 
 
    def search_product(self,product_name):
        self.driver.find_element(*self.search_box).send_keys(product_name) 
        self.driver.find_element(*self.search_button).click()
        
