from flask import Flask, request, make_response
import os, json
from flask_cors import CORS, cross_origin
from weather_data import WeatherData  # Ensure this import is correct

app = Flask(__name__)
CORS(app)  # Enabling CORS for all routes

# Initialize an instance of WeatherData globally
weather_data_instance = WeatherData()

@app.route('/')
def index():
    return 'Web App with Python Flask!'

# Getting and sending response to Dialogflow
@app.route('/webhook', methods=['POST'])
@cross_origin()
def webhook():
    req = request.get_json(silent=True, force=True)
    print("Request received:")
    print(json.dumps(req, indent=4))

    # Use the instance of WeatherData to call processRequest
    res = weather_data_instance.processRequest(req)  # Fixed this line
    res = json.dumps(res)
    
    print("Response to be sent:")
    print(res)
    
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

if __name__ == '__main__':
    # Run the app in debug mode
    app.run(debug=True)
