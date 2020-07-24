# Open https://the-internet.herokuapp.com/login

# Please automate next test cases:

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
driver = webdriver.Chrome(executable_path="c:/selenium/chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/login")

# 1. Login with valid creds (tomsmith/SuperSecretPassword!) and assert you successfully logged in
driver.find_element_by_id("username").send_keys("tomsmith");
driver.find_element_by_id("password").send_keys("SuperSecretPassword!");
driver.find_element_by_class_name("fa, fa-2x, fa-sign-in").click();
alertMessage = driver.find_element_by_id("flash").text
assert "You logged into a secure area!" in alertMessage

# 3. Logout from app and assert you successfully logged out
driver.find_element_by_partial_link_text("Logout").click()
alertMessage = driver.find_element_by_id("flash").text
assert "You logged out of the secure area!" in alertMessage

# 2. Login with invalid creds and check validation error
driver.find_element_by_id("username").send_keys("dima");
driver.find_element_by_id("password").send_keys("amid1516");
driver.find_element_by_class_name("fa, fa-2x, fa-sign-in").click();
alertMessage = driver.find_element_by_id("flash").text
assert "Your username is invalid!" in alertMessage












