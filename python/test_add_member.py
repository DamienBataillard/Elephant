import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://e.se1.hr.dmerej.info/")
    page.get_by_role("link", name="Add new employee").click()
    page.get_by_placeholder("Name").click()
    page.get_by_placeholder("Name").fill("Romain")
    page.get_by_placeholder("Email").click()
    page.get_by_placeholder("Email").fill("romain@gmail.com")
    page.locator("#id_address_line1").click()
    page.locator("#id_address_line1").fill("1 Rue de la Paix")
    page.locator("#id_address_line2").click()
    page.locator("#id_address_line2").fill("1 Rue de la Paix")
    page.get_by_placeholder("City").click()
    page.get_by_placeholder("City").fill("Paris")
    page.get_by_placeholder("Zip code").click()
    page.get_by_placeholder("Zip code").fill("75001")
    page.get_by_placeholder("Hiring date").fill("2003-02-01")
    page.get_by_placeholder("Job title").click()
    page.get_by_placeholder("Job title").fill("Pilote de table basse")
    page.get_by_role("button", name="Add").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)