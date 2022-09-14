import cohere
try:
  response = co.generate(
      model='invalid-model',
      prompt='sample prompt')
except cohere.CohereError as e:
    print(e.message)
    print(e.http_status)
    print(e.headers)