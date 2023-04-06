
from selene.support.shared import browser
from selene import be, have


def test_google_search(set_up_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_google_nullsearch(set_up_browser):
    browser.element('[name="q"]').should(be.blank).type('fgvyhercg').press_enter()
    browser.element('#result-stats').should(have.text('Результатов: примерно 0'))
