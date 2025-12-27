import requests
import random
import re
from config import male_names, female_names
import base64


def get_wp_nonce2():

    # 1. Define the URL
    url = "https://ylilit.ru"

    str_encoded = "Ci8qIDwhW0NEQVRBWyAqLwp2YXIgZGF0YUFqYXggPSB7InVybCI6Imh0dHBzOi8veWxpbGl0LnJ1L3dwLWFkbWluL2FkbWluLWFqYXgucGhwIiwibm9uY2UiOiI0ZDI5NzE3MGI2In07Ci8vIyBzb3VyY2VVUkw9Y2FydC1qcy1leHRyYQovKiBdXT4gKi8K"

    # 2. Send an HTTP GET request to the URL
    response = requests.get(url)

    # 3. Check if the request was successful (optional but recommended)
    if response.status_code == 200:
        # 4. Access the page content as a string (decoded Unicode)
        page_content_text = response.text

        for i in page_content_text.split(" "):
            if str_encoded in i:
                pattern = r'src="data:text/javascript;base64,([^"]+)"></script>'
                match = re.search(pattern, i)
                if match:
                    base64_str = match.group(1)

                    decoded_bytes = base64.b64decode(base64_str)
                    decoded_text = decoded_bytes.decode('utf-8')
                    print(decoded_text)

                    decoded_text2 = decoded_text.replace('/* <![CDATA[ */','')

                    decoded_text2 = decoded_text2.replace('//# sourceURL=cart-js-extra','')

                    decoded_text2 = decoded_text2.replace('/* ]]> */','')

                    decoded_text2 = decoded_text2.strip()

                    #print(decoded_text2)

                    pattern2 = r'var dataAjax = {"url":"https://ylilit.ru/wp-admin/admin-ajax.php","nonce":"(.*)"};'
                    match2 = re.search(pattern2, decoded_text2)
                    if match2:
                        nonce = match2.group(1)
                        print(nonce)
                        return nonce

get_wp_nonce2()
