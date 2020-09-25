from django.test import TestCase

from django.contrib.auth import get_user_model
from .models import CustomUser
from django.urls import reverse, reverse_lazy
class TestLoginView(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='majd',
            email='majdkilany@gmail.com',
            password='password'
        )

        self.user2 = get_user_model().objects.create_user(
            username='majd',
            email='majdkilany.com',
            password='password'
        )

    def test_the_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code,200)