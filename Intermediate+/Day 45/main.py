from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/news")
data = response.text

soup = BeautifulSoup(data, "html.parser")
article_tag = soup.find_all(name="a", class_="storyLink")
article_texts = []
article_links = []
for article in article_tag:
    text = article.getText()
    article_texts.append(text)
    link = article.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
largest_number = max(article_upvote)
largest_index = article_upvote.index(largest_number)
article_upvote


# with open("Day 45\\website.html",encoding="utf8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# all_anchor_tags = soup.find_all(name="a")

# # for tag in all_anchor_tags:
# #     print(tag.get("href"))

# heading = soup.find(name="h1",id="name")
