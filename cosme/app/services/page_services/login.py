# app/services/page_services/login.py

from app.drivers.driver_manager import get_driver
from app.services.page_services.base import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    URL_LOGIN_FRAME = [
        "div.inr>div.TB_main .btn-cmn a",  # 点击produce member时弹出的登录框按钮
        "div.usr-auth>ul>li:nth-child(2)>a"  # 主界面下的登陆按钮
    ]

    URL_MAIL = "form>ul input#LoginUserLoginId"
    URL_PASSWORD = "form>ul input#LoginUserPassword"
    URL_LOGIN_SUBMIT = "form>input.button-submit"

    def __init__(self):
        super().__init__(get_driver())

    def get_login_frame(self):
        return self.find_element_by_multiple_selectors(By.CSS_SELECTOR, self.URL_LOGIN_FRAME, "登录弹出框")

    def get_mail_input(self):
        return self.find_element(By.CSS_SELECTOR, self.URL_MAIL, "登录页面的邮箱输入框")

    def get_password_input(self):
        return self.find_element(By.CSS_SELECTOR, self.URL_PASSWORD, "登录页面的密码输入框")

    def get_submit_button(self):
        return self.find_element(By.CSS_SELECTOR, self.URL_LOGIN_SUBMIT, "登录页面的登录按钮")
