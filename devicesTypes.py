import logging
import time
from datetime import datetime
from swagger_client.rest import ApiException
import schedule
from dataProcessing import getAPIAccessToken, readXlsx, createDB

# ------------------------------------------- Functions ------------------------------------------------------

# Function to call the API to get the devices types
def apiGetDevices(client, logger):
    devicesInfo = []
    api_instance = getAPIAccessToken(logger)    
    
    print("Calling Devices Types")
    logger.info("Calling Devices Types")

    for key in xlsxData.keys():
        time.sleep(1)
        api_instance = getAPIAccessToken(logger) 
        devicesInfo.append(key)

        name = xlsxData.get(key).get("name")
        devicesInfo.append(name)

        devicesInfo.append(xlsxData.get(key).get("building"))

        devicesResponse = api_instance.access_point_name_device_type_count_get(name)
        dic = formatResponse(devicesResponse)

        if dic != None:
            devicesInfo.append(dic.get("android"))
            devicesInfo.append(dic.get("ios"))
            devicesInfo.append(dic.get("laptop"))

            writeDevicesOnDB(client, devicesInfo)
            devicesInfo.clear()

# Function to format the response getted from te API
def formatResponse(response):
    android = 0 
    ios = 0
    laptop = 0

    if response.device_type_counts != None:
        for device in response.device_type_counts:
            # Getting the number of laptops 
            if "Unclassified" in device.device_type:
                laptop += device.count
            if "Intel-Device" in device.device_type:
                laptop += device.count
            if "Microsoft-Device" in device.device_type:
                laptop += device.count
            if "Unknown" in device.device_type:
                laptop += device.count

            # Getting the number of android devices 
            if "Samsung" in device.device_type:
                android += device.count
            if "Huawei" in device.device_type:
                android += device.count
            if "ZTE" in device.device_type:
                android += device.count
            if "ASUS" in device.device_type:
                android += device.count
            if "MotorolaMobile" in device.device_type:
                android += device.count
            if "LG" in device.device_type:
                android += device.count
            if "Sony" in device.device_type:
                android += device.count
            
            # Getting the number of ios devices 
            if "Apple" in device.device_type:
                ios += device.count
            if "iPhone" in device.device_type:
                ios += device.count
            if "iPad" in device.device_type:
                ios += device.count

    # print(type(laptop))
    # print(type(ios))
    # print(type(android))

        return {
            "laptop": int(laptop),
            "ios": int(ios),
            "android": int(android)
        }

    return None

# Function to write the devices types on the database
def writeDevicesOnDB(client, info):
    # Data to send to the database
    json_payload = []

    #
    # Note: tags -> metadata about the measurement 
    #       fields -> a measurement that changes over time
    #

    data = { 
        "measurement" : "devicesTypes",
        "time" : datetime.now(),
        "tags" : {
            "id" : info[0],
            "ap_name" : info[1],
            "building" : info[2]
        },
        "fields" : {
            "android" : info[3],
            "ios" : info[4],
            "laptop" : info[5]
        }
    }
    
    # Send data to the API
    json_payload.append(data)
    client.write_points(json_payload)

# ------------------------------------------ Main Function --------------------------------------------------- 

if __name__ == "__main__":

    # Creating the log file for the service
    logging.basicConfig(filename='/var/log/devicesTypes.log', level=logging.INFO)
    logger = logging.getLogger("DEVICES TYPES")

    # To read the data given from the xlsx file to a var
    xlsxData = readXlsx('.', 'PrimeCore.xlsx')

    # Creating the database
    client = createDB()

    # Getting the initial information about the metrics 
    try:
        apiGetDevices(client, logger)
    except Exception as e:
        print("Devices types Exception: " +str(e))
        logger.error("Devices types Exception: " +str(e))

    # Calling the API to get the metrics info every 8 minutes
    try:
        schedule.every(30).minutes.do(apiGetDevices, client, logger)
    except Exception as e:
        print("Devices types Exception: " +str(e))
        logger.error("Devices types Exception: " +str(e))

    while True:
        try:
            schedule.run_pending()
        except ApiException as e:
            logger.error("Exception: %s\n" % e)