# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import User

# Create your tests here.

class UserModelTest(TestCase):
    def test_string_representation(self):
        user = User(usn='1')
        self.assertEqual(str(user), user.usn)