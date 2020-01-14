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
            pass
            #print(measurement['value'])
        
# 2. Sum all measurements and save them in a list
    # We have to go through the data, check for the station, and then sort by date. 


    measurement_of_station = [ # creating a list of twelf zeros, one vessel for each month
        0
    ]*12
    # going through the data set and calculating the sum of precipitation for each month
    for measurement in precipitation_data:
        date_parsed = measurement['date'].split('-')
        if measurement['station'] == station_code:              # checks for the correct station
            for month in range(len(measurement_of_station)):    # 12 months, 12 sums...
                if int(date_parsed[1]) == month+1:              # string difficult, int easy
                    measurement_of_station[month] += measurement['value'] # creating the sum for current month

# save the result as a json file
#with  open(’myJSONfile.json’, ’w’) as f:
    # open  JSON  file3json.dump(my_dictionary 
 #   , f, indent=4, sort_keys=True)

# Part 2
    # Nr. 1 - Percipitation value for the whole year
percipitation_year = sum(measurement_of_station)
print(f'The percipitation for the year is: {percipitation_year}')

    # Nr. 2 - Calculate the relative precipitation per month 
    # (percentage compared to the precipitation over the whole year)

# a dictionary which should contain 12 entries, representing the relative value for each month
# month is the key, the relative value of the calculation is the value
relative_per_month = {} 
for month in range(len(measurement_of_station)):
    relative_per_month[month] = measurement_of_station[month] / percipitation_year
print(f'The relative percipitation for each month for the station Seattle is: {relative_per_month}. Legend: 0 = January, 1 = February, etc.')
    



    
        


