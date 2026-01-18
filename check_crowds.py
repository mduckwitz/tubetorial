import requests

APP_KEY = None 
BASE_URL = 'https://api.tfl.gov.uk'

def check_station_crowds(station_id):
    url = f"{BASE_URL}/Crowding/{station_id}"
    params = {'app_key': APP_KEY} if APP_KEY else {}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        print(f"Crowding Profile for Station: {station_id}")
        
        if 'daysOfWeek' in data:
            day_data = data['daysOfWeek'][0]
            print(f"Typical Crowding on {day_data['dayOfWeek']}:")
            for slot in day_data['timeBands'][:5]: 
                busy_percent = slot['percentageOfBaseLine'] * 100
                print(f"  {slot['timeBand']}: {busy_percent:.1f}% load")
        else:
            print("No crowd profile data available.")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    STATION_ID = "940GZZLUOXC" # Oxford Circus
    check_station_crowds(STATION_ID)