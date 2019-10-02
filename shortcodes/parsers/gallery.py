#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template import Template, Context
from django.template.loader import render_to_string
from django.conf import settings
from mezzanine.galleries.models import Gallery
from mezzanine.galleries.models import GalleryImage

def parse(kwargs):
    print kwargs
    gallery_id = kwargs.get('id')

    gallery = Gallery.objects.get(id=gallery_id)

    if gallery:
        images = GalleryImage.objects.all().filter(gallery_id=gallery.id)

        templatename = "shortcodes/gallery.html"
        context = Context({
            'sliderimages': images,
            'MEDIA_URL':settings.MEDIA_URL
        })
        return render_to_string(templatename,context)
    else:
        return ''