import requests
def send_discord_alert(webhook_url, message):
    data = {"content": message}
    headers = {"Content-Type": "application/json"}
    response = requests.post(webhook_url, json=data, headers=headers)
    if response.status_code != 204:
        print(f"Failed to send Discord message: {response.text}")
