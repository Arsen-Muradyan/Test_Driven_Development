from selenium import webdriver
import unittest

PATH="C:\Program Files (x86)\chromedriver.exe"


class NewVisitorTest(unittest.TestCase):
  def setUp(self) -> None:
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    self.browser = webdriver.Chrome(executable_path=PATH, options=options)
  def tearDown(self) -> None:
    self.browser.quit()
  def test_can_start_a_list_and_retrieve_it_later(self):
    # John listen about new cool to-do app. He goes 
    # to check page
    self.browser.get('http://localhost:8000')

    # She notices the page title
    self.assertIn("To-Do", self.browser.title)
    self.fail("Finish the test")
  
if __name__ == "__main__":
  unittest.main(warnings="ignore")