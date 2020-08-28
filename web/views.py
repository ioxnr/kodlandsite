from datetime import datetime

from django.forms import model_to_dict
from django.shortcuts import render, redirect

from web.models import Post


def index(request):
    limit = 10

    return render(request, 'index.html', {
        'posts': Post.objects.all()[1:limit],
        'new_post': Post.objects.all().order_by('-id')[:1][0]
    })


def write_post(request):
    if request.method == 'GET':
        return render(request, 'write.html')
    else:
        name = request.POST['name']
        text = request.POST['text']
        image = request.FILES['image']

        if len(name) == 0:
            return render(request, 'write.html', {
                'error': 'Введите название статьи'
            })

        if len(text) == 0:
            return render(request, 'write.html', {
                'error': 'Введите текст статьи'
            })

        Post(name=name, date=datetime.now(), text=text.replace('\n', '<br />'), image=image).save()

        return redirect('/')


def read_post(request, number):
    publications = Post.objects.filter(id=number)

    if len(publications) == 1:
        publication = model_to_dict(publications[0])
        return render(request, 'post.html', publication)
    else:
        return redirect('/')
