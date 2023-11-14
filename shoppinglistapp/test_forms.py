# from django.test import TestCase
# from django.views.generic.edit import FormView
# from django.views.generic.edit import CreateView


# class TestItemForm(TestCase):
#     def test_name_field_is_required(self):
#         form = FormView({'name':''})
#         self.assertFalse(form.is_valid())
#         self.assertIn(form.errors.keys())
#         self.assertEqual(form.errors['name'][0], 'This field is required.')

#     def test_complete_field(self):
#         form = CreateView({'name':'Test complete item'})
#         self.assertTrue(form.is_valid())

#     def test_field_explicit_in_form_metaclass(self):
#         form = CreateView()
#         self.assertEqual(form.Meta.fields,['name', 'complete'])   
