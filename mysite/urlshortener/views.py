from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import URLs

# Create your views here.

def index(request, id=1):
    url_object = None
    shrinked_url = None
    if request.method == 'POST':
        engine_url = request.POST['engine'] # url that was written
        try:
            url_object = URLs.objects.get(pk=engine_url)
        except URLs.DoesNotExist:
            new_url = URLs.objects.create_url(engine=engine_url)
            new_url.save()
            url_object = new_url

    if url_object is not None:
        shrinked_url = 'http://127.0.0.1:8000/' + url_object.shortcut

    context = {
        'url_object': url_object,
        'shrinked_url': shrinked_url,
    }

    return render(request, 'urlshortener/base.html', context)


def redirection(request, shortcut=None):
    try:
        url = URLs.objects.filter(shortcut=shortcut)[0]
    except URLs.DoesNotExist :
         return HttpResponse('There is no such url')
    except IndexError:
        return HttpResponse('There is no such url')

    return redirect(url.engine)
