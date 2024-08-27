# Find a player who has won the highest number of Player of the Match awards for each season
import  pandas as pd
import json

matches_csv_path = '../data/matches.csv'
# read csv
matches_csv_read = pd.read_csv(matches_csv_path)
# get data
matches_data = matches_csv_read.to_json(orient='records')
# get data in python list
matches_data = json.loads(matches_data)

#person won highest umber of player of Match award
result ={}

for match in matches_data:
    if match['season'] not in result:
        result[match['season']] = {}
    if match['player_of_match'] not in result[match['season']]:
        result[match['season']][match['player_of_match']] = 0
    result[match['season']][match['player_of_match']] += 1


for season in result:
    player_data = result[season]
    sorted_payer_data  = sorted(player_data.items(), key=lambda x: x[1], reverse=True)
    sorted_payer_data = sorted_payer_data[:1]
    result[season] = sorted_payer_data
print(result)