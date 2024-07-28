import requests
import json


def fetch_data_from_api(api_url, output_file):
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        with open(output_file, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Data successfully saved to {output_file}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


api_url = "https://jsonplaceholder.typicode.com/posts"
output_file = "posts.json"
fetch_data_from_api(api_url, output_file)
