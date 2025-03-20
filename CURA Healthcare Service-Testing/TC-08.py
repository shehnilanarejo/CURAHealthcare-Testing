#TC08 verifies successful logout after booking an appointment on the CURA Healthcare website.

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

    # Select "Tokyo CURA Healthcare Center"
    facility_dropdown = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "combo_facility"))
    )
    facility_dropdown.click()

    option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Tokyo CURA Healthcare Center')]"))
    )
    option.click()
    print("Successfully selected Tokyo CURA Healthcare Center!")

    # Check the "Apply for hospital readmission" checkbox if not already checked
    readmission_checkbox = driver.find_element(By.ID, "chk_hospotal_readmission")
    if not readmission_checkbox.is_selected():
        readmission_checkbox.click()

    # Select Healthcare Program (Medicare)
    driver.find_element(By.XPATH, "//label[normalize-space()='Medicare']").click()

    # Set Visit Date
    visit_date = driver.find_element(By.ID, "txt_visit_date")
    visit_date.clear()
    visit_date.send_keys("05/11/2025")

    # Add a comment
    driver.find_element(By.ID, "txt_comment").send_keys("Appointment confirmed! Hoping for a smooth check-up.")

    # Click "Book Appointment"
    driver.find_element(By.ID, "btn-book-appointment").click()

    # Wait for confirmation message
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[normalize-space()='Appointment Confirmation']"))
    )
    print("Appointment booked successfully!")

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
