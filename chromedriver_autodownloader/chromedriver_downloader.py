import re
import subprocess
import sys
import zipfile
import os
import requests


chrome_version_map = {
    "linux": {
        "name": "linux",
        "zipfile_name": "chromedriver_linux64.zip",
        "cmd": r"google-chrome --version",
    },
    "darwin": {
        "name": "mac",
        "zipfile_name": "chromedriver_mac64.zip",
        "cmd": r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome --version",
    },
    "win32": {
        "name": "windows",
        "zipfile_name": "chromedriver_win32.zip",
        "cmd": r'wmic datafile where name="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe" get Version /value',
    },
}

chromedriver_url = "https://chromedriver.storage.googleapis.com/"


def download_chromedriver(target_dir=None):
    """Download and extracting chromedriver to target directory.
    Params: target_dir: directory to extract chromedriver. If you use helium,
    you can set target_dir='helium'."""

    platform = sys.platform
    pattern = r"([\s=])(\d{2,3})(.)"
    chrome_version = subprocess.check_output(chrome_version_map[platform]["cmd"])
    version = re.search(pattern, str(chrome_version)).group(2)
    print(f"Your chrome version: {version}")
    chrome_version_url = chromedriver_url + "LATEST_RELEASE_" + version

    try:
        res = requests.get(chrome_version_url)
        download_url = (
            chromedriver_url
            + res.text
            + "/"
            + chrome_version_map[platform]["zipfile_name"]
        )
        print(f"Downloading chromedriver from: {download_url}")
        res = requests.get(download_url)
        with open("chromedriver.zip", "wb") as chromedriver:
            for chunk in res.iter_content(chunk_size=100000):
                chromedriver.write(chunk)
    except Exception as e:
        print("Error.", e)

    try:
        print("Extracting chromedriver to ", end="")
        with zipfile.ZipFile("chromedriver.zip", "r") as zip_ref:
            if target_dir:
                if target_dir == "helium":
                    import importlib

                    helium_dir = os.path.join(
                        os.path.dirname(importlib.util.find_spec("helium").origin),
                        "_impl",
                        "webdrivers",
                        chrome_version_map[platform]["name"],
                    )
                    print(helium_dir)
                    zip_ref.extractall(helium_dir)
                else:
                    print(target_dir)
                    zip_ref.extractall(target_dir)
            else:
                print("current directory.")
                zip_ref.extractall()
        os.unlink("chromedriver.zip")
        print("Done.")

    except Exception as e:
        print("Error.", e)
