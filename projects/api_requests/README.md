Project 1: Creating and using a class to make an API request to the AESO API

1. Use the API key provided in constants.py to make a request to the AESO API
2. Pull down the following data:
   1. Actual Forecast Report
   2. Pool Price Report
3. Once that is finished, use the environment Canada API (https://api.weather.gc.ca/) to fetch the weather data for Calgary
   1. This should include daily temperatures, percipitation information and forecasting data
4. Also, use pandas to import more granular xls data from excel files to be provided by Neal in the folder data > raw

5. If we have city granular energy use for Calgary, then we can use said usage and weather for the city. 
   1. Public holidays (https://date.nager.at/Api)
   2. natural gas prices (https://datahub.io/vara.maruboina/henry-hub-natural-gas-spot-price)
   3. big events (maybe??) - like stampede - check if there is an impact first before including it as a feature 
   4. weather (https://api.weather.gc.ca/) 
   5. length of daylight (sunrise/sunset) ??
   6. Demand (AESO)
   