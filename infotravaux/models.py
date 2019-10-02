from __future__ import unicode_literals
from django.db import models
from mezzanine.galleries.models import Gallery
import datetime
from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Displayable

#@todo: conditional validation

class InfoTravaux(Displayable, RichText):
    ik_image = FileField("Image", max_length=200, upload_to="", blank=True, null=True)
    ik_diapo = models.ForeignKey("galleries.Gallery", verbose_name="Diaporama", blank=True, null=True, default=None)
    s_link = models.CharField(max_length=255, verbose_name='Lien externe', blank=True, null=True)
    s_link_title = models.CharField(max_length=255, verbose_name='Titre du lien', blank=True, null=True)
    s_link_youtube = models.CharField(max_length=255, verbose_name='Lien Youtube', blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('infotravaux:detail', kwargs={'slug':self.slug})

    @staticmethod
    def latest_infos_list():
        return InfoTravaux.objects.filter(
            publish_date__lte = datetime.datetime.now()
        ).filter(
            models.Q(expiry_date__gte = datetime.datetime.now()) | models.Q(expiry_date__isnull = True)
        ).filter(
            status = 2
        ).order_by('-publish_date')


    search_fields = ['title']
    ordering=['-publish_date']

    class Meta:
        verbose_name = 'Info-Travaux'
        verbose_name_plural = 'Info-Travaux'



