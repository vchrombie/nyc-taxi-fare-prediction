import os
import requests
from bs4 import BeautifulSoup


url = "https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

yellow_taxi_links = soup.find_all("a", title="Yellow Taxi Trip Records")

# Create the 'data' folder if it doesn't exist
if not os.path.exists("data"):
    os.makedirs("data")

for link in yellow_taxi_links:
    file_url = link["href"]
    file_name = file_url.split("/")[-1]

    # Save the files in the 'data' folder
    file_path = os.path.join("data", file_name)

    print(f"Downloading {file_name}...")
    
    with requests.get(file_url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    print(f"{file_name} downloaded successfully.")
