#An application programing interface is a set of commands, functions, protocols, and objects that programmers can use to create software or interact with an external system.

import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()#it will raise an error if there is any error in the api call

data = response.json()#["iss_position"]["longitude"]
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
print(longitude,latitude)
