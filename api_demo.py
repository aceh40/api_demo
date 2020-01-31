import requests, json
from os import getenv
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

endpoint_url = getenv("URL")
passwd = getenv("PASSWORD")
user_name = getenv("USER")

req_array = [
    {"function": "GDSP", "identifier": "IBM:NYSE", "mnemonic": "IQ_TOTAL_REV", "properties": {"PeriodType": "IQ_FY"}},
    {"function": "GDSHE", "identifier": "IBM:NYSE", "mnemonic": "IQ_EBITDA",
     "properties": {"PeriodType": "IQ_FY-4", "restatementTypeId": "LC"}},
    {"function": "GDST", "identifier": "IBM:NYSE", "mnemonic": "IQ_MARKETCAP",
     "properties": {"frequency": "Monthly", "startDate": "01/01/2018"}}]

req = {"inputRequests": req_array}

response = requests.post(endpoint_url,
                         headers={'Content-Type': 'application/json'},
                         data=json.dumps(req),
                         auth=HTTPBasicAuth(username=user_name, password=passwd),
                         verify=True)
print(response.text)
