import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.uniqlo.com/us/en/men")
    page.get_by_role("button", name="What are you looking for?").click()
    page.get_by_role("textbox", name="Search by keyword").click()
    page.get_by_role("textbox", name="Search by keyword").fill("lambswool sweater")
    page.get_by_role("textbox", name="Search by keyword").press("Enter")

    page.get_by_role("link", name="Premium Lambswool Sweater").click()

    productName = page.get_by_role('heading').first.inner_text()
    price = page.get_by_role('main').get_by_text(re.compile(r'\$\d+\.\d{2}')).inner_text()
    # ---------------------
    context.close()
    browser.close()

    print("Success! Product " + productName + " found at " + price + "!")


with sync_playwright() as playwright:
    run(playwright)