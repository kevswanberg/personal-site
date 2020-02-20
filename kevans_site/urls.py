from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from experience.views import ExperienceModelViewSet

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.sitemaps.views import sitemap


api_router = DefaultRouter()
api_router.register(r'work-experience', ExperienceModelViewSet)


urlpatterns = [
    re_path('^sitemap\.xml', sitemap),
    path('admin/', admin.site.urls),
    path('api/', include(api_router.urls)),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'', include(wagtail_urls))
]

if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
