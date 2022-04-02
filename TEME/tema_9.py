import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC


class Login(unittest.TestCase):
    LOGIN_H2 = (By.XPATH, '//*[@id="content"]/div/h2')
    ELEMENTAL_SELENIUM = (By.XPATH, '//*[@id="page-footer"]/div/div/a')
    MIDDLE_NAME_INPUT = (By.XPATH, '//input[@id="middle-name"]')
    FLASH_SUCCESS = (By.XPATH, '//*[@class="flash success"]')
    BTN_LOGIN=(By.XPATH, '//*[@id="login"]/button')

    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com')
        self.chrome.find_element(By.XPATH, '//a[contains(text(), "Form Authentication")]').click()

    def tearDown(self):
        self.chrome.quit()

    # Test1 Verificam ca noul url e corect

    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')

    # Test2 Verificam ca  page title e corect

    def test_page_title(self):
        actual = self.chrome.title
        expected = 'The Internet'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    # Test3 Verificam textul de pe elementul xpath=//h2 e corect
    def test_login_pageh2_text(self):
        actual = self.chrome.find_element(*self.LOGIN_H2).text
        expected = 'Login Page'
        self.assertEqual(expected, actual, 'Login Page text is incorrect')

    # Test4 Verificam ca butonul de login este displayed
    def test_elem_displayed(self):
        btn_login = self.chrome.find_elements(*self.BTN_LOGIN)
        self.assertTrue(len(btn_login) == 1, 'The login button is not visible')

    # Test5 Verificam ca atributul href al linkului ‘Elemental Selenium’ e corect
    def test_elem_atribute(self):
        actual = self.chrome.find_element(*self.ELEMENTAL_SELENIUM).get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(expected, actual, 'Elemental Selenium href attribute is wrong!')

    # Test6 Lasam goale user si pass Click login Verificam ca eroarea e displayed
    def test_error_displayed(self):
        self.chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        error = self.chrome.find_element(By.ID, 'flash')
        self.assertTrue(error.is_displayed(), 'Eroarea nu este afisata!')

    # Test7 Completeaza cu user si pass invalide Click login Verifica ca mesajul de pe eroare e corect
    def test_invalide_displayed(self):
        self.chrome.find_element(By.ID, 'username').send_keys('Ionica')
        self.chrome.find_element(By.ID, 'password').send_keys('*****')
        self.chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        error = self.chrome.find_element(By.ID, 'flash').text
        self.assertTrue('Your username is invalid!' in error, 'Eroarea e vizibila in mod incorect!')

    # Test8 Lasam goale user si pass Click login Apasam x la eroare Verificam ca eroarea a disparut
    def test_closeerror_correct(self):
        self.chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        close_error = self.chrome.find_element(By.XPATH, '//*[@id="flash"]/a')
        close_error.click()
        try:
            self.chrome.find_element(By.XPATH, '//*[@id="flash"]')
        except NoSuchElementException:
            pass

    # Test9 Ia ca o lista toate //label VerificaM textul ca textul de pe ele sa fie cel asteptat (Username si Password) Aici e ok sa avem 2 asserturi
    def test_userandpass(self):
        label_list = self.chrome.find_elements(By.TAG_NAME, 'label')
        self.assertEqual(label_list[0].text, 'Username', 'error')
        self.assertEqual(label_list[1].text, 'Password', 'error')

    # Test10
    # Completeaza cu user si pass valide
    # Click 0
    # Verifica ca noul url CONTINE /secure
    # Foloseste un explicit wait pentru elementul cu clasa ’flash succes’
    # Verifica ca elementul cu clasa=’flash succes’ este displayed
    # Verifica ca mesajul de pe acest element CONTINE textul ‘secure area!’

    def test_loginpage(self):
        self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
        self.chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        actual = self.chrome.current_url
        self.assertTrue('secure' in actual, 'Secure  is not present in URL')
        # elem gasit
        WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@class="flash success"]')))
        elem = self.chrome.find_element(*self.FLASH_SUCCESS)
        self.assertTrue(elem.is_displayed(), 'FLASH SUCCESS is not displayed!')
        self.assertTrue('secure area' in elem.text, 'mesajul de pe text nu contine secure area')

        # Test11
        # Completeaza cu user si pass valide
        # Click login
        # Click logout
        # Verifica ca ai ajuns pe https://the-internet.herokuapp.com/login

    def test_verificareURL(self):
        self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
        self.chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
        self.chrome.find_element(By.XPATH, '//*[@id="content"]/div/a').click()
        actual = WebDriverWait(self.chrome, 5).until(EC.url_changes('https://the-internet.herokuapp.com/secure'))
        # WebDriverWait(self.chrome, 5).until(EC.url_contains('/login')) initial am facut asa fara assert si testul a trecut
        expected = WebDriverWait(self.chrome, 5).until(EC.url_to_be('https://the-internet.herokuapp.com/login'))
        self.assertEqual(expected, actual, 'URL is incorrect')

    # Test12 - brute force password hacking
    # Completeaza user tomsmith
    # Gaseste elementul // h4 si ia  tot textul de pe el
    # Ia textul de pe el si fa split dupa spatiu.
    # Considera fiecare cuvant  ca o potentiala parola
    # Foloseste  o  structura iterativa prin care sa introduci rand pe rand parolele  si sa apesi pe login
    # La final  testul  trebuie sa imi printeze fie
    # ‘Nu   am  reusit  sa gasesc parola’
    # ‘Parola secreta este[parola]’

    def test_pass_hacking(self):
        elem_h = self.chrome.find_element(By.XPATH, '//*[@id="content"]/div/h4').text
        elem_h_list=elem_h.split()
        print(elem_h_list)
        for element in elem_h_list:
            self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')
            self.chrome.find_element(By.ID, 'password').send_keys(element)
            self.chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
            actual = self.chrome.current_url
            if 'secure' in actual:
                print(f'Parola secreta este {element}')
                break
            else:
                print('Nu   am  reusit  sa gasesc parola')





