from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

def check_exists_by_id(id):
    try:
        search_box = browser.find_element_by_id(id)
        search_box.send_keys('Тензор')
    except NoSuchElementException:
        return False
    return True

try:
    link = "http://yandex.ru"
    browser = webdriver.Chrome()
    browser.get(link)

    check_exists_by_id('text')

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()