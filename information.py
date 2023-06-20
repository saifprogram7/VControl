import random
from serpapi import GoogleSearch
import webbrowser as wb

def informationAutomation(q):
    params = {
        "q": q,
        "location": "Seattle, Washington, United States",
        "hl": "en",
        "gl": "us",
        "google_domain": "google.com",
        "api_key":"2765c27d5d4d860f1a333f2303547c24d1b7b5edd119e6b7c9bfa659f619358c"
    }

    search = GoogleSearch(params)
    results = search.get_json()
    links = []
    for organic_result in results['organic_results']:
        entry = {
            "Link": organic_result['link'],
        }
        links.append(entry)
    raw_links = [i["Link"] for i in links if "youtube.com" not in i["Link"]]
    #print(raw_links)
    wb.open(random.choice(raw_links))