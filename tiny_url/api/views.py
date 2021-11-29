from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from django.shortcuts import redirect
from api.service import add_url, get_random_alphanumeric_string, increase_count_tiny_url
import json


@csrf_exempt
@require_POST
def create(request):
    if request.method == 'POST':
        url_unicode = request.body.decode('utf-8')
        body = json.loads(url_unicode)
        url = body.get("url")
        if url is None:
            return HttpResponseBadRequest("Missing mandatory field 'url'")
        tinyurl = add_url(url)
        return HttpResponse(tinyurl)


@require_GET
def redirect_short(request, tiny_id):
    try:
        url = increase_count_tiny_url(tiny_id)
        return redirect(url)
    except Exception:
        return HttpResponseNotFound("Could not find redirect")


