from flask import Flask, request
import os
import numpy as np
import joblib
from google.cloud import storage

app = Flask(__name__)
client_storage = storage.Client()

def load_model(client, bucket_name, path):
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(path)
    blob.download_to_filename(os.getcwd() + '/model.pkl')
    model = joblib.load('model.pkl')
    return model

@app.post("/predict")
def predict_result():
    feature_data = request.get_json()
    feature_array = np.array(list(feature_data.values()))
    model = load_model(client_storage, 'trained-models-1234', 'breast-cancer-model/model.pkl')
    prediction = model.predict(feature_array).tolist()
    return prediction


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)

