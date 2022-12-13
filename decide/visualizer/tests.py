from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.tests import BaseTestCase 
from selenium.webdriver.support.color import Color


import random
import itertools
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from base import mods
from census.models import Census
from mixnet.mixcrypt import ElGamal
from mixnet.mixcrypt import MixCrypt
from mixnet.models import Auth
from voting.models import Voting, Question, QuestionOption

# Create your tests here.

class VisualizerTestCase(BaseTestCase):

    def test_funcionamiento_pagina_visualizer(self):
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        driver.get("http://0.0.0.0:8080/visualizer/1/")

        assert driver.find_element(By.CSS_SELECTOR, ".navbar-brand").text == "Decide"


    def test_visualizer_voting_id_negativo(self):
        response = self.client.put('/visualizer/'+str(-1), follow=True)
        self.assertEqual(response.status_code, 404)