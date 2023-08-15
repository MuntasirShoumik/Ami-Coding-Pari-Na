import requests


api_url = "http://127.0.0.1:8000/api/get-input-values/"
params = {
    "user_id": 1,
    "start_datetime": "2023-01-01T00:00:00",
    "end_datetime": "2023-08-16T00:00:00"
}


response = requests.get(api_url, params=params)


if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"API request failed with status code: {response.status_code}")
