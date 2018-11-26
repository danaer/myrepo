from django.urls import re_path, include
from . import views

urlpatterns = [
    re_path('all/', views.show),
    re_path('showOne/(?P<video_id>\d+)/$', views.ShowOneVideo),
    re_path('addcomment/(?P<video_id>\d+)/$', views.addcomment),
    re_path('sign/',views.sign),
    re_path('login/',views.login),
    re_path('logout/',views.logout),
    re_path('videolike/(?P<video_id>\d+)/$',views.videolike),
    re_path('commentlike/(?P<comment_id>\d+)/$',views.commentlike),
    re_path('videolike/ajax/',views.ajax),
    #re_path('commentlike/ajaxcom/',views.ajaxcom),
    re_path('bio/',views.bio),
    re_path('',views.mainpage)
]