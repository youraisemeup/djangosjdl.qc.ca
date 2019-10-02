from django.template import Library, Node, Variable, VariableDoesNotExist, TemplateSyntaxError
from django.db import models
from itertools import chain
from operator import attrgetter
import datetime, re
from sjdl.documentation.models import BulletinsMunicipaux

register = Library()

class GetLoisirs(Node):
    def __init__(self, slug, contextname):
        self.contextname = contextname
        self.requestedpage = Variable(slug)

    def render(self,context):
        if re.search('loisirs-et-culture',self.requestedpage.resolve(context)):
            try:
                cahierloisirs = BulletinsMunicipaux.objects.all().filter(
                    publish_date__lt = datetime.datetime.now()
                ).filter(
                    titleloisirs__isnull = False
                ).filter(
                    docloisirs__isnull = False
                ).exclude(
                    titleloisirs__exact=''
                ).exclude(
                    docloisirs__exact=''
                ).order_by('-publish_date')[:1]

                context[self.contextname] = {'cahierloisirs':cahierloisirs[0]}
                return ''
            except VariableDoesNotExist:
                return ''
        else:
            return ''

def get_loisirs_doc(parser, token):
    bits = token.contents.split()
    if len(bits) !=3:
        raise TemplateSyntaxError, "get_loisirs_doc takes two arguments"
    return GetLoisirs(bits[1],bits[2])

get_loisirs_doc = register.tag(get_loisirs_doc)