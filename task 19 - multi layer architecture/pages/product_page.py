# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self):
        self.driver.find_element_by_css_selector(
            'button[value=\'Add To Cart\']'
        ).click()
        self.wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, 'quantity'), '1'
        ))
        return self

    def go_to_checkout(self):
        self.driver.find_element_by_css_selector(
            'a.link[href=\'http://localhost/litecart/en/checkout\']'
        ).click()
