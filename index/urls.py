from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.home, name='home'),
    path('collaborate/', views.collaborate, name='collaborate'),
    path('communities/', views.communities, name='communities'),
    path('connect/', views.connect, name='connect'),
    path('blog/', views.blog, name='blog'),
]