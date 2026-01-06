import requests
import re
import base64
import json


def get_token():

    # 1. Define the URL
    url = "https://ylilit.ru/cart"


    # 2. Send an HTTP GET request to the URL
    response = requests.get(url)

    # 3. Check if the request was successful (optional but recommended)
    if response.status_code == 200:
        # 4. Access the page content as a string (decoded Unicode)
        page_content_text = response.text

        for i in page_content_text.split(" "):
            pattern = r'sitekey="(.*)"'
            match = re.search(pattern, i)
            if match:
                token_str = match.group(1)
                return token_str

g_token = get_token()

headers = {
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',

}

my_cookies = {

}
data = {
    'k': '6Lc_UTksAAAAACENYofamCPxqUn1sMUODwXZOUwQ'
}

url = 'https://www.google.com/recaptcha/api2/userverify'

# Make request and get responce

responce = requests.post(url, headers=headers, cookies=my_cookies, data=data, timeout=20)

print(responce.status_code, responce.text)
