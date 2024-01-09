import time
import pytest
import string
import random
from Utilities.ReadPropertyfile import ReadConfig
from PageObjects.Common_Methods import common_methods
from PageObjects.Widgets_page import Widget
from TestCases.confest import setup
from Utilities.customLogger import LogGen


class Test_001_Element:
    url = "https://demoqa.com/"
    logger = LogGen.loggen()

    def test_widgets_page(self,setup):
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
        self.cm.click_on_text("Widgets")
        self.cm.Scroll_Down()
        self.cm.click_on_text("Widgets")
        self.cm.Scroll_Down()
        self.cm.click_on_text("Accordian")
        self.cm.click_on_text("What is Lorem Ipsum?")
        self.cm.click_on_text("Where does it come from?")
        self.cm.Scroll_Down()
        time.sleep(4)
        self.cm.click_on_text("Why do we use it?")
        self.cm.click_on_text("Auto Complete")
        self.wg = Widget(self.driver)
        time.sleep(2)
