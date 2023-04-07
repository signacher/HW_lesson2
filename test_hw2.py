import random
import string

from selene.support.shared import browser
from selene import be, have


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for _ in range(length))
    return rand_string


def test_google_search(set_up_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_nullsearch(set_up_browser):
    length = random.randint(10, 15)
    rand_string = generate_random_string(length)
    print('\n', 'Поиск по строке: ' + rand_string)
    browser.element('[name="q"]').should(be.blank).type(rand_string).press_enter()
    browser.element('#result-stats').should(have.text('Результатов: примерно 0'))
