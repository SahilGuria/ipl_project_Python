# Number of matches won per team per year in IPL.
import json
import pandas as pd

matches_file_loction = '../data/matches.csv'

read_match = pd.read_csv(matches_file_loction)

#  convert json data
matches_json  = read_match.to_json(orient='records')

#Parse the JSON string into a Python list of dictionaries
matches_list = json.loads(matches_json)

# Number of matches won per team per year in IPL.
result = {}

for match in matches_list:
    winner = match['winner']
    season = match['season']
    if season not in result:
        result[season] = {}
    if winner not in result[season]:
        result[season][winner] = 0
    result[season][winner] += 1

print(result)