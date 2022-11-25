import time

from playwright.sync_api import Playwright


class App:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=True, slow_mo=100) # headless=False
        self.context = self.browser.new_context(
            user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/89.0.4389.114 Safari/537.36')
        self.page = self.context.new_page()
        self.page.goto('https://gsmserver.com/')

    def login(self):
        self.page.click("//div[text()='My Account']")
        self.page.click("//div[@class='s-g_dropdown-result-item' and text()='Log In']")
        self.page.fill('//input[@name="username"]', 'tester_fs@i.ua')
        self.page.fill('//input[@name="password"]', 'testI25@')
        self.page.click('//div[@name="submit"]')
        time.sleep(2)

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

