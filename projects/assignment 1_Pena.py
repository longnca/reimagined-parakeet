import requests
import json


class AESOfetcher:
    """A class for fetching data from the AESO API using API calls"""

    def __init__(self, api_key, base_url, accept_type='application/json'):
        """Initialize the AESOfetcher instance"""
        self.api_key = api_key
        self.base_url = base_url
        self.headers = {
            'Accept': accept_type,
            'X-API-Key': self.api_key
        }

    def fetch_data(self, dataset, params=None):
        """A method to fetch data from a specific dataset.

        dataset: The specific dataset to fetch from the AESO API.
        params: An optional dictionary of parameters for the query (e.g. startDate).
        """
        try:
            url = f"{self.base_url}/{dataset}"
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()  # This will raise an HTTPError for bad responses
            return response.json(), response.status_code
        except requests.RequestException as e:
            print(f"Error fetching  data: {e}")
            return None, getattr(e.response, 'status_code', -1)

# Constants

AESO_API_KEY='eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ4bGs2dTYiLCJpYXQiOjE3MDc1MDYwOTZ9.JtX8AnzuRpMBMibDs5q7oaEzH9etllM_xWGtS-qbv0Q' # os.getenv('AESO_API_KEY')
BASE_URL='https://api.aeso.ca/report'
CURRENT_SUPPLY_DEMAND_URL='v1/csd/summary/current'
INTERNAL_LOAD_URL='v1/load/albertaInternalLoad'
POOL_PRICE_REPORT='v1.1/price/poolPrice'
CALGARY_API_URL='https://api.weather.gc.ca/'

# Create an instance of the AESOfetcher with the API key
fetcher = AESOfetcher(api_key=AESO_API_KEY,base_url=BASE_URL)

# Try fetching Actual Forecast for a specific date range

actual_forecast_data, status_code = fetcher.fetch_data(INTERNAL_LOAD_URL,
                                        {'startDate':'2015-01-01', 'endDate':'2016-01-01'})
print(actual_forecast_data.keys())
print(f"Status Code: {status_code}")

# Try fetching Current Supply Demand
current_supply_demand, status_code = fetcher.fetch_data(CURRENT_SUPPLY_DEMAND_URL)
print(f"Status Code: {status_code}")
print(current_supply_demand.keys())

load_sum = 0.0
aeso_data = actual_forecast_data['return']['Actual Forecast Report']
for loadval in range(len(aeso_data)):
		load_sum += float(aeso_data[loadval]['alberta_internal_load'])

print(f"Total Load for 2015: {load_sum}")

# Try fetching Pool Price Report
pool_price_rep, status_code = fetcher.fetch_data(POOL_PRICE_REPORT)
print(f"Status Code: {status_code}")
print(pool_price_rep.keys())

# Create an instance of the Calgary API with the API key
yyc_fetcher = AESOfetcher(api_key=AESO_API_KEY,base_url=CALGARY_API_URL)

# Try fetching Actual Forecast for a specific date range

yyc_forecast_data, status_code = yyc_fetcher.fetch_data('https://dd.weather.gc.ca/citypage_weather/xml/AB/s0000047_e.xml'  ,
                                        {'startDate':'2015-01-01', 'endDate':'2016-01-01'})