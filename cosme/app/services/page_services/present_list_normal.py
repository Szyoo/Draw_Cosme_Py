# services/page_services/present_list_normal.py

from app.drivers.driver_manager import get_driver
from app.services.page_services.present_list import PresentListPage


class PresentListNormalPage(PresentListPage):
    URL = "https://www.cosme.net/present"
    CSS_SELECTORS = [
        "a[href*='present/detail/present_id']",
        "a[href*='/as.iy.impact-ad.jp/ct?id=']"
    ]

    def __init__(self):
        super().__init__(get_driver())

    def get_css_selectors(self):
        return self.CSS_SELECTORS

    def get_element_description(self):
        return "抽奖介绍界面的开始抽奖按钮"

    def get_url(self):
        return self.URL
