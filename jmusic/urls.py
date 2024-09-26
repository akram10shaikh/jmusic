from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from player import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('stream_audio/<int:id>/',views.stream_audio,name="stream_audio"),
    path('play/<int:id>/',views.play,name="play"),
    path('user_login/',views.user_login,name='user_login'),
    path('login_page/',views.login_page,name='login_page'),
    path('logout_user/',views.logout_user,name='logout_user'),
    path('create_user/',views.create_user,name='create_user'),
    path('create_user_page/',views.create_user_page,name='create_user_page'),
    path('profile/',views.profile,name='profile'),
    path('add_playlist/<int:id>/',views.add_playlist,name='add_playlist'),
    path('song_user/',views.song_user,name="song_user"),
    path('next_song/<int:id>/',views.next_song,name='next_song'),
    path('add_song/',views.add_song,name="add_song"),
    path('add_song_page/',views.add_song_page,name="add_song_page"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
