import requests
import json

# API Key
api = 'XYKFTUH8J9GE0HX9'

# Requesting
def return_data(company_symbol):
    req_url='https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol='+company_symbol+'&outputsize=full&&apikey='+api
    resp = requests.get(req_url)

# Check status code
if resp.status_code != 200:
    raise ApiError('GET /tasks/ {}'.format(resp.status_code))
#     What does the above code do?
data = resp.json()
