from django.template import Library, Node, Variable, VariableDoesNotExist, TemplateSyntaxError
from django.db import models
from itertools import chain
from operator import attrgetter
import datetime
from sjdl.coordonnees.models import Coordonnees

register = Library()

class GetCoordonnees(Node):
    def __init__(self, pageid, contextname):
        self.contextname = contextname
        self.requestedpage = Variable(pageid)

    def render(self,context):
        try:
            actual_ik_page = self.requestedpage.resolve(context)
            coordonnees = Coordonnees.objects.all().filter(pages = actual_ik_page)

            useGeneralAddress = True
            for coords in coordonnees:
                if coords.address:
                    useGeneralAddress = False

            context[self.contextname] = {'coordonnees':coordonnees,'useGeneralAddress':useGeneralAddress}
            return ''
        except VariableDoesNotExist:
            return ''

def get_coordonnees_data(parser, token):
    bits = token.contents.split()
    if len(bits) !=3:
        raise TemplateSyntaxError, "get_coordonnees_data takes two arguments"
    return GetCoordonnees(bits[1],bits[2])

get_coordonnees_data = register.tag(get_coordonnees_data)