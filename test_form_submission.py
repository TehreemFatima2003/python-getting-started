from selenium import webdriver
from selenium.webdriver.common.by import By
def test_form_submission_success():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
driver.get("https://www.selenium.dev/selenium/web/web-form.html")    driver.find_element(By.NAME, "username").send_keys("testuser")
    driver.find_element(By.NAME, "password").send_keys("securepassword")
    driver.find_element(By.TAG_NAME, "button").click()
    success_message = driver.find_element(By.ID, "success-message").text
    assert success_message == "Form submitted successfully!"
    driver.quit()
