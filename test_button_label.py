from selenium import webdriver
from selenium.webdriver.common.by import By
def test_button_text():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
   driver.get("https://www.selenium.dev/selenium/web/web-form.html")    button = driver.find_element(By.ID, "submit-button")
    assert button.text == "Submit"
    driver.quit()
