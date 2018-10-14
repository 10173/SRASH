import os
from flask import Flask, render_template, make_response
from flask import redirect, request, jsonify, url_for

from clarifai.rest import ClarifaiApp
from appclaifai.model.helpers import get_model
from appclaifai.model.helpers import predict

app_obj = ClarifaiApp(api_key = 'a28d6ad6382d434a9cae46a67b97364e')
paper_model = get_model(app_obj, 'general-v1.3')

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.debug = True
app._static_folder = os.path.abspath("pics")

@app.route('/', methods=['GET'])
def home():
    return redirect('https://srash.netlify.com')

@app.route('/<base64image>', methods=['POST'])
def captured(base64image):
    class_probs = predict(paper_model, base64image)

if __name__ == '__main__':
    app.run()
