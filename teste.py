from __future__ import print_function
import time
import swagger_client
import requests
from swagger_client.rest import ApiException
from pprint import pprint
from requests.auth import HTTPBasicAuth



url = 'https://wso2-gw.ua.pt/token?grant_type=client_credentials&state=123&scope=openid'
header = {'Content-Type': 'application/x-www-form-urlencoded'}

x = requests.post(url,headers=header,auth=HTTPBasicAuth('***REMOVED***','***REMOVED***'))
resp = x.json()

# Configure OAuth2 access token for authorization: default
swagger_client.configuration.access_token = resp["access_token"]
# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_response = api_instance.access_point_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->access_point_count_get: %s\n" % e)
