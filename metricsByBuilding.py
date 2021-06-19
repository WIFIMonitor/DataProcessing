import logging
from datetime import datetime
from swagger_client.rest import ApiException
import schedule
import time
from dataProcessing import getAPIAccessToken, createDB

# ------------------------------------------- Functions ------------------------------------------------------

# Function to call the API to get the building metrics info
def apiGetMetrics(client, logger):
    buildingInfo = []
    api_instance = getAPIAccessToken(logger)    
    
    print("Calling Metrics")
    logger.info("Calling Metrics")

    # Getting the buildings list from the API
    buildings = api_instance.building_get().buildings
    
    # These buildings put the API in a timeout state
    buildings.remove("STIC") # Está a retornar vazio
    buildings.remove("LABTEC") # Está a retornar vazio
    buildings.remove("RALUNOS") # Não funciona
    buildings.remove("EDIF3") # Está a retornar vazio
    buildings.remove("AAUAV")
    #--------------------------------------------------

    for build in buildings:
        time.sleep(1)
        api_instance = getAPIAccessToken(logger)
        buildingInfo.append(build)
        rx_response = api_instance.network_metric_building_get(build, "rx")
        rx = formatResponse(rx_response)
        buildingInfo.append(rx)
        
        tx_response = api_instance.network_metric_building_get(build, "tx")        
        tx = formatResponse(tx_response)
        buildingInfo.append(tx)

        writeMetricsOnDB(client, buildingInfo)
        buildingInfo.clear()


# Function to format the response getted from te API
def formatResponse(response):
    tot = 0

    # Getting the number of values  
    size = len(response.metrics_data.values)
    
    lst = []
    for i in range(1, 4):
        # Obtain the last 3 measurement 
        dic = response.metrics_data.values[size-i].y_values.to_dict()
        valueList = list(dic.values())

        newStr = str(valueList[0]).replace("]", "")
        final = newStr.replace("[", "")
        splits = final.split(".")

        lst.append(int(splits[0]))

    for elem in lst:
        tot += elem 

    return tot

# Function to write the metrics data on the database
def writeMetricsOnDB(client, info):
    # Data to send to the database
    json_payload = []

    #
    # Note: tags -> metadata about the measurement 
    #       fields -> a measurement that changes over time
    #

    data = { 
        "measurement" : "metricsBuildingCount",
        "time" : datetime.now(),
        "tags" : {
            "building" : info[0]
        },
        "fields" : {
            "rx" : info[1],
            "tx" : info[2]
        }
    }
    
    # Send data to the API
    json_payload.append(data)
    client.write_points(json_payload)

# ------------------------------------------ Main Function --------------------------------------------------- 

if __name__ == "__main__":

    # Creating the log file for the service
    logging.basicConfig(filename='/var/log/metricsByBuilding.log', level=logging.INFO)
    logger = logging.getLogger("METRICS BY BUILDING")

    # Creating the database
    client = createDB()

    # Getting the initial information about the metrics 
    try:
        apiGetMetrics(client, logger)
    except Exception as e:
        print("Building metrics Exception: " +str(e))
        logger.error("Building metrics Exception: " +str(e))

    # Calling the API to get the metrics info every 15 minutes
    try:
        schedule.every(20).minutes.do(apiGetMetrics, client, logger)
    except Exception as e:
        print("Building metrics Exception: " +str(e))
        logger.error("Building metrics Exception: " +str(e))

    while True:
        try:
            schedule.run_pending()
        except ApiException as e:
            logger.error("Exception: %s\n" % e)