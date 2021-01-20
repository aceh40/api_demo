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
     "properties": {"PeriodType": "IQ_FY-4", "restatementTypeId": "LC", "metaDataTag" : "perioddate" }},
    {"function": "GDST", "identifier": "IBM:NYSE", "mnemonic": "IQ_MARKETCAP",
     "properties": {"frequency": "Monthly", "startDate": "01/01/2018", "endDate": "06/01/2018"}}]

req = {"inputRequests": req_array}

response = requests.post(endpoint_url,
                         headers={'Content-Type': 'application/json'},
                         data=json.dumps(req),
                         auth=HTTPBasicAuth(username=user_name, password=passwd),
                         verify=True)
print(response.text)


######################################

'''

{"GDSSDKResponse":
    [
    {"SnapType":"","ErrMsg":"","Headers":["IQ_TOTAL_REV"],"NumRows":1,"Seniority":"","Properties":{"periodtype":"IQ_FY"},"CacheExpiryTime":"0","StartDate":"",
        "Function":"GDSP","Identifier":"IBM:NYSE","NumCols":1,"Mnemonic":"IQ_TOTAL_REV","Frequency":"","Limit":"",
        "Rows":[{"Row":["77147.000000"]}]},
    
    {"ErrMsg":"","Headers":["IQ_EBITDA","AsOfDate"],"NumRows":5,"Seniority":"",
        "Properties":{"restatementtypeid":"LC","periodtype":"IQ_LTM", "absolutePeriodStart":"CQ12018"},
        "EndDate":"","CacheExpiryTime":"0","StartDate":"",
        "Function":"GDSHE","Identifier":"IBM:NYSE","NumCols":2,"Mnemonic":"IQ_PRICECLOSE","Frequency":"","Limit":"",
        "Rows":[{"Row":["20372.000000","1/20/2021"]},{"Row":["18551.000000","1/20/2021"]},{"Row":["16223.000000","1/20/2021"]},{"Row":["16711.000000","1/20/2021"]},{"Row":["16844.000000","1/20/2021"]}]},
    
    {"SnapType":"","ErrMsg":"","Headers":["1/31/2018","2/28/2018","3/29/2018","4/30/2018","5/31/2018"],
        "NumRows":2,"Seniority":"","Properties":{"enddate":"06/01/2018","startdate":"01/01/2018","frequency":"Monthly"},
        "CacheExpiryTime":"0",
        "Function":"GDST","Identifier":"IBM:NYSE","NumCols":5,"Mnemonic":"IQ_MARKETCAP","Limit":"",
        "Rows":[{"Row":["151552.048579","143545.592922","141334.789976","133068.685638","129718.101321"]}]}
    ]
}


'''