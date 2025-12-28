import requests


def get_cookies_from_cart():
    """
    Заходит на страницу корзины https://ylilit.ru/cart
    и выводит все cookies, полученные от сайта.
    """
    url = "https://ylilit.ru/cart"

    # Создаём сессию (чтобы cookies сохранялись)
    session = requests.Session()


    # Выполняем GET-запрос
    response = session.get(url)

    # Проверяем успешность запроса
    response.raise_for_status()

    if session.cookies:
        for name, value in session.cookies.items():
            cookie = session.cookies.get_dict().get(name)
            # Получаем дополнительные атрибуты, если доступны
            jar = session.cookies
            for c in jar:
                cookie_vaulue = c.value

    return cookie_vaulue.split("-")[-1]
# Вызов функции
print(get_cookies_from_cart())