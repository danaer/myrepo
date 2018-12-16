from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Video, Comment
from django.contrib.auth import get_user_model
from . import form
from django.template.context_processors import csrf
from django.contrib import auth

from bs4 import BeautifulSoup
from sqlite3 import connect
import requests

User = get_user_model()

def show(request):
    content = []
    for vid in Video.objects.all():
        tmp = []
        tmp.append(vid)
        comments = Comment.objects.filter(Comment_Video_id=vid.id)
        list_users = []
        for com in comments:
            list_users.append(User.objects.get(id=com.Comment_User_id))
        tmp.append(list(zip(comments,list_users)))
        content.append(tmp)

    return render(request,"mytemplate.html",{'content':content, 'user':auth.get_user(request).username})

def ShowOneVideo(request, video_id):
    args = {}
    args.update(csrf(request))
    args['form'] = form.CommentForm
    args['user'] = auth.get_user(request).username
    args['video'] = Video.objects.get(id = video_id)
    comments = Comment.objects.filter(Comment_Video_id = video_id)
    list_users = []
    for com in comments:
        list_users.append(User.objects.get(id=com.Comment_User_id))
    args['comments'] = list(zip(comments, list_users))
    return render(request, 'onevideo.html',args)

def addcomment(request, video_id):
    if request.POST:
        forma = form.CommentForm(request.POST)
        if forma.is_valid():
            comment = forma.save(commit=False)
            comment.Comment_Video = Video.objects.get(id=video_id)
            comment.Comment_User = User.objects.get(id=request.user.id)
            forma.save()
    return redirect("/games/showOne/" + str(video_id) + "/")


def sign(request):
    if request.POST:
        forma = form.UserForm(request.POST)
        user = User.objects.create_user(username=request.POST.get('username',""),
                                        email=request.POST.get('email',""),
                                        password=request.POST.get('password',""))
        if user:
            auth.login(request, user)

        return redirect('/games/all')
    else:
        args = {}
        args.update(csrf(request))
        args['form'] = form.UserForm
        args['url'] = '/games/sign/'
        args['user'] = auth.get_user(request).username
        return render(request, 'sign.html', args)


def login(request):
    if request.POST:
        forma = form.UserFormL(request.POST)
        user = auth.authenticate(username=request.POST.get('username',""),
                                 password=request.POST.get('password',""))
        if user:
            auth.login(request, user)
        else:
            args = {}
            args.update(csrf(request))
            args['user'] = auth.get_user(request).username
            args['form'] = form.UserFormL
            args['url'] = '/games/login/'
            args['error'] = "Такой пользователь не найден"
            return render(request, 'sign.html', args)
        return redirect('/')

    else:
        args = {}
        args.update(csrf(request))
        args['user'] = auth.get_user(request).username
        args['form'] = form.UserFormL
        args['url'] = '/games/login/'
        return render(request, 'sign.html', args)

def logout(request):
    auth.logout(request)
    return redirect('/')


def videolike(request, video_id):
    vid = Video.objects.get(id = video_id)
    vid.Video_likes += 1
    vid.save()
    return redirect("/games/showOne/" + str(video_id) + "/")

def commentlike(request, comment_id):
    com = Comment.objects.get(id=comment_id)
    com.Comment_likes += 1
    com.save()
    return redirect("/games/showOne/" + str(com.Comment_Video_id) + "/")

def england(request):
    args = {}
    args.update(csrf(request))
    req = requests.get("https://sports.ru/epl/table")
    soup = BeautifulSoup(req.text)
    stats = [];    teams = [];    stats1 = []
    teams.extend([i.text for i in soup.find_all("", {"class": "name"})])
    data = soup.find("div", {"class": "stat mB6"}).text.replace("\n", " ").split()
    for i in data:
        if i.isnumeric() == True:
            stats1.append(i)
    for i in range(len(stats1)):
        if i % 8 != 0:
            stats.append(stats1[i])
    return render(request, "england.html", {'user': auth.get_user(request).username, 'teams':teams,'stats':stats})

def spain(request):
    args = {}
    args.update(csrf(request))
    req = requests.get("https://sports.ru/la-liga/table")
    soup = BeautifulSoup(req.text)
    stats = [];    teams = [];    stats1 = []
    teams.extend([i.text for i in soup.find_all("", {"class": "name"})])
    data = soup.find("div", {"class": "stat mB6"}).text.replace("\n", " ").split()
    for i in data:
        if i.isnumeric() == True:
            stats1.append(i)
    for i in range(len(stats1)):
        if i % 8 != 0:
            stats.append(stats1[i])
    return render(request, "spain.html", {'user': auth.get_user(request).username, 'teams':teams,'stats':stats})

def france(request):
    args = {}
    args.update(csrf(request))
    req = requests.get("https://sports.ru/ligue-1/table")
    soup = BeautifulSoup(req.text)
    stats = [];    teams = [];    stats1 = []
    teams.extend([i.text for i in soup.find_all("", {"class": "name"})])
    data = soup.find("div", {"class": "stat mB6"}).text.replace("\n", " ").split()
    for i in data:
        if i.isnumeric() == True:
            stats1.append(i)
    for i in range(len(stats1)):
        if i % 8 != 0:
            stats.append(stats1[i])
    return render(request, "france.html", {'user': auth.get_user(request).username, 'teams':teams,'stats':stats})

def germany(request):
    args = {}
    args.update(csrf(request))
    req = requests.get("https://sports.ru/bundesliga/table")
    soup = BeautifulSoup(req.text)
    stats = [];    teams = [];    stats1 = []
    teams.extend([i.text for i in soup.find_all("", {"class": "name"})])
    data = soup.find("div", {"class": "stat mB6"}).text.replace("\n", " ").split()
    for i in data:
        if i.isnumeric() == True:
            stats1.append(i)
    for i in range(len(stats1)):
        if i % 8 != 0:
            stats.append(stats1[i])
    return render(request, "germany.html", {'user': auth.get_user(request).username, 'teams':teams,'stats':stats})

def italy(request):
    args = {}
    args.update(csrf(request))
    req = requests.get("https://sports.ru/seria-a/table")
    soup = BeautifulSoup(req.text)
    stats = [];    teams = [];    stats1 = []
    teams.extend([i.text for i in soup.find_all("", {"class": "name"})])
    data = soup.find("div", {"class": "stat mB6"}).text.replace("\n", " ").split()
    for i in data:
        if i.isnumeric() == True:
            stats1.append(i)
    for i in range(len(stats1)):
        if i % 8 != 0:
            stats.append(stats1[i])
    return render(request, "italy.html", {'user': auth.get_user(request).username, 'teams':teams,'stats':stats})
def bio(request):
    return render(request,"bio.html", {'user':auth.get_user(request).username} )

def mainpage(request):
    return render(request, 'mainpage.html',{'user':auth.get_user(request).username})

def ajaxcom(request):
    if request.GET:
        idcom = request.GET['addlikecom']
        com = Comment.objects.get(id=idcom)
        com.Comment_likes += 1
        com.save()
    return HttpResponse(com.Comment_likes)

def ajax(request):
    if request.GET:
        idvid = request.GET['addlike']
        vid = Video.objects.get(id=idvid)
        vid.Video_likes += 1
        vid.save()
    return HttpResponse(vid.Video_likes)



    #return render(request,'mytemplate.html', {'name':'Richard'})
    #return HttpResponse("Hello")