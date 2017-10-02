from . import views
from django.conf.urls import url
from django.conf import settings
urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'(?P<album_id>[0-9]+)/updatealbum',views.updatealbum,name='updatealbum'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login_user/$',views.login_user,name='login_user'),
    url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='details'),
    url(r'^addalbum$',views.addalbum,name='addalbum'),
    url(r'(?P<album_id>[0-9]+)/album/addsong',views.addsong,name='addsong'),
    url(r'(?P<album_id>[0-9]+)/delete/$', views.deletealbum,name='deletealbum'),
    url(r'(?P<album_id>[0-9]+)/song/(?P<song_id>[0-9]+)/delete',views.deletesong,name='deletesong'),
    url(r'^allsongs$',views.allsongs,name='allsongs'),
    url(r'^profile$',views.profile,name='profile'),
    url(r'^logout$',views.logoutuser,name='logoutuser'),
    url(r'^glanceall$',views.glanceall,name='glanceall'),
    url(r'^fetchxml_foralbums$',views.getxml_foralbums,name='getxml_foralbums'),
    url(r'(?P<album_id>[0-9]+)/fetchxml_forsongs',views.getxml_forsongs,name="getxml_forsongs"),
    url(r'^fetchxml_forallsongs$',views.getxml_forallsongs,name="getxml_forallsongs"),
    url(r'^getjson$',views.getjson,name="getjson"),
    url(r'^testangular$',views.test_angular,name="test_angular"),

]