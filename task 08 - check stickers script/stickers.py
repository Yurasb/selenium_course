# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver(request):
    wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_stickers(driver):
    driver.get('http://localhost/litecart/en/')
    ducks = driver.find_elements_by_css_selector('li.product')
    for duck in ducks:
        sticker = duck.find_elements_by_css_selector('div.sticker')
        assert len(sticker) == 1
