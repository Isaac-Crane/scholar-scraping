import json
import pandas as pd 


# Opening JSON file
f = open('scraped.json')
 
# returns JSON object as
# a dictionary
data = json.load(f)
 
# Iterating through the json
# list
array = []
for i in data:
    if 'organic_results' in i:
        for j in i["organic_results"]:
            if "publication_info" in j:
                for k in range(len(j["publication_info"]["summary"])):
                    if j["publication_info"]["summary"][k] == '-':
                        lastHyphen = k
                year = ''
                if "-" in j["publication_info"]["summary"]:
                    testYear = j["publication_info"]["summary"][lastHyphen-5]+j["publication_info"]["summary"][lastHyphen-4]+j["publication_info"]["summary"][lastHyphen-3]+j["publication_info"]["summary"][lastHyphen-2]
                    if testYear.isdigit():
                        if int(testYear) > 2018 and int(testYear) < 2024:
                            year = testYear
            if "link" in j:
                array.append([j["title"], j["link"], year])
            else:
                array.append([j["title"], '', year])

pd.DataFrame(array).to_csv('titleLinked.csv', header  = ['Paper title','Link', 'Year'], index=False)    

# Closing file
f.close()