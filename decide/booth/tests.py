from django.test import TestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from base.tests import BaseTestCase 

from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from base import mods


class BoothTestCase(BaseTestCase):

    def test_booth_voting_id_negativo(self):
        response = self.client.put('/booth/'+str(-1), follow=True)
        self.assertEqual(response.status_code, 404)