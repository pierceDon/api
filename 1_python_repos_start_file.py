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

#print the keys
for key in first_repo:
    print(key)

#EXERCISE 
#print out the full name,the html url, the license name and topics
# for the first repo, List each topic one by one

print(f"Full Name: {first_repo['full_name']}")
print(f"HTML URL: {first_repo['owner']['html_url']}")
#print(f"License Name: {first_repo['license']['name']}")

for topic in first_repo['topics']:
    print(f"Topic Name: {topic}")

repo_names, stars = [], []

for repo in list_of_repos[:10]:
    repo_names.append(repo['name'])
    stars.append(repo['stargazers_count'])

from plotly.graph_objects import Bar
from plotly import offline 

data = [
    {
        "type":"bar",
        "x":repo_names,
        "y":stars,
        "marker": {
            "color": "rgb(60,100,150)",
            "line": {"width":1.5,"color": "rgb(25,25,25)"},
        },
        "opacity": 0.6
    }
]

my_layout = {
    "title": "Most starred Python Repositories on GitHub",
    "xaxis": {"title": "Repository"},
    "yaxis": {"title": "Stars"},
}

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="python_repos.html")