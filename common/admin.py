from copy import deepcopy
from django.contrib import admin
from mezzanine.galleries.admin import GalleryImageInline, GalleryAdmin
from mezzanine.galleries.models import Gallery, GalleryImage
from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.generic.models import ThreadedComment

admin.site.unregister(Gallery)

class NewGalleryImageInline(GalleryImageInline):
    fields = ('file','title','description','credits')

class NewGalleryAdmin(GalleryAdmin):
    inlines = (NewGalleryImageInline,)


admin.site.register(Gallery, NewGalleryAdmin)
admin.site.unregister(BlogPost)
admin.site.unregister(BlogCategory)
admin.site.unregister(ThreadedComment)