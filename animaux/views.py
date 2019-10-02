from django.shortcuts import render
from django.views import generic
from sjdl.animaux.forms import EnregistrementChienForm
from sjdl.animaux.models import EnregistrementChien


class EnregistrementChienFormView(generic.edit.FormView):
    template_name = "forms/enregistrement_chien.html"
    form_class = EnregistrementChienForm
    success_url = '?sent=1'
    model = EnregistrementChien

    def form_valid(self, form):

        form.send_email()
        form.save()

        return super(EnregistrementChienFormView, self).form_valid(form)
