import pandas as pd
import requests
import os

BASE_URL="https://www2.calrecycle.ca.gov/LGCentral/DisposalReporting/Destination/DisposalByFacility"
df = pd.read_csv("jurisdictions.csv")

YEARS = range(1998, 2021)
for year in YEARS:
    if not os.path.exists('files/{}'.format(year)):
        os.makedirs('files/{}'.format(year))
    print(year)
    for idx, row in df.iterrows():
        name = row['name'].replace("/", "-")
        file_path = 'files/{}/{}_{}.xls'.format(year, row['id'], name)
        if os.path.exists(file_path):
            continue
        print(row['id'], name)
        data = {
            "Year": year,
            "JurisdictionSelections": row['id'],
            "JurisdictionID": row['id'],
            "ReportFormat": 'XLS'
        }
        r = requests.post(BASE_URL, data)
        with open(file_path, 'wb') as f:
            f.write(r.content)
        # break
    # break
