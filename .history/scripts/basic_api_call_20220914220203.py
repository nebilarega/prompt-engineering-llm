import cohere
from dotenv import dotenv_values

config = dotenv_values(".env")  
print(config[0])
# co = cohere.Client(config.API_KEY)
# try:
#   response = co.generate(
#       model='invalid-model',
#       prompt='sample prompt')
# except cohere.CohereError as e:
#     print(e.message)
#     print(e.http_status)
#     print(e.headers)