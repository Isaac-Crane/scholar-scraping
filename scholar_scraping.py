from serpapi import GoogleSearch
import json
import math

#Input the number of results shown when you enter your search into Google Scholar,
numberOfResults: int
#Input your exact search. Make sure to have single quotes on the outside if there are double quotes on the inside.
searchQuery: str
#Enter your API key from SERP API.
key: str

for i in range(math.ceil(numberOfResults)):
    print(i)
    params = {
        "engine": "google_scholar",
        "q": searchQuery,
        "hl": "en",
        "num": "20",
        "start": str(20*i),
        "api_key": key
    }
    search = GoogleSearch(params)
    results = search.get_dict()
    if i == 0:
        array = [results]
    else:
        array.append(results)

json_object = json.dumps(array, indent=4)
    
# Writing to sample.json
with open("scraped.json", "w") as outfile:
    outfile.write(json_object)
