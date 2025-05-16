from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from datetime import datetime

app = Flask(__name__)

def get_verge_headlines():
    url = "https://www.theverge.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    articles = soup.find_all("h2", class_="group-hover:shadow-underline-franklin")

    headlines = []
    for article in articles:
        title = article.get_text(strip=True)
        link = article.find_parent("a")["href"]
        headlines.append({"title": title, "url": link})

    return headlines

@app.route('/')
def home():
    headlines = get_verge_headlines()
    return render_template("index.html", headlines=headlines)

if __name__ == '__main__':
    app.run(debug=True)

