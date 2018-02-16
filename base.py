#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 20:44:15 2017

@author: ronaldo
"""

from contextlib import contextmanager

# Exceptions
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec
# WAIT AND CONDITIONS METHODS
from selenium.webdriver.support.ui import WebDriverWait


class Page(object):
    """Page Class Object with common navigation functions"""

    timeout = 30

    def __init__(self, driver):
        # noinspection SpellCheckingInspection
        """ Initializes the webdriver and the timeout"""
        # if type(driver) != type(webdriver):
        #     raise TypeError("The object {0} must be of type{1}".format(driver,
        #                     type(webdriver)))
        self.driver = driver

    def __enter__(self):
        """ Implementation class """
        return self

    def close(self):
        """ Basic implementation class"""
        self.driver.close()

    @contextmanager
    def wait_for_page_load(self):
        """ Only used when navigating between Pages with different titles"""
        old_page = self.driver.find_element_by_tag_name('title')
        yield
        WebDriverWait(self.driver, self.timeout).until(
            ec.staleness_of(old_page))

    def alert_is_present(self, timeout=5):

        try:

            alert = WebDriverWait(self.driver, timeout).until(
                ec.alert_is_present())

        except (TimeoutException, WebDriverException):

            return False

        return alert

    def elem_is_visible(self, *locator, timeout=timeout):
        """
        Check is locator is visible on page given the timeout

        Args: Instance of object and a locator defined on locators module

        Return: True if locator is visible, False o.w.
        """
        try:

            WebDriverWait(self.driver, timeout).until(
                ec.visibility_of_element_located(*locator))
        except TimeoutException:
            return False

        return True

    def find_element(self, *locator):
        return self.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url()

    def hover(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def check_element_exists(self, *locator):
        try:
            self.wait_for_element(*locator)
        except TimeoutException:
            return False
        return True

    def wait_for_element_to_be_visible(self, *locator, timeout=timeout):
        return WebDriverWait(self.driver, timeout).until(
            ec.visibility_of_element_located(*locator))

    def wait_for_element(self, *locator, timeout=timeout):
        return WebDriverWait(self.driver, timeout).until(
            ec.presence_of_element_located(*locator))

    def wait_for_element_to_click(self, *locator, timeout=timeout):
        return WebDriverWait(self.driver, timeout).until(
            ec.element_to_be_clickable(*locator))

    def wait_for_new_window(self, timeout=timeout):
        return WebDriverWait(self.driver, timeout).until(
            ec.number_of_windows_to_be(2))