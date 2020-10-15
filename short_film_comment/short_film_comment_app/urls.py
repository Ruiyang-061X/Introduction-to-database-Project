from django.urls import path

from . import views

app_name = 'short_film_comment_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('film_list/<int:film_list_id>/', views.film_list, name='film_list'),
    path('film/<int:film_id>/', views.film, name='film'),
    path('comment/<int:film_id>/', views.comment, name='comment'),
]