# Number of matches played per year for all the years in IPL.
import json

import pandas as pd


# file paths
csv_file_path_match = '../data/matches.csv'

csv_file = pd.read_csv(csv_file_path_match)

# json data to convert
matchesData = csv_file.to_json(orient='records')

# Parse the JSON string into a Python list of dictionaries
matchesData = json.loads(matchesData)

# data dictionary of matches played per year
result = {}

for match in matchesData:
    season = match['season']
    if season not in result:
        result[season] = 1
    else:
        result[season] += 1

print(result)
