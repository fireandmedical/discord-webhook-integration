# main.py

import requests
import json

def send_discord_message(webhook_url, message):
    data = {
        "content": message,
        "username": "Webhook Bot"
    }
    
    headers = {
        "Content-Type": "application/json"
    }
    
    response = requests.post(webhook_url, data=json.dumps(data), headers=headers)
    
    if response.status_code == 204:
        print("Message sent successfully")
    else:
        print(f"Failed to send message: {response.status_code}")

if __name__ == "__main__":
    webhook_url = "YOUR_DISCORD_WEBHOOK_URL_HERE"
    message = "Hello, this is a test message from your webhook!"
    send_discord_message(webhook_url, message)
  
