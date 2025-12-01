# app.py
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from the Dockerized Python App!'

if __name__ == '__main__':
    # 0.0.0.0 is crucial for containers to be externally accessible
    app.run(host='0.0.0.0', port=5000)