import sys
import os
import unittest
from unittest.mock import patch, mock_open

# Add the project directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from xendpalmagic import FileSignatureMatcher
from xendpalmagic.exceptions import InvalidSignatureError, InvalidReturnTypeError, InvalidExtensionError, FileNotFoundError

class TestFileSignatureMatcher(unittest.TestCase):

    def setUp(self):
        self.matcher = FileSignatureMatcher()

    def test_init_invalid_return_type(self):
        with self.assertRaises(InvalidReturnTypeError):
            FileSignatureMatcher(return_type='invalid')

    def test_read_file_signature_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            self.matcher.read_file_signature('non_existent_file.txt')

    @patch('builtins.open', new_callable=mock_open, read_data=b'\x89PNG\r\n\x1a\n')
    @patch('os.path.exists', return_value=True)
    def test_read_file_signature_success(self, mock_exists, mock_file):
        signature = self.matcher.read_file_signature('file.png')
        self.assertEqual(signature, '89504E470D0A1A0A')

    def test_match_signature(self):
        hex_signature = '89504E470D0A1A0A'
        extension = self.matcher.match_signature(hex_signature)
        self.assertEqual(extension, 'png') 

    def test_determine_file_type_extension_method(self):
        self.matcher.detection_method = 'extension'
        self.matcher.mime_types['txt'] = 'text/plain'
        file_type, method = self.matcher.determine_file_type('file.txt')
        self.assertEqual(file_type, 'text/plain')
        self.assertEqual(method, 'extension')

    @patch('builtins.open', new_callable=mock_open, read_data=b'\x89PNG\r\n\x1a\n')
    @patch('os.path.exists', return_value=True)
    def test_determine_file_type_signature_method(self, mock_exists, mock_file):
        self.matcher.detection_method = 'signature'
        self.matcher.signatures['png'] = {'hex_signature': ['89504E47'], 'description': 'PNG image', 'mime_type': 'image/png'}
        file_type, method = self.matcher.determine_file_type('file.png')
        self.assertEqual(file_type, 'image/png')
        self.assertEqual(method, 'signature')

    @patch('builtins.open', new_callable=mock_open, read_data=b'\x00\x00\x00\x00')
    @patch('os.path.exists', return_value=True)
    def test_determine_file_type_unknown(self, mock_exists, mock_file):
        self.matcher.detection_method = 'signature'
        file_type, method = self.matcher.determine_file_type('unknown_file.xyz')
        self.assertEqual(file_type, 'unknown')
        self.assertEqual(method, 'fallback')

    def test_add_custom_signature_invalid_extension(self):
        with self.assertRaises(InvalidExtensionError):
            self.matcher.add_custom_signature('.txt', 'hex_signature', 'description', 'mime_type')

    def test_add_custom_signature_invalid_signature(self):
        with self.assertRaises(InvalidSignatureError):
            self.matcher.add_custom_signature('txt', 'invalid_signature', 'description', 'mime_type')

    def test_add_custom_signature_success(self):
        self.matcher.add_custom_signature('txt', '68656C6C6F', 'Text file', 'text/plain')
        self.assertIn('txt', self.matcher.signatures)
        self.assertEqual(self.matcher.signatures['txt']['description'], 'Text file')

    def test_add_or_update_mime_type_invalid_extension(self):
        with self.assertRaises(InvalidExtensionError):
            self.matcher.add_or_update_mime_type('.txt', 'text/plain')

    def test_add_or_update_mime_type_success(self):
        self.matcher.add_or_update_mime_type('txt', 'text/plain')
        self.assertIn('txt', self.matcher.mime_types)
        self.assertEqual(self.matcher.mime_types['txt'], 'text/plain')

if __name__ == '__main__':
    unittest.main()