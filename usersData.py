import logging
import time
from datetime import datetime
from swagger_client.rest import ApiException
import schedule
from dataProcessing import getAPIAccessToken, readXlsx, createDB

# ------------------------------------------- Functions ------------------------------------------------------

# Function to call the API to get the users info
def apiGetUsers(client, logger):
    apInfo = []
    api_instance = getAPIAccessToken(logger)    
    
    print("Calling Users")
    logger.info("Calling Users")

    for key in xlsxData.keys():
        time.sleep(1)
        api_instance = getAPIAccessToken(logger)
        apInfo.append(key)

        name = xlsxData[key].get('name')
        
        apInfo.append(name)
        apInfo.append(xlsxData[key].get('building'))
        count = api_instance.access_point_name_total_usernames_get(name).count
        apInfo.append(count)

        writeUsersOnDB(client, apInfo)
        apInfo.clear()

# Function to write the users data on the database
def writeUsersOnDB(client, info):
    # Data to send to the database
    json_payload = []

    #
    # Note: tags -> metadata about the measurement 
    #       fields -> a measurement that changes over time
    #

    data = { 
        "measurement" : "usersCount",
        "time" : datetime.now(),
        "tags" : {
            "id" : info[0],
            "ap_name" : info[1],
            "building" : info[2]
        },
        "fields" : {
            "users" : info[3]
        }
    }
    
    # Send data to the API
    json_payload.append(data)
    client.write_points(json_payload)

# ------------------------------------------ Main Function --------------------------------------------------- 

if __name__ == "__main__":

    # Creating the log file for the service
    logging.basicConfig(filename='/var/log/usersData.log', level=logging.INFO)
    logger = logging.getLogger("USERS DATA")

    # To read the data given from the xlsx file to a var
    xlsxData = readXlsx('.', 'PrimeCore.xlsx')

    # Creating the database
    client = createDB()

    # Getting the initial information about the users 
    try:
        apiGetUsers(client, logger)
    except Exception as e:
        print("Users Count Exception: " +str(e))
        logger.error("Users Count Exception: " +str(e))

    # Calling the API to get the users info every 12 minutes
    try:
        schedule.every(30).minutes.do(apiGetUsers, client, logger)
    except Exception as e:
        print("Users Count Exception: " +str(e))
        logger.error("Users Count Exception: " +str(e))

    while True:
        try:
            schedule.run_pending()
        except ApiException as e:
            logger.error("Exception: %s\n" % e)
