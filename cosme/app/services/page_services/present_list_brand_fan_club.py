# services/page_services/present_list_fan_club.py

from app.drivers.driver_manager import get_driver
from app.services.page_services.present_list import PresentListPage


class PresentListBrandFanClubPage(PresentListPage):
    URL = "https://www.cosme.net/present"
    CSS_SELECTORS = [
        "div[class=psnt]>ul[class=clearfix]>li>a[href*='cosme.net/brand/brand_id']"
    ]

    def __init__(self):
        super().__init__(get_driver())

    def get_css_selectors(self):
        return self.CSS_SELECTORS

    def get_element_description(self):
        return "品牌粉丝俱乐部抽奖介绍界面的开始抽奖按钮"

    def get_url(self):
        return self.URL
