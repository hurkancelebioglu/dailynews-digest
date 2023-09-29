import requests

api_key = "4a32e4c4421c444f8080b76a0f83f5f4"
url = "https://newsapi.org/v2/everything?q=tesla&from=2023-08-29&sortBy=publishedAt&apiKey=4a32e4c4421c444f8080b76a0f83f5f4"

request = requests.get(url)
content = request.json()

for article in content["articles"]:
    print(article["title"])
    print(article["description"])
