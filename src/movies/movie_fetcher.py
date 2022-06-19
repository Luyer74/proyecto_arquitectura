from unicodedata import name
import requests
import re
import csv
from movies import models
from movie_dict import SimpleExpFac
import pandas as pd
from bs4 import BeautifulSoup


def insert():
    data = pd.read_csv("/src/movies/movie_results.csv")
    data['movie_id'] = data.index
    try:
        data.to_sql(con=models.engine, name="movies",
                    if_exists="replace", index=False)
        print("movies updated!")
    except:
        print("error jeje")


def main():
    # Downloading imdb top 250 movie's data
    url = 'http://www.imdb.com/chart/top'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')

    movies = soup.select('td.titleColumn')
    links = [a.attrs.get('href') for a in soup.select('td.titleColumn a')]
    crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
    ratings = [b.attrs.get('data-value')
               for b in soup.select('td.posterColumn span[name=ir]')]
    votes = [b.attrs.get('data-value')
             for b in soup.select('td.ratingColumn strong')]

    # create a empty list for storing
    # movie information
    list = []

    # Iterating over movies to extract
    # each movie's details
    for index in range(0, len(movies)):
        # Separating movie into: 'place',
        # 'title', 'year'
        movie_string = movies[index].get_text()
        movie = (' '.join(movie_string.split()).replace('.', ''))
        movie_title = movie[len(str(index)) + 1:-7]
        year = re.search('\((.*?)\)', movie_string).group(1)
        place = movie[:len(str(index)) - (len(movie))]

        data = {"movie_title": movie_title,
                "year": year,
                "place": place,
                "star_cast": crew[index],
                "rating": ratings[index],
                "vote": votes[index],
                "link": links[index],
                "preference_key": index % 4 + 1}
        list.append(data)

    exporter = SimpleExpFac.createExporter('csv')
    exporter.save(list)


if name == '__main__':
    main()
