import pandas as pd
import json

matches_csv_path = '../data/matches.csv'
delivery_csv_path = '../data/deliveries.csv'

matches_csv_read = pd.read_csv(matches_csv_path)
deliveries_csv_read = pd.read_csv(delivery_csv_path)

# get data in json
matches_data = matches_csv_read.to_json(orient='records')
deliveries_data = deliveries_csv_read.to_json(orient='records')

# convert to python list
matches_data = json.loads(matches_data)
deliveries_data = json.loads(deliveries_data)

result = {}
for match in matches_data:
    match_id = match['id']
    season = match['season']

    #     putting year and team
    if season not in result:
        result[season] = {}

    for delivery in deliveries_data:
        bowler_team = delivery['bowling_team']
        extra_run = delivery['extra_runs']

        if bowler_team not in result[season]:
            result[season][bowler_team] = 0

        if delivery['match_id'] == match_id:
            result[season][bowler_team] += extra_run

print(result)
