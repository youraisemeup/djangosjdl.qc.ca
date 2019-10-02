#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from sjdl.searchbac.models import *

def recherche_bacs_list(request):
    return render(request, "admin/baclist.html")