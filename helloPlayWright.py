import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.amazon.com/")
    page.get_by_role("searchbox", name="Search Amazon").click()
    page.get_by_role("searchbox", name="Search Amazon").fill("rtx 5070")
    page.get_by_role("button", name="rtx 5070", exact=True).click()
    page.get_by_role("link", name="Sponsored Ad - ASUS The SFF-").click()
    page.get_by_text("579.", exact=True).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)