"""
Script to demonstrate installing and testing the local xendpalmagic package.

Steps performed:
1. Installs the local package in editable mode.
2. Imports FileSignatureMatcher and demonstrates basic usage.

Run this script after activating your virtual environment:
source ../.venv/bin/activate
python test_xendpalmagic.py
"""

import os
import subprocess
import sys


def install_from_pypi():
    """
    Installs the xendpalmagic package from PyPI using pip.

    Args:
        None
    Returns:
        None
    """
    subprocess.check_call([
        sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'
    ])
    subprocess.check_call([
        sys.executable, '-m', 'pip', 'install', 'xendpalmagic'
    ])


def test_all_file_signature_matcher_methods():
    """
    Demonstrates usage of all public methods of FileSignatureMatcher from xendpalmagic.

    Args:
        None
    Returns:
        None
    """
    from xendpalmagic import FileSignatureMatcher
    matcher = FileSignatureMatcher()
    print("\n--- Test: determine_file_type ---")
    test_file = 'test.txt'
    with open(test_file, 'w') as f:
        f.write('Hello, this is a test file!')
    file_type, method = matcher.determine_file_type(test_file)
    print(f"determine_file_type('{test_file}') -> {file_type} (method: {method})")

    print("\n--- Test: add_custom_signature ---")
    matcher.add_custom_signature(
        extension='custom',
        hex_signatures=['00 11 22 33'],
        description='Custom File Format',
        mime_type='application/x-custom'
    )
    print("Added custom signature for extension 'custom'.")

    print("\n--- Test: add_or_update_mime_type ---")
    matcher.add_or_update_mime_type('custom', 'application/x-custom-updated')
    print("Updated MIME type for extension 'custom'.")

    print("\n--- Test: determine_file_type for custom (should fallback) ---")
    # Create a dummy file with the custom signature
    custom_file = 'custom_file.custom'
    with open(custom_file, 'wb') as f:
        f.write(bytes.fromhex('00 11 22 33 44 55 66 77'))
    file_type, method = matcher.determine_file_type(custom_file)
    print(f"determine_file_type('{custom_file}') -> {file_type} (method: {method})")
    os.remove(test_file)
    os.remove(custom_file)

    print("\n--- Test: read_file_signature (internal, for demonstration) ---")
    # Re-create test.txt
    with open(test_file, 'w') as f:
        f.write('Hello, this is a test file!')
    hex_sig = matcher.read_file_signature(test_file)
    print(f"read_file_signature('{test_file}') -> {hex_sig}")
    os.remove(test_file)

    print("\n--- Test: match_signature (internal, for demonstration) ---")
    # Use a known hex signature for txt (should return None unless mapped)
    result = matcher.match_signature('00 11 22 33 44 55 66 77'.replace(' ', '').upper())
    print(f"match_signature('00 11 22 33 44 55 66 77') -> {result}")

if __name__ == '__main__':
    install_from_pypi()
    test_all_file_signature_matcher_methods()
