#%%

import folium
import json
import requests

# %%

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:132.0) Gecko/20100101 Firefox/132.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-GB,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'api-auth': 'c3VwcG9ydCtjcHNhcHBAdmVyc2FudHVzLmNvLnVrOmt5YlRYJkZPJCEzcVBOJHlhMVgj',
    'Origin': 'https://chargeplacescotland.org',
    'Connection': 'keep-alive',
    'Referer': 'https://chargeplacescotland.org/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
}

response = requests.get('https://account.chargeplacescotland.org/api/v3/poi/chargepoint/static', headers=headers)

#%%
# Assuming the data is saved in `response.json`
data = response.json()

file_path = 'charge_points_data.json'
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)
