import requests
import urllib3
import sys
 
urllib3.disable_warnings()
 
def fetch_IP_hydra(hostname):
    hydra_search_url = "https://hydra.xxxx.xx.com/api/9.0/ip/search"
    bearer_token = '01xxxxxxxx'  # Replace with your real token
 
    headers = {
        "Authorization": bearer_token,
        "Content-Type": "application/json"
    }
 
    body = {
        "dns_entry": hostname
    }
 
    try:
        response = requests.post(
            hydra_search_url,
            json=body,
            headers=headers,
            verify=False
        )
        response.raise_for_status()
 
        data = response.json()
        results = data.get("result", [])
 
        if results:
            for entry in results:
                print(f"Ip address: {entry['ip_addr']}, Dns entry: {entry['dns_entry']}")
        else:
            print(f"⚠️ No IPs found for hostname: {hostname}")
    except Exception as e:
        print(f"❌ Error occurred while fetching IP for {hostname}: {e}")
        sys.exit(1)
 
# Accept multiple comma-separated hostnames
if __name__ == "__main__":
    input_string = input("Enter hostname(s) separated by commas: ").strip()
    hostnames = [h.strip() for h in input_string.split(',') if h.strip()]
 
    if not hostnames:
        print("No valid hostnames entered.")
        sys.exit(1)
 
    for host in hostnames:
        print(f"\n🔍 Checking: {host}")
        fetch_IP_hydra(host)
