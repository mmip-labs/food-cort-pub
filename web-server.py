#!/usr/bin/python3

from flask import Flask, request, jsonify, render_template_string
import requests

app = Flask(__name__)

# HTML-форма для тестирования (отображается при GET-запросе)
FORM_HTML = '''
<!doctype html>
<html>
    <head><title>Тест POST-запроса</title></head>
    <body>
        <h1>Отправка данных через форму</h1>
        <form method="post">
            <label>Имя: <input type="text" name="name"></label><br><br>
            <label>Возраст: <input type="number" name="age"></label><br><br>
            <input type="submit" value="Отправить">
        </form>

        <h2>Тестирование JSON (используйте curl или Postman)</h2>
        <pre>
curl -X POST /submit \\
     -H "Content-Type: application/json" \\
     -d '{"name": "Иван", "age": 30}'
        </pre>
    </body>
</html>
'''

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'GET':
        return render_template_string(FORM_HTML)

    if request.method == 'POST':
        # Обработка данных формы (application/x-www-form-urlencoded или multipart/form-data)
        if request.form:
            action = request.form.get('action')
            name = request.form.get('name')
            tel = request.form.get('tel')
            email = request.form.get('email')
            adress = request.form.get('adress')
            nonce_code = request.form.get('nonce_code')
            cart = request.form.get('cart')

            cart = cart.encode().decode('unicode_escape')
            print(name, tel, email, adress)
            print(cart)

            return jsonify({
                'message': 'Данные формы получены',
                'action': action,
                'name': name,
                'tel': tel,
                'email': email,
                'adress': adress,
                'nonce_code': nonce_code,
                'cart': cart
            })

        else:
            return jsonify({'error': 'Неподдерживаемый тип данных'}), 400

if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', debug=True)
