import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

DATABASES_NAME = os.getenv("DATABASES_NAME")
DATABASES_USER = os.getenv("DATABASES_USER")
DATABASES_PASSWORD = os.getenv("DATABASES_PASSWORD")

CACHE_LOCATION = os.getenv("CACHE_LOCATION")
