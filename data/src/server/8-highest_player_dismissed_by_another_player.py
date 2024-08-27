# Find the highest number of times one player has been dismissed by another player
import pandas as pd
import json


delivery_csv_path = '../data/deliveries.csv'

# read csv
deliveries_csv_read = pd.read_csv(delivery_csv_path)
# get data
deliveries_data = deliveries_csv_read.to_json(orient='records')
# get data in python list
deliveries_data = json.loads(deliveries_data)

result = {}
for delivery in deliveries_data:
    bowler = delivery['bowler']
    batsman = delivery['batsman']
    if bowler not in result:
        result[bowler] = {}
    if batsman not in result[bowler]:
        result[bowler][batsman] = 0
    result[bowler][batsman] += 1


# Find the highest number of dismissals by any bowler against any batsman
highest_dismissal = {'bowler': None, 'batsman': None, 'count': 0}

for bowler, batsman_data in result.items():
    for batsman, count in batsman_data.items():
        if count > highest_dismissal['count']:
            highest_dismissal['bowler'] = bowler
            highest_dismissal['batsman'] = batsman
            highest_dismissal['count'] = count


print(highest_dismissal)