from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send_message', methods=['POST'])
def send_message():
    phone = request.json.get('phone')
    message = request.json.get('message')

    if not phone or not message:
        return jsonify({'error': 'Все поля обязательны для заполнения!'}), 400

    # Здесь можно добавить код для отправки данных (например, в Telegram или на email)
    print(f'Номер телефона: {phone}')
    print(f'Сообщение: {message}')

    return jsonify({'success': 'Сообщение успешно отправлено!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
