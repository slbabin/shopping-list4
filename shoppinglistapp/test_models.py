from django.test import TestCase
from .models import Item


class TestModel(TestCase):
    def test_complete_defaults_false(self):
        item = Item.objects.create(name='Test item')
        self.assertFalse(item.complete)