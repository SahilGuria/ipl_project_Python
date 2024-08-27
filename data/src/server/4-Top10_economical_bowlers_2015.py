import json
from typing import overload

import pandas as pd

match_csv_path = '../data/matches.csv'
delivery_csv_path = '../data/deliveries.csv'
match_season = 2015

# read file
matches_csv_read = pd.read_csv(match_csv_path)
deliveries_csv_read = pd.read_csv(delivery_csv_path)

# get json data
matches_data = matches_csv_read.to_json(orient='records')
deliveries_data = deliveries_csv_read.to_json(orient='records')

# convert the json data to python list
matches_data = json.loads(matches_data)
deliveries_data = json.loads(deliveries_data)

bowler_economical_rate_2015 = {}

for match in matches_data:
    if match['season'] == match_season:
        match_id = match['id']
        for delivery in deliveries_data:
            if delivery['match_id'] == match_id:
                bowler_name = delivery['bowler']
                bowler_runs = delivery['total_runs']
                if bowler_name not in bowler_economical_rate_2015:
                    bowler_economical_rate_2015[bowler_name] = {'runs' : 0 , 'ball' : 0}
                bowler_economical_rate_2015[bowler_name]['runs'] += bowler_runs
                bowler_economical_rate_2015[bowler_name]['ball'] += 1

for bowler in bowler_economical_rate_2015:
    over = bowler_economical_rate_2015[bowler]['ball']/6
    economical_rate = round((bowler_economical_rate_2015[bowler]['runs']/over),2)
    bowler_economical_rate_2015[bowler] = economical_rate

# sorting by econimical rate
bowler_economical_rate_2015 = sorted(bowler_economical_rate_2015.items(), key=lambda x: x[1], reverse=False)
# taking top 10
bowler_economical_rate_2015 = bowler_economical_rate_2015[:10]
print(bowler_economical_rate_2015)

