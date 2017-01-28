# -*- coding: utf-8 -*-
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def remove_item(self):
        item = self.driver.find_element_by_css_selector(
            'td.item'
        )
        self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'button[value=\'Remove\']')
        ))
        self.driver.find_element_by_css_selector(
            'button[value=\'Remove\']'
        ).click()
        self.wait.until(EC.staleness_of(item))
