# Find the number of times each team won the toss and also won the match

import pandas as pd
import json

matches_csv_path = '../data/matches.csv'

# reading csv
matches_csv_read = pd.read_csv(matches_csv_path)
# get data
matches_data = matches_csv_read.to_json(orient='records')
# get it in python list
matches_data = json.loads(matches_data)

# contains team won the toss and also won the match
result ={}
for match in matches_data:
    toss_winner = match['toss_winner']
    match_winner = match['winner']
    if match_winner not in result:
        result[match_winner] = 0
    if toss_winner == match_winner:
        result[match_winner] += 1

print(result)
