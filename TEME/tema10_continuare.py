import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
'''
Ganditi voi o clasa de test din paginile sugerate in tema 8 (ce doriti voi, cate functii de
test doriti, freestyle ca sa incepeti sa ganditi si singuri niste scenarii de test). Folositi firefox in loc de chrome
'''

class Login(unittest.TestCase):
    FIRST_ITEM=(By.CSS_SELECTOR,'#homefeatured > li:nth-child(1)')
    SECOND_ITEM=(By.CSS_SELECTOR,'#homefeatured > li:nth-child(2)')
    skip_step = False

    def setUp(self):
        self.firefox = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        self.firefox.maximize_window()
        self.firefox.get('http://automationpractice.com/index.php')

    def tearDown(self):
        self.firefox.quit()

    #test1 verify the new url

    def test_url(self):
        button_cart=self.firefox.find_element(By.CSS_SELECTOR, 'a[title="View my shopping cart"]')
        button_cart.click()
        actual = self.firefox.current_url
        expected = 'http://automationpractice.com/index.php?controller=order'
        self.assertEqual(expected, actual, 'URL is incorrect')

    #test2-insert item in cart, verify cart message

    def test_cart(self):
        first_item=self.firefox.find_element(*self.FIRST_ITEM)
        hover = ActionChains(self.firefox).move_to_element(first_item)
        hover.perform()
        btn_cart=self.firefox.find_element(By.CSS_SELECTOR, 'a[title="Add to cart"]')
        btn_cart.click()
        sleep(2)
        actual= self.firefox.find_element(By.XPATH,'/html/body/div/div[1]/header/div[3]/div/div/div[4]/div[1]/div[2]/h2/span[2]').text
        expected='There is 1 item in your cart.'
        self.assertEqual(expected, actual, 'Cart message is incorrect')

    #test3- verify price from product description  with price from cart

    def test_price_cart(self):
        if self.skip_step == False:
            self.test_cart()
        total_products=self.firefox.find_element(By.CLASS_NAME,'ajax_block_products_total').text
        total_shipping=self.firefox.find_elements(By.CLASS_NAME,'ajax_cart_shipping_cost')[1].text
        total_shop=self.firefox.find_elements(By.CLASS_NAME,'ajax_block_cart_total')[1].text
        proceed_checkout=self.firefox.find_element(By.CSS_SELECTOR, 'a[title="Proceed to checkout"]')
        proceed_checkout.click()
        self.assertEqual(self.firefox.find_element(By.ID, 'total_product').text, total_products, 'The price doesn`t match')
        self.assertEqual(self.firefox.find_element(By.ID, 'total_shipping').text, total_shipping, 'The price doesn`t match')
        self.assertEqual(self.firefox.find_element(By.ID, 'total_price_without_tax').text, total_shop, 'The price doesn`t match')

    #test4 addmore products in cart and compare price on the description product with price from cart
    def test_moreproduct(self):
        self.test_cart()
        continue_shop=self.firefox.find_element(By.CSS_SELECTOR, 'span[title="Continue shopping"]')
        continue_shop.click()
        second_item = self.firefox.find_element(*self.SECOND_ITEM)
        hover1 = ActionChains(self.firefox).move_to_element(second_item)
        hover1.perform()
        sleep(2)
        add_newproduct = self.firefox.find_elements(By.CSS_SELECTOR, 'a[title="Add to cart"]')[1]
        add_newproduct.click()
        sleep(2)
        self.skip_step = True
        self.test_price_cart()




