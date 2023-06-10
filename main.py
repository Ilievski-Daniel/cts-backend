import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping')
def ping():
    response = {
        'status': 'success',
        'message': '200 OK'
    }
    return jsonify(response)

def create_app():
    return app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))