from pytest import fixture
from playwright.sync_api import Playwright, sync_playwright
from Page_Objects.application import App


@fixture(scope="class")
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture(scope="class")
def desktop_app(get_playwright) -> None:
    app = App(get_playwright)
    yield app
    app.close()


