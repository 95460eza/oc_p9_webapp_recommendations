
from flask import Flask, render_template, request
import requests
import json
import pandas as pd

app = Flask(__name__)

# API Endpoint URL
api_url = "http://127.0.0.1:5000/predict"
#api_url = "https://oc-p9-azure-function-contentbased-precalculation-all-in-one.azurewebsites.net/predict"
#api_url = "https://oc-p9-azure-function-contentbased-precalculation-blobbinding.azurewebsites.net/predict"

headers_for_content_and_response = {'Content-Type': 'application/json', 'accept': 'application/json'}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_id = request.form['user_id']

        # Send POST request to API
        payload = {'id': int(user_id)}
        data_as_json = json.dumps(payload)
        response = requests.post(api_url, headers=headers_for_content_and_response, data=data_as_json)
        response_data_received = json.loads(response.text)
        json_string = response_data_received['response']
        last_clicked_item = response_data_received['message']
        df = pd.read_json(json_string)
        
        return render_template('index.html', response_data=df, customer = user_id, last_clicked=last_clicked_item)
        #return render_template('index.html', response_data=df, customer=user_id)

    return render_template('index.html')



#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000, debug=True)

