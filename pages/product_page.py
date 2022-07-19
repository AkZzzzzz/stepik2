from .base_page import BasePage
from .locators import LoginPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
  def add_product(self):
    product_add = self.browser.find_element(By.CLASS, ".btn-add-to-basket")
    product_add.click()
    
    
    
    
