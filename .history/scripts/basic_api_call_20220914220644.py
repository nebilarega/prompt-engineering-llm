import cohere
from dotenv import dotenv_values

config = dotenv_values(".env")  
co = cohere.Client(config['API_KEY'])
try:
    response = co.generate(
      prompt='Once upon a time in a magical land called')
    print('Prediction: {}'.format(response.generations[0].text))
except cohere.CohereError as e:
    print(e.message)
    print(e.http_status)
    print(e.headers)
