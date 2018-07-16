from os import urandom
import pandas as pd
import json
import requests
subjects = pd.read_csv('test.csv')
data = []
for i in range(len(subjects)):

    payload = {
        'value': subjects.loc[i, "Subject Codes"],
        'label': subjects.loc[i, "Title"],
    }
    data.append(payload)

with open('new.json','w') as fp:
    json.dump(data,fp)