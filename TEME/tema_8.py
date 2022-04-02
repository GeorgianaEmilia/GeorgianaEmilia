from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

'''https://www.phptravels.net/
http://automationpractice.com/index.php
https://formy-project.herokuapp.com/
https://the-internet.herokuapp.com/
https://www.techlistic.com/p/selenium-practice-form.html
jules.app

(obs: nu 3 pe fiecare pagina, 3 in total, de pe ce site doriti, la alegere. Nu toate sites vor avea elemente cu atributul name de ex)

3 selectors by:
Id
Link text
Partial link text
Name
Tag*
Class name*
Css (1 dupa id, 1 dupa clasa, 1 dupa atribut=valoare_partiala)

*La tag si class name veti folosi find elementS! - salvati in lista. Interactionati cu un element la alegere din lista

La Xpath:
3 dupa atribut valoare
3 dupa textul de pe element
1 dupa partial text
1 cu SAU, folosind pipe |
1 cu *
1 in care le iei ca pe o lista de xpath si in python ajunge 1 element, deci cu (xpath)[1]
1 in care sa folosesti parent::
1 in care sa folosesti fratele anterior sau de dupa (la alegere)
1 functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez.
'''

# 3 selectors by Id

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
#
# chrome.maximize_window()
# chrome.get('https://www.phptravels.net/')
# #close_cookie
# cookie_stop=chrome.find_element(By.ID,'cookie_stop')
# cookie_stop.click()
# # selector by ID
# languages = chrome.find_element(By.ID, 'languages')
# languages.click()
# currency=chrome.find_element(By.ID, 'currency')
# currency.click()
# input_email = chrome.find_element(By.ID, 'exampleInputEmail1')
# input_email.send_keys('cgeorgianaemilia@gmail.com')
# sleep(6)
# chrome.quit()

# 3 selectors by Link Text

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/')
#
# # selector by Link Text
#
# chrome.find_element(By.LINK_TEXT,'Drag and Drop').click()
# chrome.find_element(By.LINK_TEXT,'Complete Web Form').click()
# chrome.find_element(By.LINK_TEXT,'Key and Mouse Press').click()
# sleep(3)
# chrome.quit()

# 3 selectors by Partial link text

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/')
#
# chrome.find_element(By.PARTIAL_LINK_TEXT,'Upload').click()
# chrome.find_element(By.PARTIAL_LINK_TEXT,'Window').click()
# chrome.find_element(By.PARTIAL_LINK_TEXT,'Web').click()
# sleep(3)
# chrome.quit()

# 3 selectors by Name

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
#
# # selector by Name
# firstname = chrome.find_element(By.NAME, 'firstname').send_keys('Emi')
# lastname = chrome.find_element(By.NAME, 'lastname').send_keys('Ciontic')
#
# sleep(3)
# chrome.quit()

# 3 selectors by TAG

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# sleep(2)
# cookie_stop=chrome.find_element(By.ID,'ez-accept-all')
# cookie_stop.click()
# input_list = chrome.find_elements(By.TAG_NAME, 'input')
# input_list[0].send_keys('Emi')
# input_list[1].send_keys('Georgiana')
# input_list[2].click()
# input_list[4].click()
# chrome.find_element(By.TAG_NAME, 'select').click()
# sleep(3)
# chrome.quit()

# 3 selectors by class name

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('http://automationpractice.com/index.php')
# sleep(3)
#
# chrome.find_element(By.CLASS_NAME, 'newsletter-input').send_keys('cge@gmail.com')
# chrome.find_elements(By.CLASS_NAME, 'button-small')[1].click()
# chrome.find_element(By.CLASS_NAME, 'item-img').click()
# sleep(3)
# chrome.quit()

# 3 selectors by Css (1 dupa id, 1 dupa clasa, 1 dupa atribut=valoare_partiala)

# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://www.techlistic.com/p/selenium-practice-form.html')
# sleep(2)
# cookie_stop=chrome.find_element(By.ID,'ez-accept-all')
# cookie_stop.click()
# chrome.find_element(By.CSS_SELECTOR, '#submit').click()
# sleep(3)
# chrome.quit()

# alt url CSS CLASA
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://www.phptravels.net/')
# cookie_stop=chrome.find_element(By.ID,'cookie_stop')
# cookie_stop.click()
# chrome.find_element(By.CSS_SELECTOR, '.logo').click()
# chrome.find_element(By.CSS_SELECTOR, 'div input[placeholder*="Enter your email"]').send_keys('TESTARE')
#
# sleep(3)
# chrome.quit()

# La Xpath:
#3 dupa atribut valoare
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/autocomplete')
# chrome.find_element(By.XPATH, '//*[@id="autocomplete"]').send_keys('Bucuresti')
# chrome.find_element(By.XPATH, '//*[@id="locality"]').send_keys('Bucuresti')
# chrome.find_element(By.XPATH, '//*[@id="country"]').send_keys('Romania')
# sleep(3)
# chrome.quit()

#3 dupa textul de pe element
# s = Service(ChromeDriverManager().install())
# chrome = webdriver.Chrome(service=s)
# chrome.maximize_window()
# chrome.get('https://formy-project.herokuapp.com/buttons')
# full_text = chrome.find_element(By.XPATH, '//button[contains(text(), "Success")]').text
# full_text1 = chrome.find_element(By.XPATH, '//button[contains(text(), "Danger")]').text
# full_text2 = chrome.find_element(By.XPATH, '//button[contains(text(), "Middle")]').text
# full_text3 = chrome.find_element(By.XPATH, '//button[contains(text(), "Prim")]').text #1 dupa partial text
# print(full_text)
# print(full_text1)
# print(full_text2)
# print(full_text3) #1 dupa partial text
#
# # 1 cu SAU, folosind pipe |
# s = chrome.find_element(By.XPATH, '//button[contains(text(), "Test1")] | //button[contains(text(), "Left")] | //button[contains(text(), "TEST2")]').text
# print(s)
# sleep(3)
# chrome.quit()

# 1 cu *
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()
chrome.get('https://formy-project.herokuapp.com/form')
chrome.find_element(By.XPATH, '//*[contains(@placeholder, "Enter")]').send_keys('your email')
# 1 in care le iei ca pe o lista de xpath si in python ajunge 1 element, deci cu (xpath)[1]
chrome.find_element(By.XPATH, '(//input[@class="form-control"])[4]').send_keys('S')

# 1 in care sa folosesti parent::
parent=chrome.find_element(By.XPATH,'//label[contains(text(), "First name")]/parent::strong').text
print(parent)
# 1 in care sa folosesti fratele anterior sau de dupa (la alegere)
bro1=chrome.find_element(By.XPATH,'//label[contains(text(), "First name")]/parent::strong/following-sibling::input').send_keys('bro')



# 1 functie ca si cea de la clasa prin care sa pot alege eu prin param cu ce element vreau sa interactionez.
def formy_input(placeholder_text, input_value):
    input = chrome.find_element(By.XPATH, f'//input[@placeholder="{placeholder_text}"]')
    input.clear()
    input.send_keys(input_value)

formy_input('Enter your job title','Automation Tester')
sleep(3)
chrome.quit()