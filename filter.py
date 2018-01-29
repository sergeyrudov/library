from selenium import webdriver
import time
import selenium.common.exceptions

f = webdriver.Firefox()
time.sleep(3)
f.get("http://google.com")
