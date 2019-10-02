#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template import Library, Node, Variable, VariableDoesNotExist, TemplateSyntaxError
from django.db import models
from itertools import chain
from operator import attrgetter
from django import template
import datetime
from datetime import date
import re
import locale
from sjdl.usefullinks.models import UsefulLinks, RepertoryLinks
from sjdl.common.models import DocumentPage

register = Library()

@register.simple_tag(takes_context=True)
def PageHasChildren(context):
    if "page" in context:
        page = context['page']
        pages = DocumentPage.objects.filter(parent_id = page.id)
        if len(pages) > 0:
            context['page_has_children'] = True
    else:
        context['page_has_children'] = False
    return ''

class GetUsefulLinks(Node):
    def __init__(self, category, varname):
        self.varname = varname
        self.category = category

    def render(self,context):
        try:

            usefullinks = UsefulLinks.objects.filter(
                models.Q(publish_date__lte = datetime.datetime.now()) | models.Q(publish_date__isnull = True)
            ).filter(
                models.Q(expiry_date__gte = datetime.datetime.now()) | models.Q(expiry_date__isnull = True)
            ).filter(
                status = 2
            ).filter(
                categorie = self.category
            ).order_by('title')

            #print usefullinks

            repertorylinks = RepertoryLinks.objects.filter(
                models.Q(publish_date__lte = datetime.datetime.now()) | models.Q(publish_date__isnull = True)
            ).filter(
                models.Q(expiry_date__gte = datetime.datetime.now()) | models.Q(expiry_date__isnull = True)
            ).filter(
                status = 2
            ).filter(
                usefullink_category = self.category
            ).order_by('title')

            links = chain(usefullinks,repertorylinks)

            links = sorted(links, key=attrgetter('title'), cmp=locale.strcoll)

            context[self.varname] = links
            return ''
        except VariableDoesNotExist:
            return ''

def get_usefullinks_list(parser, token):
    bits = token.contents.split()
    if len(bits) !=3:
        raise TemplateSyntaxError, "get_usefullinks_list takes two arguments"
    return GetUsefulLinks(bits[1],bits[2])

get_usefullinks_list = register.tag(get_usefullinks_list)

#templatetag used to add special class to body
#some sections gets a different color
class SectionClass(Node):
    def __init__(self, page, varname):
        self.varname = varname
        self.page = Variable(page)

    def render(self,context):
            try:
                actual_page = self.page.resolve(context)
                #print actual_page
                serviceclass = ''
                if re.search('^services-municipaux/environnement(/.*)?',actual_page):
                    serviceclass = 'sectionclass environnement'

                elif re.search('(travaux-publics)(/.*)?',actual_page):
                    serviceclass = 'sectionclass travauxpublics'

                elif re.search('(transport-collectif)(/.*)?',actual_page):
                    serviceclass = 'sectionclass travauxpublics'

                elif re.search('(hygiene-du-milieu)(/.*)?',actual_page):
                    serviceclass = 'sectionclass travauxpublics'

                elif re.search('^services-municipaux/urbanisme(/.*)?',actual_page):
                    serviceclass = 'sectionclass urbanisme'

                elif re.search('^loisirs-et-culture(/.*)?',actual_page):
                    serviceclass = 'sectionclass loisirs'

                elif re.search('(securite-incendie)(/.*)?',actual_page):
                    serviceclass = 'sectionclass securiteincendie'

                elif re.search('(conseil-municipal)(/.*)?',actual_page):
                    serviceclass = 'sectionclass conseilmunicipal'

                context[self.varname] = serviceclass
                return ''
            except VariableDoesNotExist:
                return ''

def get_section_class(parser, token):
    bits = token.contents.split()
    #print bits
    if len(bits) !=3:
        raise TemplateSyntaxError, "get_service_class takes two arguments"
    return SectionClass(bits[1],bits[2])

get_section_class = register.tag(get_section_class)


@register.filter('fieldtype')
def fieldtype(ob):
    return ob.__class__.__name__




# Class to get the header image
class PageHeader(Node):
    def __init__(self, contextname):
        self.contextname = contextname

    def render(self, context):
        try:
            bandeau = ''

            year = datetime.date.today().year
            current_date = datetime.date(datetime.date.today().year, datetime.date.today().month, datetime.date.today().day)
            if current_date >= datetime.date(year, 1, 1) and current_date <= datetime.date(year, 3, 21):
                bandeau = 'bandeau-hiver'
            elif current_date >= datetime.date(year, 12, 1) and current_date <= datetime.date(year, 12, 31):
                bandeau = 'bandeau-hiver'
            elif current_date >= datetime.date(year, 3, 22) and current_date <= datetime.date(year, 6, 20):
                bandeau = 'bandeau-printemps'
            elif current_date >= datetime.date(year, 6, 21) and current_date <= datetime.date(year, 9, 21):
                bandeau = 'bandeau-ete'
            elif current_date >= datetime.date(year, 9, 22) and current_date <= datetime.date(year, 11, 30):
                bandeau = 'bandeau-automne'

            context[self.contextname] = bandeau
            return ''
        except VariableDoesNotExist:
            return ''


def get_page_header(parser, token):
    bits = token.contents.split()
    # print bits
    if len(bits) != 2:
        raise template.TemplateSyntaxError("get_page_header takes one argument")
    return PageHeader(bits[1])

get_page_header = register.tag(get_page_header)





@register.filter('youtubeid')
def youtubeid(url):
    regex = '^(?:https?:\/\/)?(?:www\.)?(?:youtu\.be\/|youtube\.com\/(?:embed\/|v\/|watch\?v=|watch\?.+&v=))((?:\w|-){11})(?:&list=(\S+))?$'
    match = re.search(regex,url)

    if match.group(1):
        #print match.group(1)
        return match.group(1)
    else:
        return None