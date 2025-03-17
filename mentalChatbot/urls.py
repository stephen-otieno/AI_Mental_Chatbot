from . import views
from django.urls import path

urlpatterns = [

    path('', views.home, name='homepage'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup, name='signup'),
    path('relationships/', views.relationships, name='relationships'),
    path('drugs/', views.drugs, name='drugs'),

    path('mental/', views.mental_illness, name='mental_illness'),

    path('disability/', views.disability, name='disability'),
    path('clients/', views.view_clients, name='clients'),

    path('forum/', views.forum_view, name='forum'),
    path('contact/', views.contact, name='contact'),

]

