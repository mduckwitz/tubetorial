import requests

APP_KEY = None 
BASE_URL = 'https://api.tfl.gov.uk'

def search_station(query):
    url = f"{BASE_URL}/StopPoint/Search"
    
    params = {
        'query': query,
        'modes': 'tube' # Limit results to Tube stations
    }
    if APP_KEY:
        params['app_key'] = APP_KEY
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        matches = data.get('matches', [])
        
        if not matches:
            print(f"No stations found for '{query}'")
            return

        print(f"Found {len(matches)} results:")
        for match in matches:
            print(f"  Name: {match['name']}")
            print(f"  ID:   {match['id']}")
            print("-" * 20)
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    # Simple CLI input for testing
    user_input = input("Enter station name to search: ")
    search_station(user_input)
