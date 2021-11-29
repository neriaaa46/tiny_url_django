from os import environ

URL = environ.get("URL", "http://localhost:8000/s/")
MIN_LEN_TINY_URL = int(environ.get("MIN_LEN_TINY_URL", 5))
MAX_LEN_TINY_URL = int(environ.get("MAX_LEN_TINY_URL", 10))
