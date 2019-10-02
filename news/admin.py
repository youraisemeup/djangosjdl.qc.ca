from django.contrib import admin
from sjdl.news.models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','status','publish_date','b_home')
    ordering=['-publish_date']

admin.site.register(News,NewsAdmin)