# services/page_services/present_list.py

from typing import List
from app.utils import selenium_utils
from app.services.page_services.base import BasePage
from app.models.present import PresentBase
from app.exceptions.exceptions import ElementNotFoundException

class PresentListPage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def url(self) -> str:
        """
        抽象属性，由子类实现，提供页面链接。
        """
        raise NotImplementedError

    @property
    def css_selectors(self) -> List[str]:
        """
        抽象属性，由子类实现，提供 CSS 选择器。
        """
        raise NotImplementedError

    @property
    def element_description(self) -> str:
        """
        抽象属性，由子类实现，提供元素描述。
        """
        raise NotImplementedError

    def get_presents(self):
        """
        根据 CSS 选择器从页面中获取奖品列表。
        """
        elements = self.find_elements_by_multiple_selectors(self.css_selectors, self.element_description)
        presents = []
        for element in elements:
            text = element.text.strip()
            if not text:
                try:
                    title_element = self.find_child_element(element, ".psnt-ttl", "奖品名称")
                    text = title_element.text.strip()
                except ElementNotFoundException:
                    continue
            if text:
                href = element.get_attribute("href")
                # Assuming brand_name and img_link can be fetched similarly
                brand_name = "Extracted brand name here"  # Add extraction logic
                img_link = "Extracted img link here"     # Add extraction logic
                present = PresentBase(link=href, present_name=text, brand_name=brand_name, img_link=img_link)
                presents.append(present)
        return presents
