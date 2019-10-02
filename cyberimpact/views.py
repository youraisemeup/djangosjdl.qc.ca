#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
import requests, json
from django.http import HttpResponseRedirect
from django.contrib.sites.models import RequestSite
from sjdl.cyberimpact.models import CIForm

def subscribe(request):
    domaine = RequestSite(request).domain
    #print 'http://'+domaine+'/infolettre/confirmation'
    if request.method == 'POST':
        form = CIForm(request.POST)
        if request.POST.get("action") != "prefill":
            if form.is_valid():
                #make curl request here
                #if response ok, redirect to success page, else redirect to failure page
                params = {
                    'groups':'24',
                    'email':form.cleaned_data['email'],
                    'lastname':form.cleaned_data['lastname'],
                    'firstname':form.cleaned_data['firstname'],
                    'optinConfirmUrl':'http://'+domaine+'/infolettre/confirmation'
                }

                headers = {
                    'Content-Type':'application/json;encoding:utf-8',
                    'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3ZGEwYTVhMTJlMDEzNzcwM2ExZDYyMjMzZmViZGU1NyIsImlzcyI6IkN5YmVyaW1wYWN0IEFwcGxpY2F0aW9uIiwiYXVkIjoiYXBwLmN5YmVyaW1wYWN0LmNvbSIsImlhdCI6MTQ3OTI0NTI0MywibmJmIjowLCJyb2xlIjoic3lzYWRtaW4iLCJjaWQiOjgwMCwiZm4iOiJBZG1pbmlzdHJhdGV1ciIsImxuIjoiU3lzdFx1MDBlOG1lIiwiZW0iOiJwcm9ncmFtbWV1cnNAY3liZXJnZW5lcmF0aW9uLmNvbSIsInN1YiI6ODg1LCJ1c3IiOiJhZG1pbmlzdHJhdG9yIiwiZXhwIjoxNzk0NjA1MjQzfQ.R8Zj-Tivy3PrYaDpx1z5RW3gEdKLnlO3OhNyvymlMv0'
                }
                r = requests.post('https://apiv4.cyberimpact.com/members/optins', headers=headers, json=params)
                res = r.json()

                if r.status_code == 201: # Status Created
                    return HttpResponseRedirect('succes')
                else:
                    return HttpResponseRedirect('erreur')

    else:
        if request.GET:
            form = CIForm(request.GET)
        else:
            form = CIForm()

    return render(request, 'inscription.html',{'form':form})

def succes(request):
    return render(request,'reponse.html',{'reponse':'succes'})

def erreur(request):
    return render(request,'reponse.html',{'reponse':'erreur'})

def confirmation(request):
    return render(request,'reponse.html',{'reponse':'confirmation'})
