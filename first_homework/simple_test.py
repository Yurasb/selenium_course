# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver


@pytest.fixture(scope='session')
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_first_homework(driver):
    driver.get('http://software-testing.ru/')
