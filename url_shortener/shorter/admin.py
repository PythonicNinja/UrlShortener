from django.contrib import admin


from .models import UrlSlug, Url

admin.site.register([
    Url,
    UrlSlug
])
