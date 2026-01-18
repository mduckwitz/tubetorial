import requests

# For this tutorial, we leave this empty to remain safe for version control.
# If you have a key, you can add it here (e.g. 'YOUR_KEY') or use os.getenv('TFL_KEY')
APP_KEY = None 
BASE_URL = 'https://api.tfl.gov.uk'

def check_network_health():
    url = f"{BASE_URL}/Line/Mode/tube/Status"
    
    # We only attach the key if it exists
    params = {}
    if APP_KEY:
        params['app_key'] = APP_KEY
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        for line in data:
            status = line['lineStatuses'][0]['statusSeverityDescription']
            print(f"{line['name']}: {status}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    check_network_health()
