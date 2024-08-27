# Find the bowler with the best economy in super overs

import pandas as pd

delivery_csv_path = '../data/deliveries.csv'

# Read CSV
deliveries_csv_read = pd.read_csv(delivery_csv_path)

# Filter for Super Overs (assuming 'over' indicates the over number and 'is_super_over' is a boolean flag for super overs)
super_overs = deliveries_csv_read[deliveries_csv_read['is_super_over'] == True]

# Initialize data structures to calculate economy rate
bowler_stats = {}

for _, delivery in super_overs.iterrows():
    bowler = delivery['bowler']
    runs = delivery['total_runs']

    if bowler not in bowler_stats:
        bowler_stats[bowler] = {'runs': 0, 'overs': 0}

    bowler_stats[bowler]['runs'] += runs
    bowler_stats[bowler]['overs'] += 1 / 6  # Each delivery counts as 1/6 of an over

# Calculate economy rate and find the best
best_bowler = None
best_economy_rate = float('inf')

for bowler, stats in bowler_stats.items():
    economy_rate = stats['runs'] / stats['overs']
    if economy_rate < best_economy_rate:
        best_economy_rate = economy_rate
        best_bowler = bowler

print(f"bowler :- {best_bowler} + economy-rate:- {best_economy_rate}")