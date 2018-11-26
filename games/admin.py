from django.contrib import admin
from .models import Video, Comment

class VideoInLine(admin.StackedInline):
    model = Comment
    extra = 2
    #readonly_fields = ['Comment_likes'] #Делает неизменяемым поле

class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoInLine]
    list_filter = ['Video_data']
    #readonly_fields = ['Video_likes']

admin.site.register(Video, VideoAdmin)
