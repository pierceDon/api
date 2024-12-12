import requests
import json


#random chuch norris jokes
url = "https://api.chucknorris.io/jokes/random"


#list of categories
url = "https://api.chucknorris.io/jokes/categories"


#random joke from a specific category
url = "https://api.chucknorris.io/jokes/random?category={category}"


#text search
url = "https://api.chucknorris.io/jokes/search?query={query}"




'''
Part I
The program should welcome the user by displaying a random chuch norris joke
'''
print("Hello! Welcome to all things Chuck Norris!")
url = "https://api.chucknorris.io/jokes/random"
r = requests.get(url)

obj = r.json()
print(obj['value'])


'''
Part II
list the categories to the user and ask to pick a category
'''
url = "https://api.chucknorris.io/jokes/categories"
r = requests.get(url)
obj = r.json()

for cat in obj:
    print(cat)

ans = input("Please select a category from the list: ")



'''
Part III
Display a joke based on the category picked by the user
'''

url = f"https://api.chucknorris.io/jokes/random?category={ans}"
r = requests.get(url)
obj = r.json()

print(obj['value'])



'''
Part IV
See if you can find a match for the user's favorite chuck norris joke
by asking the user to enter in a few key words of the joke
'''

response = input(f"Do you have a favorite Chuck Norris joke? \nType in some key words and I'll try to guess it!")

url = "https://api.chucknorris.io/jokes/search?query={response}"
r = requests.get(url)
obj = r.json()

print("Here it is!")
print(obj['result'][0]['value'])