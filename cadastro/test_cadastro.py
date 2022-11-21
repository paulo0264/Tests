from django.test import Client, TestCase
from django.urls import reverse

class TestCadastroConversion(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse("cadastro:convert")

    