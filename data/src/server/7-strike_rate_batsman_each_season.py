# Find the strike rate of a batsman for each season
import pandas as pd
import json

matches_csv_path = '../data/matches.csv'
delivery_csv_path = '../data/deliveries.csv'

# read csv
matches_csv_read = pd.read_csv(matches_csv_path)
deliveries_csv_read = pd.read_csv(delivery_csv_path)
# get data
matches_data = matches_csv_read.to_json(orient='records')
deliveries_data = deliveries_csv_read.to_json(orient='records')
# get data in python list
matches_data = json.loads(matches_data)
deliveries_data = json.loads(deliveries_data)

result = {}

for match in matches_data:
    match_id = match['id']
    season = match['season']
    if season not in result:
        result[season] = {}
    for delivery in deliveries_data:
        if delivery['match_id'] == match_id:
            batsman  = delivery['batsman']
            runs = delivery['batsman_runs']
            if batsman not in result[season]:
                result[season][batsman] = {'runs' : 0 , 'balls' : 0}
            result[season][batsman]['runs'] += runs
            if delivery['wide_runs'] == 0 and delivery['noball_runs'] ==0:
                result[season][batsman]['balls'] += 1

for season in result:
    batsman_data = result[season]
    for batsman in batsman_data:
        over  = batsman_data[batsman]['balls'] /6
        strike_rate = batsman_data[batsman]['runs'] / over
        result[season][batsman] = round(strike_rate,2)

print(result)