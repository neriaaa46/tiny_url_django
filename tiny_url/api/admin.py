from django.contrib import admin
from api.models import TinyUrl, TinyUrlRequest


admin.site.register(TinyUrl)
admin.site.register(TinyUrlRequest)
