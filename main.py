import requests
from send_email import send_email

topic = "tesla"
api_key = "4a32e4c4421c444f8080b76a0f83f5f4"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-08-29&" \
      "sortBy=publishedAt&" \
      "apiKey=4a32e4c4421c444f8080b76a0f83f5f4&" \
      "language=en"

request = requests.get(url)
content = request.json()

body = ""
for article in content["articles"][:20]:
    if article["title"] is not None:
        body = "Subject: Today's news" + "\n" + body + article["title"] \
               + "\n" + article["description"] + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(message=body)
