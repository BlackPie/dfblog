from django.conf import settings
from django.contrib import admin
from django.views.static import serve
from django.conf.urls import include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from project.apps.blog.views import BlogView, EntryView, AboutView


urlpatterns = [
    url(r'^static/(?P<path>.*)$', serve),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),

    # main urls
    url(r'^$', BlogView.as_view(), name='index'),
    url(r'^blog/$', BlogView.as_view(), name='blog'),
    url(r'^post/(?P<slug>[\w-]+)/$', EntryView.as_view(), name='entry'),
    url(r'^about/$', AboutView.as_view(), name='about'),

    url(r'^admin/', include(admin.site.urls)),
]

# urlpatterns.append(staticfiles_urlpatterns())
# urlpatterns.append(('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})))
