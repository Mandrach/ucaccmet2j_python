import csv
import json


# 3. Automating everything
# 
#with open ('stations.csv') as csv_file:
    #csv_file = csv_file.read()
    #csv_file = file_contents.split(',')

    #file_dict = {}         # initialize  dictionary
    #headers = csv_file.readline() # read  first  line  and  move  pointer to  second  line
    #for  line in csv_file:        # for  2nd  line  onward
    #    location, state, station = line.strip().split(',') #remove white space  and  then  split  by  comma
    #    file_dict[location] = {
    #        'station': station,
    #        'state': state
    #    }

    #for location in file_dict
    #    if file_dict[location] == 'Seattle'
    #        print(file_dict[location])


# 1. load in json data & find 
with open ('precipitation.json') as json_file:
    precipitation_data = json.load(json_file)
    # Use this station code to select all the measurements belonging to it from the JSON data
    # GHCND:US1WAKG0038
    #precipitation_dict = {}
    station_code = 'GHCND:US1WAKG0038'

    for measurement in precipitation_data:
        if measurement['station'] == station_code:
            print(measurement['value'])




# 2. Sum all measurements and save them in a list
    # We have to go through the data, check for the station, and then sort by date. 
    # 1. does already go through all the data. But how to sort by date?
    # 


    # how can I split the date by month? 

    # measurement_of_station = []
    # for measurement in precipitation_data:
    #     if measurement['station'] == station_code
    #     # measurement['date'].split('-') ?
    # #      while measurement['date'] 
    # #     measurement_of_station[measurement] += measurement['value']
    #     else 


