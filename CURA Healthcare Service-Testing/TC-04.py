# TC_04: Verify Login via the Menu Option


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the CURA Healthcare website
driver.get("https://katalon-demo-cura.herokuapp.com/")

# Wait until the menu icon is visible and click it
menu_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "menu-toggle")))
menu_icon.click()

# Wait for the dropdown to appear and click the "Login" option
login_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='profile.php#login']")))
login_option.click()

# Enter valid username and password
driver.find_element(By.NAME, "username").send_keys("John Doe")
driver.find_element(By.NAME, "password").send_keys("ThisIsNotAPassword")

# Click the login button
driver.find_element(By.ID, "btn-login").click()

# Wait for a few seconds to ensure login process completes
time.sleep(3)

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