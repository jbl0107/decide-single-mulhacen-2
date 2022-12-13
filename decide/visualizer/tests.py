from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.tests import BaseTestCase 
from selenium.webdriver.support.color import Color

# Create your tests here.

class VisualizerTestCase(BaseTestCase):

    def test_funcionamiento_pagina_visualizer(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("http://0.0.0.0:8080/visualizer/1/")

        assert driver.find_element(By.CSS_SELECTOR, ".navbar-brand").text == "Decide"

