from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from unittest import skip


class ItemValidationTest(FunctionalTest):
    
    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidently tries to submit
        # and empty List item.  She hits Enter on the empty input box
        
        # The home page refreshes, and there is an error message saying
        # that the List items cannot be blank
        
        # She tries again with some text for the item, which now works
        
        # Perversely, she now decides to submit a second blank List item
        
        # She receives a similar warning on the List page
        
        # and she can correct it by filling in some text
        self.fail('Write me!')
        
        


