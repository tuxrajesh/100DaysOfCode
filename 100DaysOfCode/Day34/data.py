API_URL = "https://opentdb.com/api.php"
parameters = {
        "amount": 10,
        "type": 'boolean'
    }

import requests
response = requests.get(url=API_URL, params=parameters)
response.raise_for_status()
data = response.json()
question_data = data['results']
