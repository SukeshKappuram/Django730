from django.shortcuts import render,get_object_or_404
from .models import Album
from django.template import loader

# Create your views here.
from django.http import HttpResponse
from django.http import Http404

def index(request):
    albums=Album.objects.all()
    #template = loader.get_template('music/index.html')
    context ={
        'albums':albums
    }
    #return HttpResponse(template.render(context,request))
    return render(request, 'music/index.html', context)

def detail(request,album_id):
    #return HttpResponse("<h1>the album "+album_id+"</h1>")

    #try:
     #   album=Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
     #   raise Http404("Album Does not Exist")


    #http shortcut
    album = get_object_or_404(Album,pk=album_id)

    context = {
        'album': album
    }
    return render(request,'music/details.html',context)


