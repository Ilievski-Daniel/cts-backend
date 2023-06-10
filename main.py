from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping')
def ping():
    response = {
        'status': 'success',
        'message': '200 OK'
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)