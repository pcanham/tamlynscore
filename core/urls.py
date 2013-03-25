from django.conf.urls import patterns, url

import views

urlpatterns = patterns('core.views',
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^clubs/$', views.ClubList.as_view(), name='club_list'),
    url(r'^clubs/(?P<slug>[\w-]+)/$', views.ClubDetail.as_view(), name='club_detail'),
    url(r'^clubs/(?P<slug>[\w-]+)/edit/$', views.ClubUpdate.as_view(), name='club_update'),
    url(r'^archer/(?P<pk>\d+)/$', views.ArcherDetail.as_view(), name='archer_detail'),
    url(r'^archer/(?P<pk>\d+)/edit/$', views.ArcherUpdate.as_view(), name='archer_update'),
)
