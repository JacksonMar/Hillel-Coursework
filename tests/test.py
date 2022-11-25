import re
import time

import pytest
from playwright.async_api import expect
import playwright
from Page_Objects.application import App
from playwright.sync_api import Playwright


class TestCase:
    def test_log_in(self, desktop_app: App):
        desktop_app.login()
        assert desktop_app.page.locator("//div[@class='s-g_title-pretext']").text_content() == 'Hello, Jack'

    def test_check_telephone(self, desktop_app: App):
        desktop_app.page.click('//div[@class="widget_sales-chat_right-panel_btn_btn rsp_btn"]')
        time.sleep(2)
        assert desktop_app.page.locator('//a[@href="https://wa.me/85260181344"]').is_visible()
        desktop_app.page.mouse.move(20, 15)

    def test_add_item(self, desktop_app: App):
        desktop_app.page.click('//div[@key="promo"]/span')
        desktop_app.page.click('//div[@data-name="promo"]/div/div[2]')
        desktop_app.page.click('//div[@class="col-6 d-flex justify-content-end justify-content-md-center align-items-center"]')
        assert desktop_app.page.locator('//a[@href="/cart/"]/i').text_content() == "1"

    def test_remove_item(self, desktop_app: App):
        desktop_app.page.click('//a[@class="widget_cart_header-block hdr_cart invisible-in-critical"]')
        desktop_app.page.click('//div[@class="widget_cart_remove-btn_modal_remove-btn button"]')
        desktop_app.page.click('//div[@name="delete"]')
        assert desktop_app.page.locator('//div[@class="emc_title"]').text_content() == "Your cart is empty"

    def test_log_out(self, desktop_app: App):
        desktop_app.page.locator("//div[@class='s-g_title-pretext']").click()
        desktop_app.page.click('//div[@name="logout"]')
        time.sleep(1)
        assert desktop_app.page.locator("//div[@class='s-g_title-pretext']").text_content() == 'Log In'
