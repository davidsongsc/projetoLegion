import requests
import json

url = 'https://graph.facebook.com/v17.0/107675335722225/messages'
headers = {
    'Authorization': 'Bearer EAASkREVCucgBAESMMN6lGF35rQFnXXnENxffCb959DLKNBju0BP09d1meTalZAybBmLsfCFqaFbIPZA0QzYzXJ7GqfIX6AcE5nr7YyOhZASgoZBWqwoP5btFtRjGd3i5Mgaz4LAKtmhBeVkjnUjlOpePe1ZA5zlhXBtdZA77bZBWZCPJHRAZBLmcIFsFOet9XUKXWJ1vEWjpM8wZDZD',
    'Content-Type': 'application/json'
}

data = {
    "messaging_product": "whatsapp",
    "to": "5521983108439",
    "type": "template",
    "template": {
        "name": "hello_world",
        "language": {
            "code": "en_US"
        }
    }
}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.text)