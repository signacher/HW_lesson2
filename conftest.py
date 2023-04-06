import pytest
from selene.support.shared import browser
@pytest.fixture()
def set_up_browser():
    browser.open('https://google.com')
    browser.driver.set_window_size(1024, 768)
    yield browser
    browser.close()