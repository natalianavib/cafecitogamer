from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_complaint', methods=['POST'])
def submit_complaint():
    rut = request.form['rut']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    date = request.form['date']
    description = request.form['description']
    message = request.form['message']
    # Aquí puedes manejar el reclamo o felicitación como desees, por ejemplo, guardarlo en una base de datos o enviarlo por correo electrónico.
    print(f'Reclamo recibido de {first_name} {last_name} ({rut}) en fecha {date} con descripción {description}: {message}')
    return render_template('index.html', message='Tu reclamo/felicitación ha sido enviado.')

if __name__ == '__main__':
    app.run(debug=True)
