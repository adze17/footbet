import requests

url = "https://sofascores.p.rapidapi.com/v1/events/graph-points"

querystring = {"event_id": "11409174"}

headers = {
    "X-RapidAPI-Key": "2e1eb0b69cmsh5536d3be5b60949p18c2b2jsn30a9f293816c",
    "X-RapidAPI-Host": "sofascores.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

data = response.json().get('data', [])

def print_danger_attack(start_minute, end_minute, team):
    message = f"Danger attack ({team})"
    print(f"Danger Attack Started at Minute {start_minute} and Continued to Minute {end_minute}: {message}")

def check_danger_attack(team):
    danger_attack_started = False
    danger_attack_start_minute = None

    for entry in data:
        minute = entry['minute']
        value = entry['value']

        if not danger_attack_started and abs(value) > 30:
            danger_attack_started = True
            danger_attack_start_minute = minute
        elif danger_attack_started and abs(value) < 60:
            continue
        elif danger_attack_started and abs(value) >= 60:
            print_danger_attack(danger_attack_start_minute, minute, team)
            danger_attack_started = False

# Check danger attacks for both home and away teams
check_danger_attack("Home")
check_danger_attack("Away")