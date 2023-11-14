from flask import Flask

# __name__ is __main__ or the name of the file ex __app__ (namespace)
app = Flask(__name__)

# first route (first request/response): a route is a command to run a specific function which then returns the response to the user.
# Using a decorator : decorators are function that wrap around other functions and let you do things with them.


@app.route('/')  # request
def index():
    return "hello from Pet Adoption"  # response


@app.route('/set-environment')
def environment():
    return "<h1>Installation</h1>"


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='127.0.0.1')
