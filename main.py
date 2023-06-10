"""
This module defines a Flask application for the CTS backend server.

The CTS backend server provides a simple API endpoint for the "ping" route,
which returns a success response with a status message.

The Flask application is created and returned by the create_app() function.
"""

import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/ping')
def ping():
    """Endpoint for the ping route."""
    response = {
        'status': 'success',
        'message': '200 OK'
    }
    return jsonify(response)

def create_app():
    """Create and return the Flask application."""
    return app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
