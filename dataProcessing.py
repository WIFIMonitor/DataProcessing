from __future__ import print_function
from os.path import split
import swagger_client, requests, openpyxl, math, schedule, sys, logging
from pathlib import Path
from swagger_client.rest import ApiException
from requests.auth import HTTPBasicAuth
from influxdb import InfluxDBClient
from datetime import datetime

# -------------------------------- Saving data from the xlsx file to a Dict ----------------------------------

# Function to read the data given from the xlsx file
def readXlsx(dir, fileName):
    # Setting the path to the xlsx file:
    xlsx_file = Path(dir, fileName)

    # Read the Excel File
    wb_obj = openpyxl.load_workbook(xlsx_file)

    # Read the Active Sheet from the Excel file
    sheet = wb_obj.active

    # Max rows
    # print(("Number of rows: %d") % (sheet.max_row))

    accessPoints = {}
    i = 0
    for row in sheet.iter_rows(max_col=7, values_only=True):
        if (i != 0):
            id = row[0]
            apData = {
                'location' : row[1],
                'name' : row[2],
                'latitude' : row[3],
                'longitude' : row[4],
                'responsible' : row[5],
                'building' : row[6] 
            }
            accessPoints[id] = apData
        i+=1

    return accessPoints

# ------------------------------------------- Functions ------------------------------------------------------

# Function to get the API access token (expires each hour)
def getAPIAccessToken(logger):
    # Getting the access token
    url = 'https://wso2-gw.ua.pt/token?grant_type=client_credentials&state=123&scope=openid'
    header = {'Content-Type': 'application/x-www-form-urlencoded'}

    x = requests.post(url,headers=header,auth=HTTPBasicAuth('***REMOVED***','***REMOVED***'))
    resp = x.json()

    # Configure OAuth2 access token for authorization
    swagger_client.configuration.access_token = resp["access_token"]

    print("token: "+str(swagger_client.configuration.access_token))
    logger.info("token: "+str(swagger_client.configuration.access_token))

    # create an instance of the API class
    api_instance = swagger_client.DefaultApi() 

    return api_instance 

# Function to create the database
def createDB():
    client = InfluxDBClient("localhost", 8086, str(sys.argv[1]), str(sys.argv[2]), "***REMOVED***")
    client.create_database("***REMOVED***")
    client.get_list_database()
    client.switch_database("***REMOVED***")

    return client

# Function to get access points Info
def getAccessPoints(client, numReq, api_instance):
    apInfo = []
    numReq = numReq * 100;

    api_response = api_instance.access_point_get(first_result=numReq)

    # Get the first index
    firstIndex = int(api_response.first)

    # Get the last index
    lastIndex = int(api_response.last)

    # Get the access points list
    resp = api_response.access_points

    stackSize = lastIndex - firstIndex
    for i in range(0, stackSize + 1):
        apInfo.append(int(resp[i].id))
        apInfo.append(resp[i].name)    
        
        keys = xlsxData.keys()

        # Get the building by the id
        if(apInfo[0] in keys):
            building = xlsxData[apInfo[0]].get('building')
        # If a new access point is turned on
        else:
            id = int(resp[i].id)
            newRequest = api_instance.access_point_id_get(id)
            splits = newRequest.name.split('-')

            apData = {
                'location' : newRequest.location,
                'name' : newRequest.name,
                'latitude' : None,
                'longitude' : None,
                'responsible' : None,
                'building' :  splits[0]
            }

            # Save new access point data into the dict 
            xlsxData[id] = apData
            building = splits[0]

            # Write the new access point data into the xlsx file
            writeXlsx('.', 'PrimeCore.xlsx', id, apData)

        apInfo.append(building)
        apInfo.append(int(resp[i].client_count))    
        apInfo.append(int(resp[i].client_count_2_4_g_hz))
        apInfo.append(int(resp[i].client_count_5_g_hz))    

        # Write on database
        writeAccessPointsOnDB(client, apInfo)

        # Clearing the list of access points Info
        apInfo.clear()

# Function to write the new access point data into the xlsx file
def writeXlsx(dir, fileName, id, apData):
    # Setting the path to the xlsx file:
    xlsx_file = Path(dir, fileName)

    # Read the Excel File
    wb_obj = openpyxl.load_workbook(xlsx_file)

    # Read the Active Sheet from the Excel file
    sheet = wb_obj.active

    maxRows = sheet.max_row
    
    col = sheet["A" + str(maxRows+1)]
    col.value = id 
    
    list = []
    for key in apData.keys():
        list.append(key)

    cols = ["B","C","D","E","F","G"]
    for i in range(0, len(cols)):
        col = sheet[cols[i] + str(maxRows+1)]
        col.value = apData.get(list[i])

    wb_obj.save("./PrimeCore.xlsx")

# Function to write the access points Info on the database
def writeAccessPointsOnDB(client, info):
    # Data to send to the database
    json_payload = []

    #
    # Note: tags -> metadata about the measurement 
    #       fields -> a measurement that changes over time
    #

    data = { 
        "measurement" : "clientsCount",
        "time" : datetime.now(),
        "tags" : {
            "id" : info[0],
            "name" : info[1],
            "building" : info[2]
        },
        "fields" : {
            "clientsCount" : info[3],
            "clientsCount2_4Ghz" : info[4],
            "clientsCount5Ghz" : info[5]
        }
    }

    # Send data to the API
    json_payload.append(data)
    client.write_points(json_payload)

# Function to call the API to get the access points
def apiGetAccessPoint(client, logger):
    api_instance = getAPIAccessToken(logger)
    print("Calling Access Points")
    logger.info("Calling Access Points")

    # To get the total number of working access points
    apsCount = int(api_instance.access_point_count_get().count)

    # Defining the number os API requests needed
    numberReq = math.ceil(apsCount / 100)

    for index in range (0, numberReq):
        # Calling function to get the access points info
        getAccessPoints(client, index, api_instance)

# ------------------------------------------ Main Function --------------------------------------------------- 

if __name__ == "__main__":

    # Data given from the xlsx file
    xlsxData = readXlsx('.', 'PrimeCore.xlsx')

    # Creating the log file for the service
    logging.basicConfig(filename='/var/log/dataProcessing.log', level=logging.INFO)
    logger = logging.getLogger("DATA PROCESSING")

    # Creating the database
    client = createDB()

    # Getting the initial information about the access points
    try:
        apiGetAccessPoint(client, logger)
    except Exception as e:
        print("Access Point Exception: " +str(e))
        logger.error("Access Point Exception: " +str(e))

    # Calling the API to get the access points every 15 minutes
    try:
        schedule.every(15).minutes.do(apiGetAccessPoint, client)
    except Exception as e:
        print("Access Point Exception: " +str(e))
        logger.error("Access Point Exception: " +str(e))

    while True:
        try:
            schedule.run_pending()
        except ApiException as e:
            logger.error("Exception: %s\n" % e)