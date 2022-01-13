# Day33 of my 100DaysOfCode Challenge
# calling an API

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")

# to raise exceptions, if any errors in request
response.raise_for_status()

# get hold of response data from API
data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = {longitude, latitude}
print(iss_position)


