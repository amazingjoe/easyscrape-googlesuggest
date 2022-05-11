# EasyScrape - Google Suggest Scraping Wrapper
# Description - Pulls Google Suggest Data for a search term
#
# Function query(search_term, [optional headers]) function returns a List of string results.
#
# Example usage:
# from easyscrape_googlesuggest import getsuggestions as ES
# for result in ES.query("Web Scraping in Python"):
#  print(result)

import requests
import json

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32"
defaultheaders = {"User-Agent":UA}

def query(term,headers = defaultheaders):    
    url_base = "https://google.com/complete/search?"
    url_client = "client=chrome&"
    url_query = f"q={term}"

    req_url = url_base+url_client+url_query

    s_results = requests.get(req_url,headers=headers)
    return json.loads(s_results.text)[1]