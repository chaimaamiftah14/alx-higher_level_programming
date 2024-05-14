from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/route_5')
def route_5():
    return 'Hello School!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
