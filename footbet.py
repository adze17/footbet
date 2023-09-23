import requests

# Define the base URL for fetching live event statistics
statistics_base_url = "https://sofascores.p.rapidapi.com/v1/events/statistics"
# Define the URL for fetching live events
live_events_url = "https://sofascores.p.rapidapi.com/v1/events/schedule/live"

desired_statistics = [
    'Ball possession', 'Total shots', 'Shots on target', 'Shots off target',
    'Blocked shots', 'Free kicks', 'Big chances', 'Big chances missed', 'Goals prevented', 
    'Shots inside box', 'Expected goals'
]

# Define your RapidAPI key and host
rapidapi_key = "2e1eb0b69cmsh5536d3be5b60949p18c2b2jsn30a9f293816c"
rapidapi_host = "sofascores.p.rapidapi.com"



# Define query parameters
querystring = {
    "sport_id": "1",
}

headers = {
    "X-RapidAPI-Key": rapidapi_key,
    "X-RapidAPI-Host": rapidapi_host
}

# Make an API request to fetch live events
response = requests.get(live_events_url, headers=headers, params=querystring)

# Check if the request was successful
if response.status_code == 200:
    data = response.json().get('data', [])
    
    # Filter live events for the "Premier League" tournament
    premier_league_events = [event for event in data if event['tournament']['name'] == 'Liga Portugal']
    
    # Define the list of desired statistics
extracted_statistics = {}

# Iterate through the live events of the Premier League
for event in premier_league_events:
    event_id = event['id']
    tournament_name = event['tournament']['name']
    round_info = event.get('roundInfo', {}).get('round', 'N/A')
    home_team = event['homeTeam']['name']
    away_team = event['awayTeam']['name']
    status_description = event['status']['description']

    print(f"Event ID: {event_id}")
    print(f"Tournament: {tournament_name}")
    print(f"Round: {round_info}")
    print(f"Home Team: {home_team}")
    print(f"Away Team: {away_team}")
    print(f"Status: {status_description}")

    # Make a request to fetch statistics for the current live event
    statistics_response = requests.get(
        statistics_base_url,
        headers=headers,
        params={"event_id": event_id}
    )

    # Check if the statistics request was successful
    if statistics_response.status_code == 200:
        statistics_data = statistics_response.json()
        for period_data in statistics_data['data']:
            period_name = period_data['period']
            statistics_items = period_data['groups']

            # Initialize dictionaries for home and away team statistics
            home_stats = {}
            away_stats = {}

            # Iterate through the statistics items and check if they are in the desired list
            for group in statistics_items:
                for stat_item in group['statisticsItems']:
                    stat_name = stat_item['name']
                    if stat_name in desired_statistics:
                        home_value = stat_item['home']
                        away_value = stat_item['away']
                        
                        # Store home and away values in respective dictionaries
                        home_stats[stat_name] = home_value
                        away_stats[stat_name] = away_value

            # Print the statistics for the current period
            print(f"Period: {period_name} \n")
            print(f"-------------------------")
            for stat_name in desired_statistics:
                home_value = home_stats.get(stat_name, 'N/A')
                away_value = away_stats.get(stat_name, 'N/A')
                print(f"{stat_name} - Home: {home_value}, Away: {away_value}")
            print()
    else:
        print(f"Failed to fetch statistics for event {event_id}. Status code: {statistics_response.status_code}")