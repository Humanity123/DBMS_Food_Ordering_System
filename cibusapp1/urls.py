from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^cregister/$', views.cregister, name='cregister'),
    url(r'^rregister/$', views.rregister, name='rregister'),
    url(r'^clogin/$', views.clogin, name='clogin'),
    url(r'^rlogin/$', views.rlogin, name='rlogin'),
    url(r'^restaurant/$', views.restaurant, name='restaurant'),
    url(r'^restaurant/edit/', views.redit, name='redit'),
    url(r'^customer/$', views.customer, name='customer'),
    url(r'^restaurant/add$', views.add_dish, name='add_dish'),
    url(r'^customer/catselect$', views.catselect, name='catselect'),
    url(r'^customer/restdish/(?P<username>\w{0,200})/(?P<category>\w{0,2})$', views.restdish, name='restdish'),
    url(r'^customer/restdish/(?P<username>\w{0,200})$', views.restalldish, name='restalldish'),
    url(r'^customer/restdish/(?P<username>\w{0,200})/(?P<name>\w{0,200})$', views.restalldishselect, name='restalldishselect'),
    url(r'^customer/reslist/', views.reslist, name='reslist'),
    
    url(r'^customer/restdish/(?P<username>\w{0,200})/(?P<category>\w{0,2})/(?P<name>\w{0,200})$', views.restdishselect, name='restdishselect'),
    url(r'^restaurant/rorders$', views.rorders, name='rorders'),
    url(r'^restaurant/rorders/(?P<orderid>\d+)$', views.rorders_info, name='rorders_info'),
    url(r'^customer/myorder$', views.myorder, name='myorders'),
    url(r'^customer/myorder/(?P<orderid>\d+)$', views.orderinfo, name='orderinfo'),
    url(r'^customer/edit/', views.cedit, name='cedit'),
    url(r'^customer/cart/inc/(?P<dishname>\w{1,200})', views.cartinc, name='inc'),
    url(r'^customer/cart/dec/(?P<dishname>\w{1,200})', views.cartdec, name='dec'),
    url(r'^customer/cart/', views.cart, name='cart'),
    url(r'^customer/searchres/(?P<c>\w{1,2})', views.searchres, name='searchres'),
    url(r'^restaurant/restmenu$', views.restmenu, name='restmenu'),
    # url(r'^customer/catselect/searchres$', views.searchres, name='searchres'),

]
