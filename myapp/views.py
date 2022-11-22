from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View

from jsignature.utils import draw_signature
from .models import ServerRoom
from .forms import ServerRoomForm


# Create your views here.

class SignatureView(View):

    model = ""
    template_name = "myapp/index.html"
    form = ServerRoomForm()

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


    def post(self, request, *args, **kwargs):

        return render(request, self.template_name)
