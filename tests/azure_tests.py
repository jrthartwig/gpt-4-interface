import unittest
from azure.storage import AzureStorage

class TestAzureStorage(unittest.TestCase):

    def setUp(self):
        self.azure_storage = AzureStorage()

    def test_upload_document(self):
        # Test the upload_document function
        # You need to replace 'test_document' and 'test_container' with actual test values
        result = self.azure_storage.upload_document('test_document', 'test_container')
        self.assertEqual(result, True)

    def test_download_document(self):
        # Test the download_document function
        # You need to replace 'test_document' and 'test_container' with actual test values
        result = self.azure_storage.download_document('test_document', 'test_container')
        self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()