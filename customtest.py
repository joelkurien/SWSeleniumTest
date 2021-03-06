# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class CustomTest():
  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def customtest(self):
      self.driver.get('https://bhavin121.github.io/')
      self.driver.set_window_size(846, 638)
      self.driver.find_element(By.CSS_SELECTOR, "a:nth-child(1) > .Text").click()
      self.driver.find_element(By.CSS_SELECTOR, ".recipeBox:nth-child(3) > .expandRead").click()
      time.sleep(5)
      self.driver.close()

test = CustomTest()
test.setup_method()
test.customtest()
test.teardown_method()