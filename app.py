from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')  # request
def index():
    return render_template('index.html')  # response


@app.route('/pets')  # request
def pets():
    return render_template('p1-pets.html')  # response


@app.route('/set-environment')
def environment():
    return render_template('1-set-environment.html')


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')
