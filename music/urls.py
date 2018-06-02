from django.conf.urls import url
from . import views


urlpatterns=[
    #/music
    url(r'^$',views.index,name='index'),

    #/music/5
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),

    #/music/<album_id>/fav
    url(r'^(?P<album_id>[0-9]+)/favorite/$',views.detail,name='favorite')
]

