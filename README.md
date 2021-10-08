# A Super Simple Automatic Chromedriver Downloader

Usage:
```python
from chromedriver_autodownloader import download_chromedriver
download_chromedriver() # download and extract chromedriver to current directory
# or
download_chromedriver(target_dir) # download and extract to spesified target directory
```

if you use [helium](https://github.com/mherrmann/selenium-python-helium) and want to extract chromedriver to it's webdriver path you can code as below
```python
download_chromedriver('helium')
```