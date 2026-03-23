import requests

parameters = {
    "q" : "python",
    "sort" : "stars",
    "order" : "desc",
    "per_page" : 5
}

response = requests.get("https://api.github.com/search/repositories", params=parameters)

data = response.json()

items = data["items"]
for i in items:
    print("Repos:",i["name"])
    print("Stars:",i["stargazers_count"])