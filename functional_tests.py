from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    browser = webdriver.Firefox()

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Someone has heard about a new online feature. She goes to check out their homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title consist of to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

    # She is invited to enter a to-do item right away

    # She types "Buy peacock feathers" into a text box

    # When she hits enter, the page updates and page list
    # "1: Buy peacock feathers" as an item in a to-do list

    # There is still a text box inviting her to add another item.
    # She enters "Use peacock to make a fly"

    # The page updates again, and now shows both items on her list

    # Edith wonders whether the site remembers. Then she sees the site generated a unique URL
    # for her

    # She visits that URL and her to-do list is still there

    #Satistied, she goes back to sleep

    browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')