import unittest
from src.utils import data_cleaning, data_formatting

class TestUtils(unittest.TestCase):

    def setUp(self):
        # This method will be called before each test, you can use it to set up any state 
        # or to prepare the test environment.
        pass

    def test_data_cleaning(self):
        # Here you can add assertions to test your data cleaning function
        # For example, you can check if the function correctly removes sensitive information
        raw_data = "Sensitive Info: 12345"
        cleaned_data = data_cleaning(raw_data)
        self.assertNotIn("12345", cleaned_data)

    def test_data_formatting(self):
        # Here you can add assertions to test your data formatting function
        # For example, you can check if the function correctly formats the data as per OpenAI’s guidelines
        raw_data = "Some raw data"
        formatted_data = data_formatting(raw_data)
        # Add your assertions here
        # self.assertEqual(expected_result, formatted_data)

    def tearDown(self):
        # This method will be called after each test, you can use it to clean up any resources 
        # or to reset the state after the test.
        pass

if __name__ == '__main__':
    unittest.main()