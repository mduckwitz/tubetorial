import requests

APP_KEY = None 
BASE_URL = 'https://api.tfl.gov.uk'

def get_live_arrivals(station_id):
    # Endpoint: /StopPoint/{id}/Arrivals
    url = f"{BASE_URL}/StopPoint/{station_id}/Arrivals"
    
    params = {}
    if APP_KEY:
        params['app_key'] = APP_KEY
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        arrivals = response.json()
        
        if not arrivals:
            print("No arrivals predicted at this moment.")
            return

        # Sort arrivals by time (ascending)
        # 'timeToStation' is in seconds
        sorted_arrivals = sorted(arrivals, key=lambda x: x['timeToStation'])

        print(f"Live Arrivals for Station ID: {station_id}")
        print(f"{'Line':<15} {'Destination':<25} {'Time':<10}")
        print("-" * 50)

        for train in sorted_arrivals:
            line_name = train['lineName']
            destination = train['destinationName']
            # Convert seconds to minutes for display
            minutes = train['timeToStation'] // 60
            
            # Formatting "0 mins" as "Due" is a nice touch
            time_str = "Due" if minutes == 0 else f"{minutes} min"

            print(f"{line_name:<15} {destination:<25} {time_str:<10}")
            
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    # Oxford Circus ID (from our previous step)
    STATION_ID = "940GZZLUOXC" 
    get_live_arrivals(STATION_ID)
