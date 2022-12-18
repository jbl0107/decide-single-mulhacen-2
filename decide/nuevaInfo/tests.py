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

class TranslationCaseInfoDecide(StaticLiveServerTestCase):

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
        self.driver.get("http://localhost:8080/nuevaInfo/masInfo/")
        
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
        self.driver.get("http://localhost:8080/nuevaInfo/masInfo/")
        
        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(2)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="titulo"))
        self.assertEqual(username_label.text, "El Gateway")

    

    def test_german_translation_infoDecide(self):

        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8080/nuevaInfo/masInfo/")
        
        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(3)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="titulo"))
        self.assertEqual(username_label.text, "Das Tor")



class TranslationCaseEgc(StaticLiveServerTestCase):

    def setUp(self):
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

    def test_english_translation_egc(self):

        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8080/nuevaInfo/masInfoEgc/")

        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(1)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="titulo"))
        self.assertEqual(username_label.text, "Evolution and Change Management")

    def test_spanish_translation_egc(self):

        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8080/nuevaInfo/masInfoEgc/")

        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(2)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="titulo"))
        self.assertEqual(username_label.text, "Evolución y gestión de la configuración")

    def test_german_translation_egc(self):

        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8080/nuevaInfo/masInfoEgc/")

        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(3)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="titulo"))
        self.assertEqual(username_label.text, "Evolution und Change Management")



class TranslationCaseETSII(StaticLiveServerTestCase):

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

    def test_english_translation_ETSII(self):

        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8080/nuevaInfo/masInfoETSII/")
        
        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(1)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="titulo"))
        self.assertEqual(username_label.text, "The ETS of Computer Engineering")

    def test_spanish_translation_ETSII(self):

        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8080/nuevaInfo/masInfoETSII/")
        
        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(2)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="titulo"))
        self.assertEqual(username_label.text, "La E.T.S. de Ingeniería Informática")
    
    def test_german_translation_ETSII(self):

        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8080/nuevaInfo/masInfoETSII/")
        
        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(3)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="titulo"))
        self.assertEqual(username_label.text, "Das ETS der Technischen Informatik")


class TranslationCaseTraducciones(StaticLiveServerTestCase):

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

    def test_english_translation_traducciones(self):

        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8080/nuevaInfo/masInfoTraducciones/")
        
        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(1)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="titulo"))
        self.assertEqual(username_label.text, "Translation subsystem")

    def test_spanish_translation_traducciones(self):

        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8080/nuevaInfo/masInfoTraducciones/")
        
        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(2)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="titulo"))
        self.assertEqual(username_label.text, "Subsistema de traducciones")
    
    def test_german_translation_traducciones(self):

        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8080/nuevaInfo/masInfoTraducciones/")
        
        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(3)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="titulo"))
        self.assertEqual(username_label.text, "Übersetzungssubsystem")

class TranslationCaseJornadas(StaticLiveServerTestCase):

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

    def test_english_translation_jornadas(self):

        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8080/nuevaInfo/masInfoJornadas/")
        
        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(1)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="horario"))
        self.assertEqual(username_label.text, "Schedule:")

    def test_español_translation_jornadas(self):

        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8080/nuevaInfo/masInfoJornadas/")
        
        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(2)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="horario"))
        self.assertEqual(username_label.text, "Horario:")
    
    def test_denmark_translation_jornadas(self):

        self.driver.set_window_size(1920,1080)
        options = webdriver.ChromeOptions()
        options.headless = True
        driver = webdriver.Chrome(options=options)
        self.driver.get("http://localhost:8080/nuevaInfo/masInfoJornadas/")
        
        language_selector = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.NAME, value="language"))
        language_selector.click()
        selected_language = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.CSS_SELECTOR, value="select > option:nth-child(3)"))
        selected_language.click()
        change_language_button = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="boton-submit"))
        change_language_button.click()
        username_label = WebDriverWait(self.driver, timeout=10).until(lambda d: d.find_element(by=By.ID, value="horario"))
        self.assertEqual(username_label.text, "Zeitlicher Ablauf:")
    
    