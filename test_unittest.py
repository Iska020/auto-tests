import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebSite(unittest.TestCase):

    def test_web_site_1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector(
            '.form-group.first_class input[placeholder=\'Input your first name\']')
        first_name.send_keys('John')
        last_name = browser.find_element_by_css_selector(
            '.form-group.second_class input[placeholder=\'Input your last name\']')
        last_name.send_keys('Snow')
        email = browser.find_element_by_css_selector('.form-group.third_class input[placeholder=\'Input your email\']')
        email.send_keys('test@mail.ru')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        welcome_text_elt = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'h1'))
        )

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_web_site_2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector(
            '.form-group.first_class input[placeholder=\'Input your first name\']')
        first_name.send_keys('John')
        last_name = browser.find_element_by_css_selector(
            '.form-group.second_class input[placeholder=\'Input your last name\']')
        last_name.send_keys('Snow')
        email = browser.find_element_by_css_selector('.form-group.third_class input[placeholder=\'Input your email\']')
        email.send_keys('test@mail.ru')

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
        welcome_text_elt = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'h1'))
        )

        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()