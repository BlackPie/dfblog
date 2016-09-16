from django.conf import settings
from django.contrib import admin
from django.conf.urls import include, url, patterns
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from project.apps.blog.views import BlogView, EntryView
from project.apps.users import views as users_views


urlpatterns = [
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve'),

    # main urls
    url(r'^$', BlogView.as_view(), name='blog'),
    url(r'^post/(?P<slug>[\w-]+)/$', EntryView.as_view(), name='entry'),

    # users urls
    url(r'^signin/$', users_views.SigninView.as_view(), name='signin'),
    url(r'^signup/$', users_views.SignupView.as_view(), name='signup'),
    url(r'^exit/$', users_views.LogoutView.as_view(), name='logout'),

    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('', (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
