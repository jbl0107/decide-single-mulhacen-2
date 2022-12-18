from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.tests import BaseTestCase 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from base import mods


class BoothTestCase(BaseTestCase):

    def test_booth_voting_id_negativo(self):
        response = self.client.put('/booth/'+str(-1), follow=True)
        self.assertEqual(response.status_code, 404)

    def test_booth_voting_id_inexistente(self):
        response = self.client.put('/booth/'+str(999), follow=True)
        self.assertEqual(response.status_code, 404)

    



# class TraducTestCase(StaticLiveServerTestCase):

#     def setUp(self):
#         #Load base test functionality for decide
#         self.base = BaseTestCase()
#         self.base.setUp()

#         options = webdriver.ChromeOptions()
#         options.headless = True
#         self.driver = webdriver.Chrome(options=options)

#         super().setUp() 
        
#     def tearDown(self):           
#         super().tearDown()
#         self.driver.quit()

#         self.base.tearDown()
    
#     def test_en(self):

#         self.driver.set_window_size(1920,1080)
#         options = webdriver.ChromeOptions()
#         options.headless = True
#         self.driver = webdriver.Chrome(options=options)

#         self.driver.get('http://localhost:8080/booth/4/')
        
#         language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
#         language_selector.click()
#         selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(1)"))
#         selected_language.click()
#         change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
#         change_language_button.click()
#         label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="botonVotar"))
#         self.assertEqual(label.text, "Vote")

#     def test_es(self):

#         self.driver.set_window_size(1920,1080)
#         options = webdriver.ChromeOptions()
#         options.headless = True
#         self.driver = webdriver.Chrome(options=options)

#         self.driver.get('http://localhost:8080/booth/4/')
        
#         language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
#         language_selector.click()
#         selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(2)"))
#         selected_language.click()
#         change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
#         change_language_button.click()
#         label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="botonVotar"))
#         self.assertEqual(label.text, "Vota")

#     def test_de(self):

#         self.driver.set_window_size(1920,1080)
#         options = webdriver.ChromeOptions()
#         options.headless = True
#         self.driver = webdriver.Chrome(options=options)

#         self.driver.get('http://localhost:8080/booth/4/')
        
#         language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
#         language_selector.click()
#         selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(3)"))
#         selected_language.click()
#         change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
#         change_language_button.click()
#         label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="botonVotar"))
#         self.assertEqual(label.text, "Abstimmung")
        

    