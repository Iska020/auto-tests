from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def func(a):
  return math.log(abs(12*math.sin(a)))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )

    book = browser.find_element_by_id("book")
    book.click()

    x = browser.find_element_by_id('input_value')
    x = x.text

    result = func(int(x))

    answer = browser.find_element_by_id('answer')
    answer.send_keys(str(result))

    submit = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, 'solve'))
    )
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()