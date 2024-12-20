import os

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from api_gateway.api_gateway import api_gateway  # Import the API Gateway Blueprint

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS globally (or customize as needed)
load_dotenv()

# Register the API Gateway Blueprint
app.register_blueprint(api_gateway)

if __name__ == '__main__':
    print("Running Main")
    app.run(host='0.0.0.0', port=8000)


