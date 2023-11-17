# app/services/page_services/base.py

from app.utils import selenium_utils
from app.exceptions.exceptions import ElementNotFoundException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import WebDriverException


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by: By, selector: str, description: str, parent: WebElement = None):
        """
        根据 CSS/XPATH 选择器查找元素。
        """
        try:
            if parent:
                element = parent.find_element(by, selector)
            else:
                element = selenium_utils.find(by, selector)
            return element
        except WebDriverException:
            ElementNotFoundException(f"未找到元素: {description}").__str__()
            return None  # 返回 None 以表示没有找到元素

    def find_elements(self, by: By, selector: str, description: str, parent: WebElement = None):
        """
        根据 CSS/XPATH 选择器查找多个元素。
        """
        try:
            if parent:
                elements = parent.find_elements(by, selector)
            else:
                elements = selenium_utils.find_elements(by, selector)
            return elements
        except WebDriverException:
            ElementNotFoundException(f"未找到任意元素: {description}").__str__()
            return None  # 返回 None 以表示没有找到元素

    def find_element_by_multiple_selectors(self, by: By, selectors: list, description: str, parent: WebElement = None):
        """
        根据多个 CSS/XPATH 选择器查找元素。
        """
        for selector in selectors:
            try:
                element = self.find_element(by, selector, description, parent)
                if element:
                    return element
            except WebDriverException:
                ElementNotFoundException(f"未找到元素: {description}").__str__()
                return None  # 返回 None 以表示没有找到元素

        ElementNotFoundException(f"未找到元素: {description}").__str__()

    def find_elements_by_multiple_selectors(self, by: By, selectors: list, description: str, parent: WebElement = None):
        """
        根据多个 CSS/XPATH 选择器查找多个元素。
        """
        all_elements = []
        for selector in selectors:
            try:
                elements = self.find_elements(by, selector, description, parent)
                if elements:
                    all_elements.extend(elements)
            except WebDriverException:
                ElementNotFoundException(f"未找到任意元素: {description}").__str__()

        if not all_elements:
            ElementNotFoundException(f"未找到任意元素: {description}").__str__()
            return None  # 返回 None 以表示没有找到元素

        return all_elements
