from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
print(long_description)

setup(
    name='chromedriver-autodownloader',
    version='0.2.0',
    license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
    author="Umardy",
    author_email='umardev004@gmail.com',
    classifiers=[ 
        "License :: OSI Approved :: Apache Software License", 
        "Programming Language :: Python :: 3", 
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        ], 
    packages=['chromedriver_autodownloader'],
    url='https://github.com/umardy/chromedriver-autodownloader',
    keywords='automatic chromedriver downloader',
    long_description=long_description,
    long_description_content_type='text/markdown',
)
