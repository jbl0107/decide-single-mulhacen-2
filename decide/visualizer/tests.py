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

    def setUp(self):
        super().setUp()

    def tearDown(self):
        super().tearDown()

    def encrypt_msg(self, msg, v, bits=settings.KEYBITS):
        pk = v.pub_key
        p, g, y = (pk.p, pk.g, pk.y)
        k = MixCrypt(bits=bits)
        k.k = ElGamal.construct((p, g, y))
        return k.encrypt(msg)

    # def test_funcionamiento_pagina_visualizer(self):
    #     options = webdriver.FirefoxOptions()
    #     options.headless = True
    #     driver = webdriver.Firefox(options=options)
    #     driver.get("http://0.0.0.0:8080/visualizer/1/")

    #     assert driver.find_element(By.CSS_SELECTOR, ".navbar-brand").text == "Decide"

    def create_voting(self):
        q = Question(desc='test question')
        q.save()
        for i in range(5):
            opt = QuestionOption(question=q, option='option {}'.format(i+1))
            opt.save()
        v = Voting(name='test voting', question=q)
        v.save()

        a, _ = Auth.objects.get_or_create(url=settings.BASEURL,
                                          defaults={'me': True, 'name': 'test auth'})
        a.save()
        v.auths.add(a)
        return v

    def create_voters(self, v):
        for i in range(100):
            u, _ = User.objects.get_or_create(username='testvoter{}'.format(i))
            u.is_active = True
            u.save()
            c = Census(voter_id=u.id, voting_id=v.id)
            c.save()

    def get_or_create_user(self, pk):
        user, _ = User.objects.get_or_create(pk=pk)
        user.username = 'user{}'.format(pk)
        user.set_password('qwerty')
        user.save()
        return user

    def store_votes(self, v):
        voters = list(Census.objects.filter(voting_id=v.id))
        voter = voters.pop()

        clear = {}
        for opt in v.question.options.all():
            clear[opt.number] = 0
            for i in range(random.randint(0, 5)):
                a, b = self.encrypt_msg(opt.number, v)
                data = {
                    'voting': v.id,
                    'voter': voter.voter_id,
                    'vote': { 'a': a, 'b': b },
                }
                clear[opt.number] += 1
                user = self.get_or_create_user(voter.voter_id)
                self.login(user=user.username)
                voter = voters.pop()
                mods.post('store', json=data)
        return clear

    def test_visualizer_voting_in_progress(self):
        #creamos la votación 
        v = self.create_voting()
        self.create_voters(v)
        v.create_pubkey()

        #se comienza la votacion
        v.start_date = timezone.now()
        v.save()

        #Se añaden votos
        clear = self.store_votes(v)
        self.login()

        print(v.pk)
        response = self.client.put('/visualizer/'+str(v.pk), follow=True)
        self.assertEqual(response.status_code, 200)


    def test_visualizer_voting_id_negativo(self):
        response = self.client.put('/visualizer/'+str(-1), follow=True)
        self.assertEqual(response.status_code, 404)