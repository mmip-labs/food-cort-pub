import requests
from config_samolet import headers, my_cookies, russian_obscene_expressions_with_plane
from functions import get_wp_nonce, generate_phone_number, make_menu, generate_random_email
from functions import random_russian_name, get_random_yaroslavl_address
import time
import random

# Generate dishes list
dishes = make_menu()

def run_task():



    # Get random name
    name = random_russian_name()
    # Get random phone number
    phone = generate_phone_number()
    # Get random email
    email = generate_random_email()
    # Get random address
    comment = get_random_yaroslavl_address()

    theme = 'Досудебное урегулирование/Компенсация/Выплаты'

    # Form new order
    data = {
        'name': f'{name}',
        'phone': f'{phone}',
        'email': f'{email}',
        'comment': f'{random.choice(russian_obscene_expressions_with_plane)}',
        'theme': f'{theme}'
    }

    print(data)


    Make request and get responce
    try:
        responce = requests.post(url, headers=headers, data=data, timeout=20)
    except:
        print("Connection error...")
    else:
        print(responce.status_code, responce.text)
        print()

count = 0

while True:
    print(f"Task: {count}")

    run_task()
    count+=1
    time.sleep(5)

