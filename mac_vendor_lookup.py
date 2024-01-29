import requests

mac_address = "	00:00:00:00:00:00"
url = f"https://api.macvendors.com/{mac_address}"

try:
    response = requests.get(url)
    response.raise_for_status() 
    
    if response.text:
        print(f"Vendor: {response.text}")
    else:
        print("Not Found")

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
