from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^cregister/$', views.cregister, name='cregister'),
    url(r'^rregister/$', views.rregister, name='rregister'),
    url(r'^clogin/$', views.clogin, name='clogin'),
    url(r'^rlogin/$', views.rlogin, name='rlogin'),
    url(r'^restaurant/$', views.restaurant, name='restaurant'),
    url(r'^customer/$', views.customer, name='customer'),
    url(r'^restaurant/add$', views.add_dish, name='add_dish'),
    url(r'^customer/catselect$', views.catselect, name='catselect'),
]
