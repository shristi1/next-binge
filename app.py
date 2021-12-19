from flask import Flask, render_template, request
from requests import get
from random import choice, randint
from requests import get  # This function is how we will make requests to a server.
from requests.models import Response  # This is the type of a Response object.
import requests

app = Flask(__name__)

genre_dict: dict[int, str] = {
    "1":"Biography", "2":"Film Noir", "3":"Game Show", "4":"Musical", "5":"Sport", "6":"Short", "7":"Adult", "12":"Adventure", "14":"Fantasy", "16":"Animation", "18":"Drama", "27":"Horror", "28":"Action", "35":"Comedy", "36":"History", "37":"Western", "53":"Thriller", "80":"Crime", "99":"Documentary", "878":"Science Fiction", "9648":"Mystery", "10402":"Music", "10749":"Romance", "10751":"Family", "10752":"War", "10763":"News", "10764":"Reality", "10767":"Talk Show"
}


@app.route("/", methods=["GET", "POST"])
async def index():
    if request.method == "POST":    # Index.html receives info from user and POSTS it to our flask app!

        # Here is where we can set variables used by both random and dropdown methods
        genre_chosen: str = str(request.form['genre']) #
        for key, genre in genre_dict.items():
            if genre == genre_chosen:
                genre_num: str = key

        stream_chosen: str = str(request.form['streaming'])
        
        show_length: str = str(request.form['season'])

        show_num_min: int
        show_num_max: int
        if show_length == "three_or_less": # 1, 2, 3
            show_num_min = 1
            show_num_max = 3
        else:
            if show_length == "four_to_six": #4,5,6
                show_num_min = 4
                show_num_max = 6
            else:
                show_num_min = 7
                show_num_max = 50
                
        urls = "https://streaming-availability.p.rapidapi.com/search/basic"
        querystring = {"country":"us","service":{stream_chosen},"type":"series","genre":{genre_num},"page":"1","output_language":"en","language":"en"}

        headers = {
            'x-rapidapi-host': "streaming-availability.p.rapidapi.com",
            'x-rapidapi-key': "c1203a8339msh19d36a59302ebbbp1fcf1djsn5875b40ef7b7"
        }

        response = requests.request("GET", urls, headers=headers, params=querystring)
        genre_sorted_data = response.json()
        print(response.status_code)
        # single_shows_seasons: int = genre_sorted_data["results"][0]["seasons"]
        #print(single_shows_seasons)
        
        def season_sorter(data_dict: Response) -> list:
            """Sort through genre and streaming service data to further filter by seasons."""
            count: int = 0
            sorted_list = []
            for movie in genre_sorted_data["results"]:
                if (count < len(genre_sorted_data["results"])):
                    if ((genre_sorted_data["results"][count]["seasons"] >= show_num_min) and (genre_sorted_data["results"][count]["seasons"] <= show_num_max)):
                        sorted_list.append(movie)
                    count += 1
            
            return sorted_list

        # print(f"Sorted list: {season_sorter(genre_sorted_data)}")
        
        
        # Send final list over to result.html
        return render_template("result.html", data = season_sorter(genre_sorted_data))

    # if request method != post, render original page
    return render_template('index.html')


# flask idiom
if __name__ == '__main__':
    app.run(debug=True)