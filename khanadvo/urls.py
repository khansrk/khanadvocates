from django.conf.urls import url
from django.contrib import admin

from advocates import views, auth

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name = 'index'),
    url(r'^login/', auth.login, name = 'login'),
    url(r'^logout/', auth.logout, name = 'logout'),
    url(r'^register/', auth.register, name = 'register'),

    url(r'^sessions/$', views.SessionList.as_view(), name = 'sessions_list'),
    url(r'^sessions/(?P<pk>[0-9]+)/$', views.SessionDetail.as_view(), name = 'sessions_detail'),
    url(r'^sessions/create/$', views.SessionCreate.as_view(), name = 'sessions_create'),
    url(r'^sessions/update/(?P<pk>[0-9]+)/$', views.SessionUpdate.as_view(), name = 'sessions_update'),

]

