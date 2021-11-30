from api.models import TinyUrl
from tiny_url.environment import URL, MIN_LEN_TINY_URL, MAX_LEN_TINY_URL
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


# Count the number of requests for a tiny URL
def increase_count_tiny_url(tiny_id):
    tiny = TinyUrl.objects.get(id=tiny_id)
    tiny.counter = tiny.counter + 1
    tiny.save()
    return tiny.url


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
