import requests
import pandas as pd
import json

class APIDataFetcher:
    def __init__(self, url, headers, api_key):
        self.url = url
        self.headers = headers
        self.api_key = api_key

    def fetch_data(self):
        url_with_key = f"{self.url}?api_key={self.api_key}"
        response = requests.get(url_with_key, headers=self.headers)
        data = response.json()

        return data

    def save_as_csv(self, data, filename):
    # Extract only the 'period' (date) and 'value' (price) from each data point
        simplified_data = [{'date': item['period'], 'price': item['value']} for item in data['response']['data']]
    
    # Convert the simplified data to a DataFrame
        df = pd.DataFrame(simplified_data)
    
    # Save the DataFrame as a CSV file
        df.to_csv(filename, index=False)


# Usage
url = "https://api.eia.gov/v2/natural-gas/pri/fut/data/"
headers = {
    "X-Params": json.dumps({
        "frequency": "daily",
        "data": ["value"],
        "facets": {},
        "start": "1990-01-01",
        "end": "2000-01-01",
        "sort": [{"column": "period", "direction": "desc"}],
        "offset": 0,
        "length": 5000
    })
}
api_key = "80YB0XgTZLn682y6ggfsh4Q8Vy4GGyqt8YgdCFbR"         #  API key
fetcher = APIDataFetcher(url, headers, api_key)
data = fetcher.fetch_data()
fetcher.save_as_csv(data, "ng_prices_output_90s.csv")
print(data)



