#TC07 Verify booking with only selecting the date, the comment

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Open the CURA Healthcare website
driver.get("https://katalon-demo-cura.herokuapp.com/")

# Click on the "Make Appointment" button
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-make-appointment"))).click()

# Enter valid username and password
driver.find_element(By.NAME, "username").send_keys("John Doe")
driver.find_element(By.NAME, "password").send_keys("ThisIsNotAPassword")

# Click the login button
driver.find_element(By.ID, "btn-login").click()

# Validate login by checking if the appointment page is loaded
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "appointment")))
print("Successfully logged in!")

# Enter Visit Date
visit_date = driver.find_element(By.ID, "txt_visit_date")
visit_date.clear()
visit_date.send_keys("05/11/2025")
print("Visit Date Set: 05/11/2025")


# Click "Book Appointment"
driver.find_element(By.ID, "btn-book-appointment").click()

# Wait for confirmation page
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "col-xs-12")))

# Close the browser
driver.quit()
