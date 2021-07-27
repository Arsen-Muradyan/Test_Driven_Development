from selenium import webdriver

PATH="C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome(executable_path=PATH, options=options)
browser.get("http://localhost:8000")

assert 'To Do' in browser.title, "Browser title was " + browser.title

browser.quit()