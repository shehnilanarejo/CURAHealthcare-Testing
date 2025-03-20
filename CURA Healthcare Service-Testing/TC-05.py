#TC_05:Ensure users can successfully book an appointment by selecting all required options and confirming the booking.

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the CURA Healthcare website
driver.get("https://katalon-demo-cura.herokuapp.com/")

# Click on the "Make Appointment" button
driver.find_element(By.ID, "btn-make-appointment").click()

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

# Wait for and click the facility dropdown
facility_dropdown = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "col-sm-offset-3"))
)
facility_dropdown.click()  # Open the dropdown

# Wait for the option and click it
option = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Tokyo CURA Healthcare Center')]"))
)
option.click()
print("Successfully selected Tokyo CURA Healthcare Center!")

#Verify is  Apply for hospital readmission  box is checkbox
readmission_checkbox = driver.find_element(By.XPATH, "//label[@for='chk_hospotal_readmission']")
if not readmission_checkbox.is_selected():
    readmission_checkbox.click()

# Selecting "Medicare" as the Healthcare Program
driver.find_element(By.XPATH, "//label[normalize-space()='Medicare']").click()

# Setting the visit date
visit_date = driver.find_element(By.XPATH, "//input[@id='txt_visit_date']")
visit_date.clear()
visit_date.send_keys('05/11/2025')

# Adding a comment
driver.find_element(By.ID, 'txt_comment').send_keys('Appointment confirmed! Hoping for a smooth and quick check-up')

# Clicking the "Book Appointment" button
driver.find_element(By.ID, 'btn-book-appointment').click()
time.sleep(3)  # Wait for the booking process

# Wait for confirmation page
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "col-xs-12")))

# Verify successful booking
confirmation_message = driver.find_element(By.XPATH, "//h2[normalize-space()='Appointment Confirmation']").text
if "Appointment Confirmation" in confirmation_message:
    print("Appointment booked successfully!")

# Close the browser
driver.quit()