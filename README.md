
---

# Xendpalmagic: Advanced File Type Detection Library

Xendpalmagic is a comprehensive Python library designed to enhance file type detection through a multi-faceted approach. By combining file extensions, magic numbers, content analysis, and header parsing, Xendpalmagic offers unmatched accuracy and reliability for identifying a wide range of file formats.

## Features

- **Robust File Type Detection**: Utilizes magic numbers, content analysis, and header parsing for accurate file identification.
- **Customizable Detection Strategies**: Tailor the detection process to prioritize speed, accuracy, or a balance of both.
- **Extensive File Format Support**: Comes with a broad database of file signatures and MIME types, with the flexibility to add new ones.
- **Developer-friendly**: Easy to integrate and use in any Python project requiring file handling capabilities.

## Installation

Install Xendpal-magic using pip:

```bash
pip install xendpalmagic
```

## Quick Start

```python
from xendpalmagic import FileSignatureMatcher

# Initialize the matcher
matcher = FileSignatureMatcher()

# Determine the file type of 'example.pdf'
file_type, method = matcher.determine_file_type('example.pdf')
print(file_type)  # Outputs: 'application/pdf'

```

## Advanced Usage

### Custom Detection Strategy

```python
matcher = FileSignatureMatcher(detection_method='signature', return_type='description')
file_description, method = matcher.determine_file_type('example.docx')
print(file_description)  # Outputs: 'Microsoft Word document'

```

### Adding Custom File Signatures

```python
matcher.add_custom_signature(
    extension='custom',
    hex_signatures=['00 11 22 33', '44 55 66 77'],
    description='Custom File Format',
    mime_type='application/x-custom'
)
```

 
 