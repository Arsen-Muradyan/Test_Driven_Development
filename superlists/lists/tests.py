from django.http import response
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

  def test_only_saves_items_when_necessary(self):
    self.client.get('/')
    self.assertEqual(Item.objects.count(), 0)

  def test_can_save_a_POST_request(self):
    response = self.client.post('/', data={'item_text': 'A new list item'})
    self.assertEqual(Item.objects.count(), 1)
    new_item = Item.objects.first()
    self.assertEqual(new_item.text, 'A new list item')
    
  def test_can_redirect_after_POST(self):
    response = self.client.post('/', data={'item_text': 'A new list item'})
    self.assertEqual(response.status_code, 302)
    self.assertEqual(response['location'], '/')
  def test_showing_multpile_items_in_table(self):
    Item.objects.create(text="Item one")
    Item.objects.create(text="Item two")

    response = self.client.get('/')
    self.assertIn("Item one", response.content.decode())
    self.assertIn("Item two", response.content.decode())

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