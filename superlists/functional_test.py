from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

PATH="C:\Program Files (x86)\chromedriver.exe"


class NewVisitorTest(unittest.TestCase):
  def setUp(self) -> None:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    self.browser = webdriver.Chrome(executable_path=PATH, options=options)
  def tearDown(self) -> None:
    self.browser.quit()
  def check_for_row_in_list_table(self, row_text):
    table = self.browser.find_element_by_id("id_list_table")
    rows = table.find_elements_by_tag_name("tr")
    self.assertIn(row_text, [row.text for row in rows])  

  def test_can_start_a_list_and_retrieve_it_later(self):
    # John listen about new cool to-do app. He goes 
    # to check page
    self.browser.get('http://localhost:8000')

    # She notices the page title and header mention to-do lists
    self.assertIn("To-Do", self.browser.title)
    header_text = self.browser.find_element_by_tag_name('h1').text
    self.assertIn("To-Do", header_text)
    # He is invited to enter a to-do item straight away
    inputbox = self.browser.find_element_by_id('id_new_item')

    # He types "Buy peacock feathers" to text box (John's hobby
    # is tying fly-fishing lures)
    inputbox.send_keys("Buy peacock feathers")

    # He press enter and page lists updated
    # "1: Buy peacock feathers" as an item in a to-do list table
    inputbox.send_keys(Keys.ENTER)
    time.sleep(2)
    
    self.check_for_row_in_list_table("1: Buy peacock feathers")

    # There is still text box inviting her to another item
    # He enters Use peacock feathers to make a fly" (Edith is very
    # methodical)
    inputbox = self.browser.find_element_by_id('id_new_item')
    inputbox.send_keys('Use peacock feathers to make a fly')
    inputbox.send_keys(Keys.ENTER)
    time.sleep(2)

    self.check_for_row_in_list_table('1: Buy peacock feathers')
    self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

    self.fail("Finish the test")
  
if __name__ == "__main__":
  unittest.main(warnings="ignore")