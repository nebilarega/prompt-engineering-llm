import cohere
from dotenv import load_dotenv
load_dotenv()
co = cohere.Client(API_KEY)
try:
  response = co.generate(
      model='invalid-model',
      prompt='sample prompt')
except cohere.CohereError as e:
    print(e.message)
    print(e.http_status)
    print(e.headers)