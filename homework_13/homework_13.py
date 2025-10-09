from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()
url="http://localhost:8000/dz.html"
driver.get(url)

url1="http://localhost:8000/dz_frame1.html"
driver.get(url1)
input_value1 = "Frame1_Secret"
field_frame1 = driver.find_element(By.XPATH, "//*[@id='input1']")
field_frame1.send_keys(input_value1)
check_button = driver.find_element(By.XPATH, '//*[contains(@onclick, "input1")]')
check_button.click()
alert = Alert(driver)
expected_text = "Верифікація пройшла успішно!"
if input_value1 == "Frame1_Secret":
    assert alert.text == expected_text
    print(f"Текст алерту '{alert.text}' успішно перевірено.")
else: 
    print("Текст Alert:", alert.text)
alert.accept()

url2="http://localhost:8000/dz_frame2.html"
driver.get(url2)
input_value2 = "Frame2_Secret"
field_frame2 = driver.find_element(By.XPATH, '//*[@id="input2"]')
field_frame2.send_keys(input_value2)
check_button2 = driver.find_element(By.XPATH, '//*[contains(@onclick, "input2")]')
check_button2.click()
expected_text = "Верифікація пройшла успішно!"
if input_value1 == "Frame1_Secret":
    assert alert.text == expected_text
    print(f"Текст алерту '{alert.text}' успішно перевірено.")
else: 
    print("Текст Alert:", alert.text)
alert.accept()

