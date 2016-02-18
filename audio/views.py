from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse, reverse_lazy

from audio.forms import AudioForm
from audio.models import Audio, Artist
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from audio.models import genres


def login(request):
    if request.user.is_authenticated():
        return redirect(reverse("audio:index"))
    if request.method == "GET":
        context = {}
        if "next" in request.GET:
            context["next"] = request.GET["next"]
        return render(request, 'audio/login.html', {"next": context})
    elif request.method == "POST":
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            auth_login(request, user)
            if "next" in request.GET:
                return redirect(request.GET["next"])
            else:
                return redirect(reverse("audio:index"))
        else:
            return redirect(reverse("login"))
    else:
        return HttpResponse("405")


def logout(request):
    auth_logout(request)
    return redirect(reverse("login"))


@login_required(login_url=reverse_lazy("login"))
def index(request):
    audios = request.user.favorites.all()
    return render(request, 'audio/index.html', {"username": request.user.username, "audios": audios})


@login_required(login_url=reverse_lazy("login"))
def show_all(request):
    if request.user.is_authenticated():
        s = "All tracks!<br/><a href=\"%s\">Back to Index</a><br><br>" % reverse('audio:index')
        audios = Audio.objects.all()
        s += "".join(map(lambda x: "<li>%s</li>" % x, audios))
        return HttpResponse(s)
    else:
        return redirect(reverse("login"))


@login_required(login_url=reverse_lazy("login"))
def audio_page(request, audio_id):
    audio_object = Audio.objects.get(id=audio_id)
    who_favorited = audio_object.favorite.all()
    return render(request, "audio/audio_page.html", {"audio": audio_object,
                                                     "liked": who_favorited})


@login_required(login_url=reverse_lazy("login"))
def add_audio_old(request):
    if request.method == "GET":
        return render(request, "audio/add_audio_old.html", {
            "artists": Artist.objects.values("id", "name"),
            "genres": genres
        })
    elif request.method == "POST":
        a = Audio()
        a.title = request.POST["title"]
        a.artist_id = request.POST["artist"]
        a.genre = request.POST["genre"]
        a.save()
        return redirect(reverse("audio:audio_page", args=(a.id,)))
    else:
        return HttpResponse("405")


@login_required(login_url=reverse_lazy("login"))
def add_audio(request):
    if request.method == "GET":
        f = AudioForm()
        return render(request, "audio/add_audio.html", {"f": f})
        pass
    elif request.method == "POST":
        f = AudioForm(request.POST)
        if f.is_valid():
            a = f.save()
            return redirect(reverse("audio:audio_page", args=(a.id,)))
    else:
        return HttpResponse("405")


    # audios = Audio.objects.all()
    # audios = Audio.objects.order_by("anon_likes")
    # audios = Audio.objects.filter(artist="AC/DC")
    # audios = Audio.objects.filter(anon_likes__gte=6000).filter(artist="AC/DC")
    # audios = Audio.objects.filter(title__contains="s")

    # audios = Audio.objects.filter(artist__name="AC/DC").order_by('title')

    # artist = Artist.objects.get(name="AC/DC")
    # audios = artist.audio_set.all()

    # audio = Duet.objects.get(title="Coo song")
    # artist = Artist.objects.get(name="Red Hot Chilly Pappers")
    #
    # audios = artist.audios_from_duet.all()
    #
    # # s += "".join(map(lambda x: "<li>%s</li>" % x, [audio.title for audio in audios]))

