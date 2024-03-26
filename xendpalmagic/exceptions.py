class InvalidExtensionError(Exception):
    """Exception raised for invalid file extension."""

    def __init__(self, extension, message="Invalid extension specified."):
        self.extension = extension
        self.message = f"{message} '{extension}' should not contain a dot ('.')."
        super().__init__(self.message)


class InvalidReturnTypeError(Exception):
    """Exception raised for invalid return type."""

    def __init__(self, return_type, message="Invalid return type specified."):
        self.return_type = return_type
        self.message = f"{message} '{return_type}' is not supported."
        super().__init__(self.message)


class InvalidSignatureError(Exception):
    """Exception raised for invalid file signature format."""

    def __init__(self, signature_hex, message="Invalid signature format."):
        self.signature_hex = signature_hex
        self.message = f"{message} '{signature_hex}' is not properly formatted."
        super().__init__(self.message)


class FileNotFoundError(Exception):
    """Exception raised when the file path does not exist."""

    def __init__(self, file_path, message="File not found:"):
        self.file_path = file_path
        self.message = f"{message} '{file_path}'"
        super().__init__(self.message)
