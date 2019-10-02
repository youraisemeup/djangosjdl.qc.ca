#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.template import Template, Context
from django.template.loader import render_to_string
from django.conf import settings

from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

def obfuscate_string(value):
    return ''.join(['&#{0:s};'.format(str(ord(char))) for char in value])

#inspired from
#https://github.com/morninj/django-email-obfuscator/blob/master/email_obfuscator/templatetags/email_obfuscator.py
def parse(kwargs):
    email = kwargs.get('email')
    text = kwargs.get('text')
    linkclass = kwargs.get('class')

    email_address = obfuscate_string(email)
    if text:
        link_text = text
    else:
        link_text = email_address

    encrypted_email = mark_safe('<a href="{0:s}{1:s}" class="{3:s}">{2:s}</a>'.format(obfuscate_string('mailto:'), email_address, link_text,linkclass))

    templatename = "shortcodes/encrypt_email.html"
    context = Context({
        'encryptedemail': encrypted_email
    })

    return render_to_string(templatename,context)