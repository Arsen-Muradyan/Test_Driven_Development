from django.http.response import HttpResponse
from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
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