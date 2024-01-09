import time
import pytest
import string
import random
from Utilities.ReadPropertyfile import ReadConfig
from PageObjects.Common_Methods import common_methods
from PageObjects.Elements_page import Element
from TestCases.confest import setup
from Utilities.customLogger import LogGen


class Test_001_Element:
    url = "https://demoqa.com/"
    logger = LogGen.loggen()

    def test_element_page(self,setup):
        self.logger.info("************Test_element page Started ***************")
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(2)
        self.driver.maximize_window()
        self.cm = common_methods(self.driver)
        self.cm.Scroll_Down()
        #self.cm.Scroll_Down_for_text("Book Store Application")
        time.sleep(2)
        #click on elements
        self.cm.click_on_text("Elements")
        self.ele = Element(self.driver)
        time.sleep(2)
        self.email = random_generator() + "@gmail.com"

        self.address = random_generator_for_Address() + "  House No 123"
        time.sleep(2)

        #textbox
        self.ele.click_on_textbox_btn(self.email, self.address)
        time.sleep(2)
        #checkbox
        self.cm.click_on_text("Check Box")
        self.ele.click_on_checkbox()
        #radio_button
        self.ele.click_on_radio_button()
        self.cm.Scroll_Down()
        #web_tables
        self.cm.click_on_text("Web Tables")
        self.ele.click_on_Web_Tables()
        self.ele.entering_fileds("First Name","ABC")
        self.ele.entering_fileds("Last Name","XYZ")
        self.ele.entering_fileds("name@example.com","abcxyz@gmail.com")
        self.ele.entering_fileds("Age","25")
        self.ele.entering_fileds("Salary","25000")
        self.ele.entering_fileds("Department","IT")
        self.ele.click_on_submit()
        self.cm.Scroll_Down()
        self.ele.highlight_row()
        self.cm.Scroll_Down()
        self.ele.click_on_delete()
        #buttons
        self.cm.click_on_text("Buttons")
        self.ele.click_on_buttons()
        self.cm.highlight_elm("You have done a double click",'pink')
        self.cm.highlight_elm("You have done a right click",'yellow')
        self.cm.highlight_elm("You have done a dynamic click",'pink')
        #link
        self.cm.Scroll_Down()
        self.cm.click_on_text("Links")
        self.cm.click_on_text("Home")
        self.cm.switch_to_parent_window()
        self.cm.click_on_text("Created")
        self.cm.Scroll_Down()
        time.sleep(2)
        #Broken Links
        self.cm.click_on_text("Broken Links - Images")
        self.cm.Scroll_Down()
        self.cm.click_on_text("Click Here for Valid Link")
        self.cm.navigate_back()
        self.cm.click_on_text("Click Here for Broken Link")
        #self.ele.highlight_p()
        self.cm.navigate_back()
        self.cm.Scroll_Down()
        #upload and download
        self.cm.click_on_text("Upload and Download")
        self.cm.click_on_text("Download")
        self.ele.upload_file()
        # Dynamic properties
        self.cm.Scroll_Down()
        self.cm.click_on_text("Dynamic Properties")
        self.cm.click_on_text("Color Change")
        self.logger.info("************Test_element page ended ***************")




    ''' 
    def test_element_page_checkbox(self,setup):
        self.logger.info("************Test_element Started ***************")
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.cm = common_methods(self.driver)
        time.sleep(2)
        self.cm.Scroll_Down()
        #self.cm.Scroll_Down_for_text("Book Store Application")
        time.sleep(3)
        self.cm.click_on_text("Elements")
        self.cm.click_on_text("Check Box")
        self.ele.click_on_checkbox()
        self.ele.click_on_radio_button()

     
    def test_element_page_radio_button(self,setup):
        self.logger.info("************Test_element Started ***************")
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        self.cm = common_methods(self.driver)
        time.sleep(2)
        self.cm.Scroll_Down()
        #self.cm.Scroll_Down_for_text("Book Store Application")
        time.sleep(3)
        self.cm.click_on_text("Elements")
        #self.cm.click_on_text("Radio Button")
        self.ele = Element(self.driver)
        self.ele.click_on_radio_button()



        #self.cm.Scroll_Down_for_text("Book Store Application")
    '''





def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_generator_for_Address(size=10, chars=string.ascii_lowercase + string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))



