class InvalidExtensionError(Exception):
    """
    Exception raised for invalid file extension.

    Args:
        extension (str): The file extension that caused the error.
        message (str): Optional custom error message.

    Attributes:
        extension (str): The invalid file extension.
        message (str): The error message.
    """

    def __init__(self, extension, message="Invalid extension specified."):
        """
        Initializes InvalidExtensionError with extension and message.

        Args:
            extension (str): The file extension that caused the error.
            message (str): Optional custom error message.

        Returns:
            None
        """
        self.extension = extension
        self.message = f"{message} '{extension}' should not contain a dot ('.')."
        super().__init__(self.message)


class InvalidReturnTypeError(Exception):
    """
    Exception raised for invalid return type.

    Args:
        return_type (str): The return type that caused the error.
        message (str): Optional custom error message.

    Attributes:
        return_type (str): The invalid return type.
        message (str): The error message.
    """

    def __init__(self, return_type, message="Invalid return type specified."):
        """
        Initializes InvalidReturnTypeError with return_type and message.

        Args:
            return_type (str): The return type that caused the error.
            message (str): Optional custom error message.

        Returns:
            None
        """
        self.return_type = return_type
        self.message = f"{message} '{return_type}' is not supported."
        super().__init__(self.message)


class InvalidSignatureError(Exception):
    """
    Exception raised for invalid file signature format.

    Args:
        signature_hex (str): The invalid hexadecimal signature.
        message (str): Optional custom error message.

    Attributes:
        signature_hex (str): The invalid hexadecimal signature.
        message (str): The error message.
    """

    def __init__(self, signature_hex, message="Invalid signature format."):
        """
        Initializes InvalidSignatureError with signature_hex and message.

        Args:
            signature_hex (str): The invalid hexadecimal signature.
            message (str): Optional custom error message.

        Returns:
            None
        """
        self.signature_hex = signature_hex
        self.message = f"{message} '{signature_hex}' is not properly formatted."
        super().__init__(self.message)


class FileNotFoundError(Exception):
    """
    Exception raised when the file path does not exist.

    Args:
        file_path (str): The file path that was not found.
        message (str): Optional custom error message.

    Attributes:
        file_path (str): The missing file path.
        message (str): The error message.
    """

    def __init__(self, file_path, message="File not found:"):
        """
        Initializes FileNotFoundError with file_path and message.

        Args:
            file_path (str): The file path that was not found.
            message (str): Optional custom error message.

        Returns:
            None
        """
        self.file_path = file_path
        self.message = f"{message} '{file_path}'"
        super().__init__(self.message)
