from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_element_clickable():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dynamic_controls")

    enable_button = driver.find_element(By.CSS_SELECTOR, "#input-example button")
    enable_button.click()

    wait = WebDriverWait(driver, 10)
    input_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#input-example input")))
    input_box.send_keys("Hello QA Engineers")

    assert input_box.get_attribute("value") == "Hello QA Engineers"
