# https://rapidapi.com/movie-of-the-night-movie-of-the-night-default/api/streaming-availability/ 

from requests import get  # This function is how we will make requests to a server.
from requests.models import Response  # This is the type of a Response object.
import requests

genre_dict: dict[int, str] = {
    "1":"Biography", "2":"Film Noir", "3":"Game Show", "4":"Musical", "5":"Sport", "6":"Short", "7":"Adult", "12":"Adventure", "14":"Fantasy", "16":"Animation", "18":"Drama", "27":"Horror", "28":"Action", "35":"Comedy", "36":"History", "37":"Western", "53":"Thriller", "80":"Crime", "99":"Documentary", "878":"Science Fiction", "9648":"Mystery", "10402":"Music", "10749":"Romance", "10751":"Family", "10752":"War", "10763":"News", "10764":"Reality", "10767":"Talk Show"
}
genre_chosen: str = "Romance"
for key, genre in genre_dict.items():
    if genre == genre_chosen:
        genre_num: str = key
        print(f"{genre_num}")

urls = "https://streaming-availability.p.rapidapi.com/search/basic"
querystring = {"country":"us","service":"netflix","type":"series","genre":"10749","page":"1","output_language":"en","language":"en"}

headers = {
    'x-rapidapi-host': "streaming-availability.p.rapidapi.com",
    'x-rapidapi-key': "c1203a8339msh19d36a59302ebbbp1fcf1djsn5875b40ef7b7"
    }

response = requests.request("GET", urls, headers=headers, params=querystring)

print(response.text)