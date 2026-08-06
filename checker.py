from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

async def checker():
    options = ChromeOptions()

    options.add_argument("--headless=new")      # Remove for debugging
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")

    browser = webdriver.Chrome(options=options)

    try:
        browser.get("https://www.facebook.com/UttarakhandDIPR/")

        wait = WebDriverWait(browser, 20)

        try:
            close_button = wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "[aria-label='Close']")
                )
            )
            close_button.click()
        except:
            pass

        browser.execute_script("window.scrollBy(0, 2000)")

        WebDriverWait(browser, 10).until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )

        combined_xpath = (
            "//div[("
            "contains(., 'देहरादून जनपद') or contains(., 'जनपद देहरादून')) and "
            "contains(., 'मौसम विभाग') and "
            "contains(., 'कक्षा 1 से 12')]"
        )

        return len(browser.find_elements(By.XPATH, combined_xpath)) > 0

    finally:
        browser.quit()