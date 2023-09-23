import requests

# API endpoint and query parameters
url = "https://sofascores.p.rapidapi.com/v1/events/shotmap"
querystring = {"event_id": "11409174"}

# Headers with API key
headers = {
    "X-RapidAPI-Key": "2e1eb0b69cmsh5536d3be5b60949p18c2b2jsn30a9f293816c",
    "X-RapidAPI-Host": "sofascores.p.rapidapi.com"
}

# Send the API request
response = requests.get(url, headers=headers, params=querystring)

# Parse the JSON response
data = response.json().get('data', [])

# Initialize a list to store shots with their xG values and times
dangerous_shots = []

# Filter and identify dangerous shots based on xG value
for shot in data:
    xg_value = shot.get('xg', 0.0)
    if xg_value > 0.1:  # You can adjust this threshold based on your criteria
        shot_time = shot.get('time', 'N/A')
        is_home_team = shot.get('isHome', False)
        team = 'home' if is_home_team else 'away'
        dangerous_shots.append((shot, xg_value, shot_time, team))

# Sort the dangerous shots by xG value (highest xG first)
dangerous_shots.sort(key=lambda x: x[2], reverse=True)

# Display information about the most dangerous shots, including time
for shot, xg_value, shot_time, team in dangerous_shots:
    player_name = shot['player']['name']
    shot_type = shot['shotType']
    xg_value = shot['xg']
    print(f"Player: {player_name}, Shot Type: {shot_type}, xG Value: {xg_value}, Time: {shot_time}, team: {team}")
