import csv
import json


#3. Automating everything
# 
with open ('stations.csv') as csv_file:
    csv_file = csv_file.read()
    csv_file = file_contents.split(',')

    file_dict = {}         # initialize  dictionary
    headers = csv_file.readline() # read  first  line  and  move  pointer to  second  line
    for  line in csv_file:        # for  2nd  line  onward
        location, state, station = line.strip().split(',') #remove white space  and  then  split  by  comma
        file_dict[location] = {
            'station': station,
            'state': state
        }
for file_dict[location] in file_dict
           # print(file_dict[location])

    # 1. load in json data & find 
    with open ('precipitation.json') as json_file:
        precipitation_data = json.load(json_file)
        # Use this station code to select all the measurements belonging to it from the JSON data
        #precipitation_dict = {}
        station_code = file_dict[station]
            for measurement in precipitation_data:
                if measurement['station'] == station_code:
                    print(measurement['value'])
    
    # 2. Sum all measurements and save them in a list
    # We have to go through the data, check for the station, and then sort by date.  
        measurement_of_station = []
        measurement['date'].split('-')
            for measurement in precipitation_data:
                if measurement['station'] == station_code:
                    for month in measurement['date']:
                        while measurement['date'][2] == month:
                            measurement_of_station[measurement] += measurement['value']
        print(measurement_of_station)

    	# save the result as a json file


    # Part 3
    # Nr. 1 - Percipitation value for the whole year
    percipitation_year = sum(measurement_of_station[2])
    print(f'The relative percipitation per year for station {file_dict[station]} is {percipitation_year}')

    # Nr. 2 - Calculate the relative precipitation per month 
    # (percentage compared to the precipitation over the whole year)

    # a dictionary which should contain 12 entries, representing the relative value for each month
    # month is the key, the relative value of the calculation is the value
    relative_per_month = {} 
    for month in measurement_of_station:
        relative_per_month[month] = measurement_of_station[month] / percipitation_year
    print(relative_per_month)
    



    
        


