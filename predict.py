import requests

url = "https://sofascores.p.rapidapi.com/v1/events/predict"

querystring = {"event_id":"11352630"}

headers = {
	"X-RapidAPI-Key": "2e1eb0b69cmsh5536d3be5b60949p18c2b2jsn30a9f293816c",
	"X-RapidAPI-Host": "sofascores.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())