import unittest
from xendpalmagic.core import FileSignatureMatcher

class TestFileSignatureMatcher(unittest.TestCase):
    
    def setUp(self):
        # Set up a FileSignatureMatcher instance before each test
        self.matcher = FileSignatureMatcher(return_type='description')

    def test_add_custom_signature(self):
        # Test adding a custom signature
        self.matcher.add_custom_signature('custom', ['DE AD BE EF'], 'Custom File', 'application/custom')
        self.assertIn('custom', self.matcher.signatures)
    
    def test_determine_file_type_known_extension(self):
        # Assuming you have a sample text file in tests directory
        file_path = 'tests/Xendpal_Backend.txt'
        file_type, method = self.matcher.determine_file_type(file_path)
        self.assertEqual(file_type, 'Plain Text File')
        self.assertEqual(method, 'extension')
    
    # More tests can be added here

if __name__ == '__main__':
    unittest.main()
