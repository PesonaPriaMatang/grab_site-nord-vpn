import requests
from bs4 import BeautifulSoup
import time
import random
import subprocess

# List Country On NordVPN
nord_countries = ["us", ]

# Function to change server NordVPN
def change_nordvpn_server():
    country = random.choice(nord_countries)
    print(f"Mengubah server NordVPN ke: {country}")
    subprocess.run(["your VPN Directory Drop Here!!!", "disconnect"], stdout=subprocess.PIPE)
    time.sleep(3)  # Wait Process disconnect
    subprocess.run(["your VPN Directory Drop Here!!!", "connect", country], stdout=subprocess.PIPE)
    time.sleep(5)  # Wait Stable Connection
    try:
        ip_check = requests.get("https://api.ipify.org").text
        print(f"new IP: {ip_check}")
    except:
        print("Unable to check new IP")

# List Dork Drop Here! 
dorks = [
    'inurl:".php?id=" site:.jp',
    'inurl:"index.php?page=" site:.jp',
    'inurl:admin intitle:login site:.jp',
    'inurl:".php?id=" site:.in',
    'inurl:"viewproduct.php?id=" site:.in',
    'inurl:upload.php site:.in'
]

# Function search with Google
def search_google(dork, page):
    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.google.com/search?q={dork}&start={page * 10}"
    response = requests.get(url, headers=headers)
    if response.status_code == 429:
        print("Error 429 - Too many requests, changing server...")
        change_nordvpn_server()
        time.sleep(random.uniform(30, 60))
        return search_google(dork, page)
    soup = BeautifulSoup(response.text, "html.parser")
    results = [a['href'] for a in soup.select(".tF2Cxc a") if 'href' in a.attrs]
    return results

# Function for searching with IP rotation
def search_with_nordvpn_rotation(dorks, pages=2):
    collected_urls = []
    for i, dork in enumerate(dorks):
        print(f"Searching with dork: {dork}")
        if i % 2 == 0:
            change_nordvpn_server()
        for page in range(pages):
            urls = search_google(dork, page)
            collected_urls.extend(urls)
            time.sleep(random.uniform(15, 25))
    return collected_urls

# Run Search
if __name__ == "__main__":
    result = search_with_nordvpn_rotation(dorks, pages=2)
    print("Search Results:")
    for url in result:
        print(url)
