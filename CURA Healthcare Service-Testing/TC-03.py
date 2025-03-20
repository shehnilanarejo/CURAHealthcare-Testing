# TC_03: Verify login with empty fields.

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the CURA Healthcare website
driver.get("https://katalon-demo-cura.herokuapp.com/")

# Click on the "Make Appointment" button
driver.find_element(By.ID, "btn-make-appointment").click()

# Enter valid username and password
driver.find_element(By.NAME, "username").send_keys("")
driver.find_element(By.NAME, "password").send_keys("")

# Click the login button
driver.find_element(By.ID, "btn-login").click()

# Wait for a few seconds to ensure login process completes
time.sleep(3)

#verify error message
err_msg = driver.find_element(By.XPATH, "//*[@class='lead text-danger']").text
exp_msg = "Login failed! Please ensure the username and password are valid."

if err_msg == exp_msg:
    print("Successfully logged in")
else:
    print("Failed to log in")
driver.quit()

# Validate the login by checking the page title
act_title = driver.title
exp_title = "CURA Healthcare Service"

# Check if login was successful
if act_title == exp_title:
    print("Successfully logged in")
else:
    print("Failed to log in")

# Close the browser
driver.quit()