#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText,Orderable
from mezzanine.core.fields import FileField

class DocumentPage(Page, RichText):
    class Meta:
        verbose_name='Page de texte riche'
        verbose_name_plural='Pages de texte riche'

class DocumentPageDocument(Orderable):
    document = models.ForeignKey("DocumentPage",related_name="documents")
    file = FileField("Document", max_length=200, format="Document", upload_to="documents", extensions=[".pdf"])
    title = models.CharField("Titre",max_length=200,default="")

    class Meta:
        verbose_name='Document'
        verbose_name_plural='Documents'

        def __unicode__(self):
            return self.title
