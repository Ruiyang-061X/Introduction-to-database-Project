from django.shortcuts import render

from .models import Film, Comment


# Create your views here.
def index(request):

    return film_list(request, 1)

def film_list(request, film_list_id):
    film_list = Film.objects.all()[(film_list_id - 1) * 10 : film_list_id * 10]
    context = {
        'film_list_id' : film_list_id,
        'film_list' : film_list,
        'id_list' : [[1, 1, 10], [2, 11, 20], [3, 21, 30], [4, 31, 40], [5, 41, 50], [6, 51, 60], [7, 61, 70], [8, 71, 80], [9, 81, 90], [10, 91, 100]],
        }
    
    return render(request, 'short_film_comment_app/film_list.html', context)

def film(request, film_id):
    film = Film.objects.all()[film_id - 1]
    comment_list = Comment.objects.filter(film_id=film_id)
    context = {
        'film_id' : film_id,
        'film' : film,
        'comment_list' : comment_list,
        }

    return render(request, 'short_film_comment_app/film.html', context)

def comment(request, film_id):
    a = request.POST['comment']
    b = Comment(id=len(Comment.objects.all()) + 1, film_id=film_id, content=a)
    b.save()

    return film(request, film_id)