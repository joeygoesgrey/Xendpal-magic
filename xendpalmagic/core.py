import binascii
import os
from xendpalmagic.exceptions import InvalidSignatureError, InvalidReturnTypeError, InvalidExtensionError, FileNotFoundError
from xendpalmagic.signatures import file_signatures, mime_types


class FileSignatureMatcher:
    """
    FileSignatureMatcher provides advanced file type detection using file extensions, magic numbers, content analysis, and header parsing.

    Attributes:
        signatures (dict): Database of file signatures.
        mime_types (dict): Mapping of file extensions to MIME types.
        detection_method (str): Strategy for detection ('auto', 'extension', 'signature').
        return_type (str): Output type ('mime', 'extension', 'description').
        num_bytes (int): Number of bytes to read from the file for signature detection.
    """

    def __init__(self, detection_method='auto', return_type='mime', num_bytes=2048):
        """
        Initializes the FileSignatureMatcher with detection strategy and return type.

        Args:
            detection_method (str): Detection strategy ('auto', 'extension', 'signature').
            return_type (str): Output type ('mime', 'extension', 'description').
            num_bytes (int): Number of bytes to read from the file for signature detection.

        Returns:
            None
        """
        self.signatures = file_signatures
        self.mime_types = mime_types
        self.detection_method = detection_method
        if return_type not in ['mime', 'extension', 'description']:
            raise InvalidReturnTypeError(return_type)
        self.return_type = return_type
        self.num_bytes = num_bytes

    def read_file_signature(self, file_path):
        """
        Reads the first num_bytes of the file and returns its hexadecimal signature.

        Args:
            file_path (str): Path to the file to read.

        Returns:
            str: Hexadecimal string representing the file's initial bytes.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file {file_path} does not exist.")
        with open(file_path, 'rb') as file:
            return binascii.hexlify(file.read(self.num_bytes)).decode('utf-8').upper()

    def match_signature(self, hex_signature):
        """
        Attempts to match a given hexadecimal file signature to a known file type.

        Args:
            hex_signature (str): The hexadecimal string representing the initial bytes of a file.

        Returns:
            str or None: The file extension (e.g., 'pdf', 'jpg') if a match is found; otherwise, None.
        """
        for extension, value in self.signatures.items():
            for signature in value["hex_signature"]:
                clean_signature = signature.replace(" ", "").upper()
                if hex_signature.startswith(clean_signature):
                    return extension
        return None

    def determine_file_type(self, file_path):
        """
        Determines the file type using the configured detection method (extension, signature, or both).

        Args:
            file_path (str): Path to the file to check.

        Returns:
            tuple: (file type in the specified return_type, detection method used as str)
        """
        # Start with extension-based detection if auto or extension is the chosen method
        extension = file_path.split('.')[-1].lower()
        if self.detection_method == 'auto' or self.detection_method == 'extension':
            if extension in self.mime_types:
                result = self._get_result_based_on_return_type(extension)
                return result, 'extension'

        # Proceed with signature-based detection if auto or signature is the chosen method
        if self.detection_method == 'auto' or self.detection_method == 'signature':
            file_signature_hex = self.read_file_signature(file_path)
            matched_extension = self.match_signature(file_signature_hex)
            if matched_extension:
                result = self._get_result_based_on_return_type(matched_extension)
                return result, 'signature'

        # Fallback if no method yields result
        return "unknown", 'fallback'

    def _get_result_based_on_return_type(self, extension):
        """
        Returns the result for the given extension in the format specified by return_type.

        Args:
            extension (str): File extension to look up.

        Returns:
            str: Result in the format specified by return_type ('mime', 'extension', or 'description').
        """
        if self.return_type == 'mime':
            return self.mime_types.get(extension, "unknown")
        elif self.return_type == 'extension':
            return extension
        elif self.return_type == 'description':
            # Assuming descriptions are stored in file_signatures
            description = self.signatures.get(extension, {}).get('description', f'{extension.upper()}')
            return description

    def add_custom_signature(self, extension, hex_signatures, description, mime_type):
        """
        Adds a custom file signature to the matcher for runtime extension of detection.

        Args:
            extension (str): File extension (without dot).
            hex_signatures (list or str): List of hex signature strings or a single string.
            description (str): Description of the file type.
            mime_type (str): MIME type for the file extension.

        Returns:
            None
        """
        if '.' in extension:
            raise InvalidExtensionError(extension)
        
        if not isinstance(hex_signatures, list):
            hex_signatures = [hex_signatures]
        
        for signature in hex_signatures:
            if not all(c in "0123456789ABCDEFabcdef " for c in signature) or '-' in signature:
                raise InvalidSignatureError(signature)
        
        self.signatures[extension] = {
            "hex_signature": hex_signatures,
            "description": description,
            "mime_type": mime_type
        }

    def add_or_update_mime_type(self, extension, mime_type):
        """
        Adds or updates the MIME type for a given file extension.

        Args:
            extension (str): File extension (without dot).
            mime_type (str): MIME type to associate with the extension.

        Returns:
            None
        """
        if '.' in extension:
            raise InvalidExtensionError(extension)
        
        self.mime_types[extension] = mime_type
