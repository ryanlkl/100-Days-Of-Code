import requests
from bs4 import BeautifulSoup

URL ="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

movies = soup.find_all(name="h3",class_="title")
movies_text = [movie.getText() for movie in movies]
movies_text = movies_text[::-1]

with open("Day 45\\Top Movies\\top_movies.txt","w",encoding="utf-8") as movie_file:
    for movie in movies_text:
        movie_file.write(f"{movie}\n")
