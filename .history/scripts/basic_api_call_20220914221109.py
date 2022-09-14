from cmd import PROMPT
import cohere
from dotenv import dotenv_values

config = dotenv_values(".env")  
co = cohere.Client(config['API_KEY'])
PROMPT = input("Prompt: ")
PROMPT = str(PROMPT)
try:
    response = co.generate(
      prompt=PROMPT)
    prediction = response.generations[0].text
    print('Prediction: {}'.format(prediction))
    print('Full output: {} {}'.format(PROMPT, prediction))
except cohere.CohereError as e:
    print(e.message)
    print(e.http_status)
    print(e.headers)
