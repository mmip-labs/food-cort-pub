import requests
import re
import base64
import json


def get_tokens():

    # 1. Define the URL
    url = "https://ylilit.ru"

    pattern_lengh = 900

    tokens = {}

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
                if len(base64_str) >= pattern_lengh:

                    decoded_bytes = base64.b64decode(base64_str)
                    decoded_text = decoded_bytes.decode('utf-8')

                    decoded_text2 = decoded_text.replace('/* <![CDATA[ */','')
                    decoded_text2 = decoded_text2.replace('//# sourceURL=icwp-wpsf-notbot-js-extra','')
                    decoded_text2 = decoded_text2.replace('/* ]]> */','')
                    decoded_text2 = decoded_text2.strip()


                    pattern2 = r'var shield_vars_notbot = (.*);'
                    match2 = re.search(pattern2, decoded_text2)
                    if match2:
                        json_data = match2.group(1)
                        data_object = json.loads(json_data)
                        exnonce = data_object['comps']['notbot']['ajax']['not_bot']['exnonce']
                        wpnonce = data_object['comps']['notbot']['ajax']['not_bot']['_wpnonce']
                        rest_url = data_object['comps']['notbot']['ajax']['not_bot']['_rest_url']

                        tokens['exnonce'] = exnonce
                        tokens['wpnonce'] = wpnonce
                        tokens['rest_url'] = rest_url

                        return tokens

