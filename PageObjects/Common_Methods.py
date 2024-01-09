from selenium import webdriver
import logging
from selenium.webdriver.common.by import By
import time
import random
import string

class common_methods:

    def __init__(self,driver):
        self.driver=driver

    def highlight_elm(self,text,clr):
        ele = self.driver.find_element(By.XPATH, "//*[contains(text(),'"+text+"')]")
        self.driver.execute_script("arguments[0].style.color='"+clr+"'",ele)
        logging.info("Verified on %s",str(text))
        time.sleep(2)

    def Scroll_Down_for_text(self,text_name):
        ele=self.driver.find_element(By.XPATH,"//*[contains(text(),'"+text_name+"')]")
        self.driver.execute_script("arguments[0].scrollIntoView();",ele)
        time.sleep(2)
        logging.info("Scrolled till %s",text_name)

    def Scroll_Down(self):
        self.driver.execute_script("window.scrollBy(0, 500)")

    def click_on_text(self,text_name):
        ele=self.driver.find_element(By.XPATH,"//*[text()='"+text_name+"']").click()
        time.sleep(2)
        logging.info("Verified on %s",text_name)

    def switch_to_parent_window(self):
        parent = self.driver.window_handles[0]
        self.driver.switch_to.window(parent)
        value_pageTitle = self.driver.title
        time.sleep(3)
        logging.info("The page title is %s",value_pageTitle)

    def navigate_back(self):
        self.driver.back()

    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

    def random_generator_for_Address(size=10, chars=string.ascii_lowercase + string.ascii_uppercase):
        return ''.join(random.choice(chars) for x in range(size))



