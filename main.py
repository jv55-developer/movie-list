import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_website = response.text

soup = BeautifulSoup(empire_website, "html.parser")

movie_list = soup.find_all(class_="listicleItem_listicle-item__title__hW_Kn")
movie_list_titles = []

file = open("movie_list.txt", "w")

for movie in reversed(movie_list):
    file.write(f"{movie.get_text()}\n")
