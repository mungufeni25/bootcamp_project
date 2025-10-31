from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog/', views.blog, name='blog'),
    path('show_all/', views.show_all, name='show_all'),
    path('about/', views.about, name='about'),
]