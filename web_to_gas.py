import os
import sys
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

GAS_URL = os.environ.get('GAS_URL')


def extract_text(url: str, selector: str) -> str:
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    try:
        driver.get(url)
        element = driver.find_element(By.CSS_SELECTOR, selector)
        return element.text
    finally:
        driver.quit()


def send_to_gas(text: str) -> requests.Response:
    if not GAS_URL:
        raise RuntimeError('GAS_URL environment variable not set')
    return requests.post(GAS_URL, json={'text': text})


def main():
    if len(sys.argv) < 3:
        print('Usage: python web_to_gas.py <url> <css_selector>')
        sys.exit(1)
    url = sys.argv[1]
    selector = sys.argv[2]
    text = extract_text(url, selector)
    response = send_to_gas(text)
    print('GAS response:', response.text)


if __name__ == '__main__':
    main()
