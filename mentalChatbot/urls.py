from . import views
from django.urls import path

urlpatterns = [

    path('', views.home, name='homepage'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup, name='signup'),

]
