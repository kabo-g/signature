from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from django.contrib import messages

import json

from jsignature.utils import draw_signature
from .models import ServerRoom
from .forms import ServerRoomForm


# Create your views here.

class SignatureView(View):

    model = ServerRoom.objects.all()
    template_name = "myapp/results.html"
    form = ServerRoomForm

    def get(self, request, *args, **kwargs):
        context = {"data" : self.model}
        return render(request, self.template_name, context)


def myview(request):
    model = ServerRoom.objects.all()
    form = ServerRoomForm(request.POST or None)

    if form.is_valid():
        signature = form.cleaned_data.get('signature')

        # As an image
        if signature:
            signature_picture = draw_signature(signature)

            # As a file path
            signature_filepath = draw_signature(signature, as_file=True)

            form.save()
            return redirect("home")
    context = {"server_room" : model, "form":form}
    return render(request, "myapp/index.html", context)
