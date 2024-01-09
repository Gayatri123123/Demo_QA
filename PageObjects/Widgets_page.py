from selenium import webdriver
import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os


class Widget:


    def __init__(self,driver):
        self.driver=driver

    def click_on_(self,btn_name):
        ele=self.driver.find_element(By.XPATH,"//*[text()='"+btn_name+"']").click()
        #time.sleep(2)
        logging.info("Verified on %s",btn_name)
