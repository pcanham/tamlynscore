from django.conf import settings
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'', include('core.urls')),
    (r'^tournaments/', include('entries.urls')),
    (r'^tournaments/scoring/', include('scores.urls')),
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import urlpatterns as static_patterns
    urlpatterns += static_patterns

