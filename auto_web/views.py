from django.shortcuts import render, HttpResponse,redirect
from .scrapedata import mainpage
from .lyrics_getter import lyrics
from .models import *
import datetime
from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required



# Create your views here.
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('adminpanel')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('adminpanel')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'auto_web/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect('loginPage')
def index(request):
    obj=Lyrics.objects.get_queryset().order_by('-id')
    ob=Lyrics.objects.values('time_stamp')
    print(len(ob))
    p = Paginator(obj, 28)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    # print(page_obj)
    context = {'page_obj': page_obj}


    # context={}
    return render(request,"auto_web/index.html",context)

def lyrics_page(request,pk):
    obj=Lyrics.objects.get(id=pk)
    context={"lyrics":obj}
    # print(obj)
    return render(request,"auto_web/post.html",context)

@login_required(login_url='loginPage')
def adminpanel(request):
    if request.method == 'POST':
        song_lst=mainpage()
        print(song_lst)
        for i in song_lst:
            lyric_str=""
            get_lyrics=lyrics(i)
            # print(get_lyrics)

            singer_name=get_lyrics[1]
            song_name=get_lyrics[2]

            for i in get_lyrics[0]:
                lyric_str=lyric_str+i
            print(singer_name)
            print(song_name)
            print(lyric_str)
            date_time=datetime.date.today()
            obj=Lyrics.objects.create(song_name=song_name,song_artist=singer_name,song_lyrics=lyric_str,time_stamp=date_time)
            obj.save()
    return render(request,"auto_web/admin.html")
def contact(request):
    return render(request,"auto_web/contact.html")
