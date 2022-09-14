import cohere
# from dotenv import load_dotenv
API_KEY = 'qpR9uc7ddIfLo3SFEjON0RK5Ypz4jtmLbdEjFV1E'
co = cohere.Client('{API_KEY}')
try:
  response = co.generate(
      model='invalid-model',
      prompt='sample prompt')
except cohere.CohereError as e:
    print(e.message)
    print(e.http_status)
    print(e.headers)