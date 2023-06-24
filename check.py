import requests
import os

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = os.environ['bottoken']
channel_username = '@pkdart'

def is_user_in_channel(user_id):
    api_url = f'https://api.telegram.org/bot{bot_token}/getChatMember'
    params = {
        'chat_id': channel_username,
        'user_id': user_id
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    if response.status_code == 200 and data['ok']:
        member_status = data['result']['status']
        if member_status in ['creator', 'administrator', 'member']:
            return True
    
    return False


