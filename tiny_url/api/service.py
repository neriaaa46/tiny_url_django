from api.models import TinyUrl
from tiny_url.environment import URL, MIN_LEN_TINY_URL, MAX_LEN_TINY_URL
import random
import string


def add_url(url):
    length_of_tiny_url = random.randint(MIN_LEN_TINY_URL, MAX_LEN_TINY_URL)
    id_tiny_url = get_random_alphanumeric_string(length_of_tiny_url)

    while TinyUrl.objects.filter(id=id_tiny_url):
        length_of_tiny_url = random.randint(MIN_LEN_TINY_URL, MAX_LEN_TINY_URL)
        id_tiny_url = get_random_alphanumeric_string(length_of_tiny_url)

    TinyUrl.objects.create(id=id_tiny_url, url=url)
    return URL + id_tiny_url


def get_random_alphanumeric_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(letters_and_digits) for i in range(length)))
    return result_str


def increase_count_tiny_url(tiny_id):
    tiny = TinyUrl.objects.get(id=tiny_id)
    tiny.counter = tiny.counter + 1
    tiny.save()
    return tiny.url
