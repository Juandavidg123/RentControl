from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class MySeleniumTests(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Chrome() 
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def test_register_and_login(self):
        self.browser.get(f"{self.live_server_url}/signup/")

        username_input = self.browser.find_element(By.NAME, "username")
        password1_input = self.browser.find_element(By.NAME, "password1")
        password2_input = self.browser.find_element(By.NAME, "password2")

        username_input.send_keys("santiagoramos")
        password1_input.send_keys("AWSDzx123*")
        password2_input.send_keys("AWSDzx123*")
        
        password2_input.send_keys(Keys.RETURN)
        
        time.sleep(1) 
        
        self.browser.get(f"{self.live_server_url}/logout/")
        self.browser.get(f"{self.live_server_url}/signin/")

        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")

        username_input.send_keys("santiagoramos")
        password_input.send_keys("AWSDzx123*")
        
        password_input.send_keys(Keys.RETURN)

        time.sleep(1)