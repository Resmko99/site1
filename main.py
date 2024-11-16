from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    phone = request.form.get('phone')
    message = request.form.get('message')

    if not phone or not message:
        flash('Все поля обязательны для заполнения!')
        return redirect(url_for('index'))

    # Здесь добавьте код для обработки данных (например, отправка на email или в Telegram)
    print(f'Номер телефона: {phone}')
    print(f'Сообщение: {message}')

    flash('Сообщение успешно отправлено!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
