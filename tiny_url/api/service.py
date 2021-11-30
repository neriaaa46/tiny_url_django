from api.models import TinyUrl, TinyUrlRequest
from tiny_url.environment import URL, MIN_LEN_TINY_URL, MAX_LEN_TINY_URL
from django.apps import apps
import random
import string
import re


# Add a original URL and tiny url that generated to the DB, return tiny URL
def add_url(url):
    length_of_tiny_url = random.randint(MIN_LEN_TINY_URL, MAX_LEN_TINY_URL)
    id_tiny_url = get_random_alphanumeric_string(length_of_tiny_url)

    while TinyUrl.objects.filter(id=id_tiny_url):
        length_of_tiny_url = random.randint(MIN_LEN_TINY_URL, MAX_LEN_TINY_URL)
        id_tiny_url = get_random_alphanumeric_string(length_of_tiny_url)

    TinyUrl.objects.create(id=id_tiny_url, url=url)
    return URL + id_tiny_url


# generate tiny URL id - length 5-10 - alphanumeric_string
def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


# add TinyUrl to db for counting and return the original url to redirect
def add_tiny_url_to_request_collection(tiny_id):
    tiny = TinyUrl.objects.get(id=tiny_id)
    TinyUrlRequest.objects.create(tiny_url=tiny)
    return tiny.url


def count_url_usage(tiny_id):
    count_tiny_url_clicks = TinyUrlRequest.objects.filter(tiny_url_id=tiny_id).count()
    return count_tiny_url_clicks


# check valid url
def is_valid_url(str_url):
    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if str_url == None:
        return False

    # Return if the string
    # matched the ReGex
    if re.search(p, str_url):
        return True
    else:
        return False
