import pandas as pd

# create initial records
records = [
    {'record': 1, 'a': 1, 'b': 0, 'c': 0},
    {'record': 2, 'a': 1, 'b': 0, 'c': 0},
    {'record': 3, 'a': 2, 'b': 1, 'c': 0}
]

# create records 4 through 25
for i in range(4, 26):
    a = records[-1]['a'] + records[-1]['b'] + records[-1]['c']
    b = records[-1]['a'] - records[-1]['b']
    c = records[-1]['a'] - records[-1]['b'] - records[-1]['c']

    records.append({'record': i, 'a': a, 'b': b, 'c': c})

# make a df of the results to neaten up the print
df = pd.DataFrame(records)
print(df)