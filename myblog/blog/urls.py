from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^index/$', views.IndexView.as_view()),
    url(r'^$', views.IndexView.as_view()),
    url(r'^view(?P<post_num>\d+)/$', views.view),
    url(r'^showtags(?P<tag_num>\d+)/$', views.showtags),
    url(r'^showcats(?P<cat_num>\d+)/$', views.showcats),
    url(r'^search_check/$', views.search),
    url(r'^archive/$', views.archive),
]


