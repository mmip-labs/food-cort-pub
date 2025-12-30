import requests
import re
import base64


def get_wp_nonce2():

    # 1. Define the URL
    url = "https://ylilit.ru"

    pattern_lengh = 192

    # 2. Send an HTTP GET request to the URL
    response = requests.get(url)

    # 3. Check if the request was successful (optional but recommended)
    if response.status_code == 200:
        # 4. Access the page content as a string (decoded Unicode)
        page_content_text = response.text

        for i in page_content_text.split(" "):
            pattern = r'src="data:text/javascript;base64,([^"]+)"></script>'
            match = re.search(pattern, i)
            if match:
                base64_str = match.group(1)
                if len(base64_str) == pattern_lengh:

                    decoded_bytes = base64.b64decode(base64_str)
                    decoded_text = decoded_bytes.decode('utf-8')

                    decoded_text2 = decoded_text.replace('/* <![CDATA[ */','')
                    decoded_text2 = decoded_text2.replace('//# sourceURL=cart-js-extra','')
                    decoded_text2 = decoded_text2.replace('/* ]]> */','')
                    decoded_text2 = decoded_text2.strip()

                    pattern2 = r'var dataAjax = {"url":"https://ylilit.ru/wp-admin/admin-ajax.php","nonce":"(.*)"};'
                    match2 = re.search(pattern2, decoded_text2)
                    if match2:
                        nonce = match2.group(1)
                        return nonce

print(get_wp_nonce2())
