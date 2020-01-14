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
    precipitation_data = json_file.read()
    # Use this station code to select all the measurements belonging to it from the JSON data
    # GHCND:US1WAKG0038
    #precipitation_dict = {}
    station_code = 'GHCND:US1WAKG0038'

    for measurement in precipitation_data:
        if precipitation_data[measurement][station == station_code]:
            print(precipitation_data[measurement][value])


