import base64
import functions_framework
import requests
from google.auth import default
from google.auth.transport.requests import Request

# Triggered from a message on a Cloud Pub/Sub topic.
@functions_framework.cloud_event
def hello_pubsub(cloud_event):
    creds, _ = default()
    creds.refresh(Request())
    REGION = "us-central1"
    PROJECT = "elated-effect-464110-f2"
    JOB_NAME = "breasst-cancer-detection"

    # Print out the data from Pub/Sub, to prove that it worked
    print(base64.b64decode(cloud_event.data["message"]["data"]))
    headers = {
        "Authorization": f"Bearer {creds.token}",
        "Content-Type": "application/json"
    }
    url = "https://us-central1-run.googleapis.com/apis/run.googleapis.com/v1/namespaces/elated-effect-464110-f2/jobs/breasst-cancer-detection:run"
    response = requests.post(url, headers=headers)
    print(f"Response code: {response.status_code}")
    print(response.text)
    print("Successfully run")
