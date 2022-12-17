from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.color import Color

from base import mods
from base.tests import BaseTestCase
from django.contrib.auth.models import User

from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient, APITestCase


# Create your tests here.

class TranslationCaseDecide(StaticLiveServerTestCase):

    def setUp(self):
        #Load base test functionality for decide
        self.base = BaseTestCase()
        self.base.setUp()

        options = webdriver.ChromeOptions()
        options.headless = True
        self.driver = webdriver.Chrome(options=options)

        super().setUp() 
        
    def tearDown(self):           
        super().tearDown()
        self.driver.quit()

        self.base.tearDown()

    def test_english_translation_infoDecide(self):

        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8000/nuevaInfo/masInfo/")
        
        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(1)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="titulo"))
        self.assertEqual(username_label.text, "The Gateway")
    


    def test_spanish_translation_infoDecide(self):
        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8000/nuevaInfo/masInfo/")
        
        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(2)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="titulo"))
        self.assertEqual(username_label.text, "El Gateway")

    



