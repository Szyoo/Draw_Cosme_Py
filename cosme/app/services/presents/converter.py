# service.presents.converter.py

from app.models.present import Present
from app.utils import selenium_utils
from selenium.webdriver.remote.webelement import WebElement


class Converter:

    @staticmethod
    def extract_present(element: WebElement) -> Present:
        """
        从WebElement中提取礼物信息。
        :param element: WebElement对象
        :return: Present的临时对象，只包括link和present_name

        使用案例：
            present_obj = Converter.extract_present(element)
        """
        link = selenium_utils.extract_url(element)
        present_name = selenium_utils.extract_name(element)

        return Present(link=link, present_name=present_name)
