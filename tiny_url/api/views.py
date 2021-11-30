from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import redirect
from api.service import add_url, get_random_alphanumeric_string, \
    add_tiny_url_to_request_collection, is_valid_url, count_url_usage
import json


# Create a tiny URL for an original URL if the URL in the body of the request is valid
@csrf_exempt
@require_POST
def create(request):
    url_unicode = request.body.decode('utf-8')
    body = json.loads(url_unicode)
    url = body.get("url")

    if url is None:
        return HttpResponseBadRequest("Missing mandatory field 'url'")

    if not is_valid_url(url):
        return HttpResponseBadRequest("Invalid 'url'")

    tinyurl = add_url(url)
    return HttpResponse(tinyurl)


# Redirect to original URL if the tiny URL is valid
@require_GET
def redirect_short(request, tiny_id):
    try:
        url = add_tiny_url_to_request_collection(tiny_id)
        return redirect(url)
    except Exception:
        return HttpResponseNotFound("Could not find redirect")


# get count of usage in tiny_url
@require_GET
def num_clicks_tiny_url(request, tiny_id):
    count_tiny_url_clicks = count_url_usage(tiny_id)
    return HttpResponse(count_tiny_url_clicks)
