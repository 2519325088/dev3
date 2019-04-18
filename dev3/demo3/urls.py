from django.conf.urls import url

from . import views

app_name='demo3'

urlpatterns=[
    url('^$',views.index,name='index'),
    url('^detail/(\d+)/$',views.detail,name='detail'),
    url('^poll/(\d+)/$',views.poll,name='poll'),

]
