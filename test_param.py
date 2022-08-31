import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    browser.implicitly_wait(15)
    yield browser
    browser.quit()

l = ["236895/step/1",
     "236896/step/1",
     "236897/step/1",
     "236898/step/1",
     "236899/step/1",
     "236903/step/1",
     "236904/step/1",
     "236905/step/1"
     ]

@pytest.mark.parametrize('links', l)
def test_l(browser, links):
    answer = math.log(int(time.time()))
    link = f"https://stepik.org/lesson/{links}"
    browser.get(link)
    textarea = browser.find_element(By.CSS_SELECTOR, '''textarea[spellcheck="false"]''').send_keys(answer)
    submit = browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()
    corr = browser.find_element(By.CSS_SELECTOR, "p.smart-hints__hint").text
    print(corr)
    assert "Correct!" == corr






