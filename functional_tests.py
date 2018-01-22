from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):
    #browser = webdriver.Firefox()

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Someone has heard about a new online feature. She goes to check out their homepage
        self.browser.get('http://localhost:8000')

        # She notices the page title consist of to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # She is invited to enter a to-do item right away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates and page list
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

        inputbox = self.browser.find_element_by_id('id_new_item')
        # She types "Use peacock feathers to make a fly" into a text box
        inputbox.send_keys('Use peacock feathers to make a fly')

        # When she hits enter, the page updates and page list
        # "2: Use peacock feathers to make a fly" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        # There is still a text box inviting her to add another item.
        # She enters "Use peacock to make a fly"
        self.fail('Finish the test!!!!!!!')

        # The page updates again, and now shows both items on her list

        # Edith wonders whether the site remembers. Then she sees the site generated a unique URL
        # for her

        # She visits that URL and her to-do list is still there

        #Satistied, she goes back to sleep

#    browser.quit()


if __name__ == '__main__':
    unittest.main(warnings='ignore')