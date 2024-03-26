from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'Xendpal-magic: Advanced File Type Detection Library'
LONG_DESCRIPTION = """Xendpal-magic is a cutting-edge Python library designed to elevate file type detection to new heights. Unlike traditional methods that rely solely on file extensions or basic signatures, Xendpal-magic introduces a multifaceted approach incorporating file extensions, magic numbers, content analysis, and header parsing to deliver unparalleled accuracy and reliability. This library stands out by offering customizable detection strategies, allowing users to tailor the detection process to their specific needs—whether prioritizing speed, accuracy, or a balance of both.

At the heart of Xendpal-magic lies a comprehensive database of file signatures and MIME types, covering a vast spectrum of file formats. From common image and document formats to more obscure or custom file types, Xendpal-magic ensures your application can identify and handle a wide array of files confidently. Furthermore, the library's extensible design means users can effortlessly add new signatures and MIME types, making it an ever-evolving tool that adapts to new file formats and industry standards.

Designed with both ease of use and flexibility in mind, Xendpal-magic caters to developers looking for a simple solution to file type detection while also offering advanced features for those needing more control over the detection process. Whether you're building a content management system, a digital asset manager, or any application that requires robust file handling capabilities, Xendpal-magic is equipped to meet the challenge.

Embrace the future of file type detection with Xendpal-magic and unlock the potential to create more intelligent, efficient, and secure applications."""

# Setting up
setup(
    name="xendpalmagic",
    version=VERSION,
    author="joeygoesgrey",
    author_email="<mail@godfreydjoseph@gmail.com>",
    description=DESCRIPTION,
    packages=find_packages(exclude=['tests*']),
    long_description_content_type="text/markdown",
    long_description=long_description,
    install_requires=open('requirements.txt').read().splitlines(),
    python_requires='>=3.6',
    license='MIT',
    keywords=[
        "file type detection",
        "file signatures",
        "MIME type",
        "content analysis",
        "python",
        "file handling",
        "file identification",
        "magic numbers",
        "file metadata",
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Operating System :: OS Independent',
    ],
)