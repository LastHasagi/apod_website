from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def hello():
        return "Hello, World!"

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)