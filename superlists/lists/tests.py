from django.http.response import HttpResponse
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
from lists.models import Item
# Create your tests here.
class HomePageTest(TestCase):
  def test_root_url_resolves_home_page(self):
    found = resolve('/')
    self.assertEqual(found.func, home_page)
  
  def test_home_page_returns_correct_html(self):
    response = self.client.get('/')
    self.assertTemplateUsed(response, "home.html")
  
  def test_can_save_a_POST_request(self):
    response = self.client.post('/', data={"item_text": "A todo item"})
    self.assertIn("A todo item", response.content.decode())
    self.assertTemplateUsed(response, "home.html")

class ItemModelTest(TestCase):
  def test_saving_and_retrieving_data(self):
    first_text = "The first list item"
    second_text = "Second item"

    first_item = Item()
    first_item.text = first_text
    first_item.save()
    
    second_item = Item()
    second_item.text = second_text
    second_item.save()

    saved_items = Item.objects.all()
    self.assertEqual(saved_items.count(), 2)
    first_saved_item = saved_items[0]
    second_saved_item = saved_items[1]
    self.assertEqual(first_saved_item.text, first_text)
    self.assertEqual(second_saved_item.text, second_text)