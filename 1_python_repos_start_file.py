import requests
import json

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

outfile = open('output.json','w')

response_dict = r.json()

json.dump(response_dict,outfile,indent=4) 

list_of_repos = response_dict['items']

print(f"Number of repos: {len(list_of_repos)}")

#how many keys are in each dictionary 
first_repo = list_of_repos[0]

print(f"Number of keys: {len(first_repo)}")