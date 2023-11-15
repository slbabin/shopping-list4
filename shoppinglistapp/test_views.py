from django.test import TestCase
from .models import Item

class Testviews(TestCase):

    def test_display_start_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoppinglistapp/index.html')


    def test_login_page(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoppinglistapp/login.html')

    def test_register_page(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shoppinglistapp/register.html')

    def test_list_page(self):
        response = self.client.get('/shoppinglist/')
        self.assertEqual(response.status_code, 302)
  

    def test_get_edit_item_page(self):      
        item = Item.objects.create(name='Test my edit')
        response = self.client.get(f'/item-update/{item.id}')
        self.assertEqual(response.status_code, 302)
  
    
    def test_can_delete_item(self):
        item = Item.objects.create(name='Test my delete')
        response = self.client.get(f'/item-delete/{item.id}')
        self.assertRedirects(response, '/login/?next=/item-delete/1')

   
