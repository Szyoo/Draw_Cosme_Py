# app/services/page_services/info_confirm.py

from app.drivers.driver_manager import get_driver
from app.services.page_services.base import BasePage
from selenium.webdriver.common.by import By


class InfoConfirmPage(BasePage):

    URL_NEXT_BUTTON = "#main form>p.enquete-apl-btn>input.btn-green"

    def __init__(self):
        super().__init__(get_driver())

    def get_next_button(self):
        return self.find_element(By.CSS_SELECTOR, self.URL_NEXT_BUTTON, "个人信息确认页面的下一步按钮")
