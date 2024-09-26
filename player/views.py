from django.shortcuts import render, redirect
from .models import Song, Playlist
from django.http import StreamingHttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
# Create your views here

def home(request):
    '''Home page views'''
    data = Song.objects.all()
    salman = Song.objects.filter(category="Hit of Salman")
    old = Song.objects.filter(category="Old is Gold")
    latest_hit = Song.objects.filter(category="Latest Hit")
    old_data = []
    j = 1
    for i in old:
        old_data.append(i)
        j = j + 1
        if j == 4:
            break

    latest_hit_data= []
    k = 1
    for m in latest_hit:
        latest_hit_data.append(m)
        k = k + 1
        if k == 4:
            break
    return render(request,'index.html',{'data':data,'salman':salman,'old':old_data,'latest_hit':latest_hit_data})

def stream_audio(request, id):
    '''Dowloading the mp3 file'''
    song = Song.objects.get(id=id)
    response = StreamingHttpResponse(open(song.song.path, 'rb'))
    response['Content-Type'] = 'audio/mp3'
    response['Content-Disposition'] = f'attachment; filename="{song.song_name}.mp3"'
    return response

def play(request,id):
    '''Playing the perticular song'''
    song = Song.objects.get(id=id)
    category = Song.objects.filter(category=song.category)

    current_song_id = song.id

    '''Logic of Next song'''
    all_song = []
    for i in category:
        all_song.append(i.id)
    next_song = all_song[1]

    if id >= next_song:
        next_song = all_song[2]
    else:
        next_song = all_song[1]

    '''logic of previous song'''
    index_song = all_song.index(current_song_id)

    previous_song_index = index_song - 1
    previous_song = all_song[previous_song_index]
    return render(request,'play.html',{'data':song,'next_song':next_song,'previous_song':previous_song})

def next_song(request,id):
    '''Next song playing'''
    song = Song.objects.get(id=id)
    return render(request,'play.html',{'data':song})

def previous_song(request,id):
    '''Playing the previous song'''
    song = Song.objects.get(id=id)
    return render(request,'play.html',{'data':song})

def user_login(request):
    '''User Login view'''
    if request.method == "POST":
        user = request.POST.get('user')
        password = request.POST.get('password')
        users = authenticate(request,username=user,password=password)
        if users is not None:
            login(request,users)
            return redirect('home')
        else:
            msg = "Wrong Username or Password"
            return render(request,'login.html',{'msg':msg})

    else:
        return render(request,'login.html')

def login_page(request):
    '''Login page view'''
    return render(request,'login.html')


def create_user(request):
    '''Creating the user'''
    if request.method == "POST":
        username = request.POST.get('user')
        password = request.POST.get('password')
        email = request.POST.get('email')

        if User.objects.filter(username=username).exists():
            msg = "Username already exist try another username"
            return render(request,'create_user.html',{'msg':msg})

        else:
            User.objects.create_user(username=username,password=password,email=email)
            msg1 = "User is registred Successfully login to the account"
            return render(request,'login.html',{'msg1':msg1})

    else:
        return render(request,'login.html')

def logout_user(request):
    '''Logout User'''
    logout(request)
    return redirect('login_page')


def create_user_page(request):
    '''Creating User page'''
    return render(request,'create_user.html')

def profile(request):
    '''User Profile'''
    return render(request,'profile.html')

def add_playlist(request,id):
    '''Adding the song into playlist'''
    song = Song.objects.get(id=id)
    user = request.user
    Playlist.objects.create(song=song,user=user)
    category = Song.objects.filter(category=song.category)

    current_song_id = song.id

    '''Logic of Next song'''
    all_song = []
    for i in category:
        all_song.append(i.id)
    next_song = all_song[1]

    if id >= next_song:
        next_song = all_song[2]
    else:
        next_song = all_song[1]

    '''logic of previous song'''
    index_song = all_song.index(current_song_id)

    previous_song_index = index_song - 1
    previous_song = all_song[previous_song_index]
    return render(request,'play.html',{'data':song,'next_song':next_song,'previous_song':previous_song})



def song_user(request):
    '''Users all songs list'''
    song = Playlist.objects.filter(user=request.user)
    return render(request,'songs.html',{'data':song})


def add_song_page(request):
    return render(request,'add_song.html')


def add_song(request):
    if request.method == "POST":
        user = request.user
        song_name = request.POST.get('song_name')
        song_data = request.FILES['song_data']
        song_image = request.FILES['song_image']
        category = request.POST.get('category')
        Song.objects.create(song_name=song_name,song=song_data,song_image=song_image,category=category,user=user)
        msg = "Song is added in the jumsic player"
        return render(request,'add_song.html',{'msg':msg})