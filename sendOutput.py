import os
import requests
from dotenv import load_dotenv
load_dotenv()
def send_to_discord(content):
    webhook_url = os.environ["WEBHOOK_URL"]
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "content": content
    }
    try:
        response = requests.post(webhook_url, json=data, headers=headers)
        print ("successfully sent to discord")
    except requests.exceptions.RequestException as e:
        print(f"Error sending to Discord: {e}")
    else:
        if response.status_code != 204:
            print(f"Error sending to Discord: {response.text}")