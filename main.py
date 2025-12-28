import requests
import json
import random
from config import headers, my_cookies, url
from functions import get_wp_nonce2, generate_phone_number, make_menu, generate_random_email
from functions import random_russian_name, get_random_yaroslavl_address
import time

# Generate dishes list
dishes = make_menu()

def run_task(wp_nonce_code):

    # Get new Word press once code
    nonce_code = wp_nonce_code


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

    try:
        cart_json = json.dumps(cart,ensure_ascii=False)
    except:
        cart = {"cart[4637]": [3, "https://ylilit.ru/wp-content/uploads/2023/11/Kebab-v-lavashe.webp", "300",
                        "Кебаб с тертым сыром в лаваше .(Фирменное блюдо)", "385"]}
        cart_json = json.dumps(cart,ensure_ascii=False)

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
    print(data)


    # Make request and get responce
    try:
        responce = requests.post(url, headers=headers, cookies=my_cookies, data=data, timeout=20)
    except:
        print("Connection error...")
    else:
        print(responce.status_code, responce.text)
        print()

count = 0
#nonce_code = get_wp_nonce()
#nonce_code = "2922f6f0ea"

while True:
    print(f"Task: {count}")
    if count % 30 == 0:
        nonce_code = get_wp_nonce2()
        print("Code updated!")
    run_task(nonce_code)
    count+=1
    time.sleep(20)

