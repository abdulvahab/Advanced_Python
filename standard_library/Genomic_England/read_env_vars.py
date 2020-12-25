# import os
# from dotenv import load_dotenv
# load_dotenv()
# API_USERNAME = os.getenv('DEBUG')
# print(API_USERNAME)
from decouple import config
config('USER')
config("PASSWORD")