from __future__ import unicode_literals
from django.db import models
import datetime
from mezzanine.core.fields import FileField
from mezzanine.core.models import RichTextField, Displayable

class Careers(Displayable):
    s_text = RichTextField(verbose_name='Texte')

    def __str__(self):
        return self.title

    @staticmethod
    def current_careers_list():
        return Careers.objects.filter(
            publish_date__lte = datetime.datetime.now()
        ).filter(
            models.Q(expiry_date__gte = datetime.datetime.now()) | models.Q(expiry_date__isnull = True)
        ).order_by('-publish_date')

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('careers:detail', kwargs={'slug':self.slug})


    search_fields = ['title']
    ordering=['-publish_date']

    class Meta:
        verbose_name = 'Emploi'
        verbose_name_plural = 'Emplois'



