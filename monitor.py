# Python program to monitor a website and send a notification when the website is changed or updated.
# url will be taken as an argument from flask app frontend and is dynamically changed in the backend.
# This program will be run in a separate thread, notification will be sent using emailer.py

import time
import hashlib
from urllib.request import urlopen, Request
from urllib.error import URLError
from emailer import send_email


def get_hash(url):
    """
    Function to get the hash of the website.
    :param url: url of the website
    :return: hash of the website
    """
    try:
        response = urlopen(Request(url))
        html = response.read()
        hash_object = hashlib.sha256(html)
        hex_dig = hash_object.hexdigest()
        return hex_dig
    except URLError:
        return None


def check_change(url):
    """
    Function to check if the website has changed.
    :param url: url of the website
    :return: True if changed, False if not
    """
    hex_dig = get_hash(url)
    if hex_dig is None:
        return False
    if hex_dig != get_hash(url):
        return True
    return False


def monitor(url):
    """
    Function to monitor the website.
    :param url: url of the website
    :return: None
    """
    while True:
        if check_change(url):
            send_email(url)
        time.sleep(60)


if __name__ == "__main__":
    monitor("https://www.example.com")