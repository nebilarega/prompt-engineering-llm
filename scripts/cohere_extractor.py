import cohere
import pandas as pd
from dotenv import dotenv_values
import datetime
import requests
config = dotenv_values(".env")  
co = cohere.Client(config['API_KEY'])

class CohereExtractor():
    def __init__(self, examples, example_labels, labels, task_desciption, example_prompt):
        self.examples = examples
        self.example_labels = example_labels
        self.labels = labels
        self.task_desciption = task_desciption
        self.example_prompt = example_prompt

    def make_prompt(self, example):
        examples = self.examples + [example]
        labels = self.example_labels + [""]
        return (self.task_desciption +
                "\n---\n".join( [examples[i] + "\n" +
                                self.example_prompt + " "+
                                 labels[i] for i in range(len(examples))]))

    def extract(self, example):
      extraction = co.generate(
          model='large',
          prompt=self.make_prompt(example),
          max_tokens=10,
          temperature=0.1,
          stop_sequences=["\n"])
      return(extraction.generations[0].text[:-1])
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

print(pd.DataFrame(data={'text': movies_list, 'extracted_text': results}))
