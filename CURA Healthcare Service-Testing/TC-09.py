#TC09 Logout without booking appointment

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

try:
    # Open the CURA Healthcare website
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # Click on "Make Appointment"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-make-appointment"))).click()

    # Enter username and password
    driver.find_element(By.NAME, "username").send_keys("John Doe")
    driver.find_element(By.NAME, "password").send_keys("ThisIsNotAPassword")

    # Click Login button
    driver.find_element(By.ID, "btn-login").click()

    # Wait for login to complete
    WebDriverWait(driver, 10).until(EC.title_contains("CURA Healthcare Service"))
    print("Successfully logged in!")

    # Open the menu
    menu_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "menu-toggle")))
    menu_icon.click()

    # Click Logout
    logout_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
    )
    logout_option.click()

    print("Logout Successfully!")

finally:
    # Close the browser
    driver.quit()
