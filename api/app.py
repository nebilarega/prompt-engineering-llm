from flask import Flask, jsonify, request
from scripts.cohere_extractor import CohereExtractor
import datetime
import requests
import pandas as pd

app = Flask(__name__)

incomes = [
    { 'description': 'salary', 'amount': 5000 }
]


@app.route('/')
def get_incomes():
    return jsonify(incomes)


@app.route('/jdentities', methods=['POST'])
def call_cohere_api():
    movie_examples = [
    ("Deadpool 2", "Deadpool 2 | Official HD Deadpool's \"Wet on Wet\" Teaser | 2018"),
    ("none", "Jordan Peele Just Became the First Black Writer-Director With a $100M Movie Debut"),
    ("Joker", "Joker Officially Rated “R”"),
    ("Free Guy", "Ryan Reynolds’ 'Free Guy' Receives July 3, 2020 Release Date - About a bank teller stuck in his routine that discovers he’s an NPC character in brutal open world game."),
    ("none", "James Cameron congratulates Kevin Feige and Marvel!"),
    ("Guardians of the Galaxy", "The Cast of Guardians of the Galaxy release statement on James Gunn"),
    ]
    def get_post_titles(**kwargs):
        """ Gets data from the pushshift api. Read more: https://github.com/pushshift/api """
        base_url = f"https://api.pushshift.io/reddit/search/submission/"
        payload = kwargs
        request = requests.get(base_url, params=payload)
        return [a['title'] for a in request.json()['data']]

    cohereMovieExtractor = CohereExtractor([e[1] for e in movie_examples], 
                                        [e[0] for e in movie_examples], [],
                                        "", 
                                        "extract the movie title from the post:")

    # Uncomment to inspect the full prompt:
    results = []
    num_posts = 10
    try:
        movies_list = get_post_titles(size=num_posts, 
        after=str(int(datetime.datetime(2021,1,1,0,0).timestamp())), 
        before=str(int(datetime.datetime(2022,1,1,0,0).timestamp())), 
        subreddit="movies", 
        sort_type="score", 
        sort="desc")
    except:
        print("Cannot pull the data right now")
    else:
        for text in movies_list:
            try:
                extracted_text = cohereMovieExtractor.extract(text)
                results.append(extracted_text)
            except Exception as e:
                print('ERROR: ', e)

    return pd.DataFrame(data={'text': movies_list, 'extracted_text': results})
