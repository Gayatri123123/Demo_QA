from selenium import webdriver
import logging
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os


class Element:


    def __init__(self,driver):
        self.driver=driver

    def click_on_btn_in_element(self,btn_name):
        ele=self.driver.find_element(By.XPATH,"//*[text()='"+btn_name+"']").click()
        #time.sleep(2)
        logging.info("Verified on %s",btn_name)

    def click_on_textbox_btn(self,email,address):
        self.driver.find_element(By.XPATH,'//*[@id="item-0"]/span').click()
        logging.info("Verified on testbox")
        self.driver.find_element(By.ID,'userName').send_keys("abc")
        logging.info("Entered the username")
        self.driver.find_element(By.ID,'userEmail').send_keys(email)
        logging.info("Entered the useremail")
        self.driver.find_element(By.ID,'currentAddress').send_keys(address)
        logging.info("Entered the currentAddress")
        self.driver.find_element(By.ID,'permanentAddress').send_keys(address)
        logging.info("Entered the permanentAddress")
        self.driver.execute_script("window.scrollBy(0, 300)")
        self.driver.find_element(By.ID,'submit').click()
        logging.info("Clicked on submit")

    def click_on_checkbox(self):
        self.driver.find_element(By.XPATH,'//*[@id="tree-node"]/div/button[1]').click()
        logging.info("Clicked on expand all")
        home_chechbox = self.driver.find_element(By.XPATH,'//*[@id="tree-node"]/ol/li/ol/li[2]/span/label').click()
        #time.sleep(2)
        logging.info("Checkbox selected for Desktop")
        #time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="tree-node"]/div/button[2]').click()
        logging.info("Clicked on Collapse all")

        '''
        
        if not home_chechbox.is_selected():
            home_chechbox.click()
            time.sleep(4)
        '''

#//*[@id="tree-node"]/ol/li/span/label

    def click_on_radio_button(self):
        self.driver.find_element(By.XPATH,'//*[@id="item-2"]').click()
        logging.info("Clicked on RadioBox")
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label').click()
        #time.sleep(2)
        logging.info("Selected Radio button 'YESRadio'")
        #time.sleep(2)
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/label').click()
        #time.sleep(2)
        logging.info("Selected Radio button 'impressiveRadio'")

    def click_on_Web_Tables(self):
        self.driver.find_element(By.ID,'addNewRecordButton').click()
        logging.info("Clicked on Add")

    def entering_fileds(self,text,field_name):
        #self.driver.find_element(By.ID,'firstName').send_keys("ABC")

        self.driver.find_element(By.XPATH,"//input[@placeholder='"+text+"']").send_keys(field_name)
        logging.info("Entered the %s",field_name)

    def click_on_submit(self):
        self.driver.find_element(By.ID,'submit').click()
        logging.info("Clicked on submit")

    def highlight_row(self):
        ele=self.driver.find_element(By.XPATH,'//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div')
        self.driver.execute_script("arguments[0].style.color='pink'",ele)
        #time.sleep(2)
        logging.info("highlighted the row")

    def click_on_delete(self):
        time.sleep(2)
        scroll_value=500
        self.driver.execute_script(f"window.scrollBy({scroll_value},0);")
        #self.driver.execute_script(f"window.scrollBy(0,{scroll_value});")
        self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[1]/div[2]/div[4]/div/div[7]/div/span[2]').click()
        #time.sleep(2)
        logging.info("Clicked on delete")
        '''
        self.driver.find_element(By.ID,'firstName').send_keys("ABC")
        self.driver.find_element(By.ID,'lastName').send_keys("XYZ")
        self.driver.find_element(By.ID,'userEmail').send_keys("abcxyz@gmail.com")
        '''

    def click_on_buttons(self):
        #double click
        ele = self.driver.find_element(By.ID,'doubleClickBtn')
        actions = ActionChains(self.driver)
        actions.double_click(ele).perform()
        logging.info("Clicked on double click me button")

        #right click
        ele = self.driver.find_element(By.ID,'rightClickBtn')
        actions.context_click(ele).perform()
        logging.info("Clicked on right click me button")
        #just click
        #time.sleep(2)
        ele = self.driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div[2]/div[2]/div[3]/button')
        ele.click()
        logging.info("Clicked on click me button")

    def highlight_p(self):
        ele=self.driver.find_element(By.TAG_NAME,'p')
        self.driver.execute_script("arguments[0].style.color='yellow'",ele)
        logging.info("Highlighted the Link Response")
        time.sleep(3)

    def upload_file(self):
        ele = self.driver.find_element(By.ID,'uploadFile')
        path = os.path.abspath("C:\\Users\\G51\\Downloads\\sampleFile.jpeg")
        ele.send_keys(path)
        ele = self.driver.find_element(By.ID,'uploadedFilePath')
        self.driver.execute_script("arguments[0].style.color='yellow'",ele)
        time.sleep(2)
        logging.info("Highlighted the file_path")







