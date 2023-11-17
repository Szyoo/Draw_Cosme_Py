# services/page_services/info.py

from app.drivers.driver_manager import get_driver
from app.services.page_services.base import BasePage
from selenium.webdriver.common.by import By


class InfoPage(BasePage):

    URL_INFO_PAGE_A = [
        "div.block-info>div.inner>div.box-present>div.col-wrap div.col>div.txtset div.btn a.gatrack",
        "div.block-info + div.box-image>a.gatrack",
        "div.bg-area div.present li.btn-cosme>a.gatrack",
        "#main>#section>.content>.apply>input.btn-green",
        "#presentInfo>div.detail>p.apply>a",
        "#brd-psnt>div.brd-psnt-frm>div.brd-psnt-frm-inr>a"
    ]

    URL_INFO_PAGE_IMG = [
        "div.block-info>div.inner>div.box-present>div.col-wrap div.col>p img[src]",
        "div.box-image>div.clearfix>div.fl-none>img",
        "div.bg-area div.present>img",
        "#main>#section>.photo>img",
        "#presentInfo>p.img>img",
        "#brd-psnt>div.brd-psnt-frm>div.brd-psnt-frm-inr>a img"
    ]

    URL_PRODUCE_MEMBER_APPLIED = "#main>#section>.content>p.apply-after"

    def __init__(self):
        super().__init__(get_driver())

    def get_start_button(self):
        return self.find_element_by_multiple_selectors(By.CSS_SELECTOR, self.URL_INFO_PAGE_A, "抽奖介绍界面的开始抽奖按钮")

    def get_image(self):
        return self.find_element_by_multiple_selectors(By.CSS_SELECTOR, self.URL_INFO_PAGE_IMG, "抽奖介绍界面的图片")

    def get_produce_member_applied(self):
        return self.find_element(By.CSS_SELECTOR, self.URL_PRODUCE_MEMBER_APPLIED, "ProduceMember応募済み灰色按钮")
