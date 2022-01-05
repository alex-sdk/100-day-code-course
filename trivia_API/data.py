import requests

paramaters = {
    'amount':10,
    'type':'boolean'
}
response = requests.get("https://opentdb.com/api.php", params=paramaters)
response.raise_for_status()
data = response.json()
question_data = data['results']

