import requests
import json
import random
from config import headers, my_cookies, url
from functions import get_wp_nonce, generate_phone_number, make_menu, generate_random_email
from functions import random_russian_name, get_random_yaroslavl_address
import time

# Generate dishes list
dishes = make_menu()

def run_task():

    # Get new Word press once code
    nonce_code = get_wp_nonce()


    # Get new random dish
    dish_id = random.choice(list(dishes.keys()))
    dish_name = dishes[dish_id][0]
    dish_value = dishes[dish_id][1]
    dish_img = dishes[dish_id][2]
    dish_price = dishes[dish_id][3]

    cart = {
        f"cart[{dish_id}]":
        [random.randint(1, 3),
        f"{dish_img}",
        dish_value,
        f"{dish_name}",
        dish_price]
    }


    cart_json = json.dumps(cart).encode('utf8')

    # Get random name
    name = random_russian_name()
    # Get random phone number
    phone = generate_phone_number()
    # Get random email
    email = generate_random_email()
    # Get random address
    address = get_random_yaroslavl_address()

    # Form new order
    data = {
        'action': 'sendCart',
        'name': f'{name}',
        'tel': f'{phone}',
        'email': f'{email}',
        'adress': f'{address}',
        'nonce_code': nonce_code,
        'cart': cart_json
    }

    print(name, phone, email, address, dish_name, dish_value, dish_price, nonce_code)

    # Make request and get responce
    try:
        responce = requests.post(url, headers=headers, cookies=my_cookies, data=data, timeout=10)
    except:
        print("Connection error...")
    else:
        print(responce.status_code, responce.json())
        print()

count = 1
while True:
    print(f"Task: {count}")
    run_task()
    count+=1
    time.sleep(15)

