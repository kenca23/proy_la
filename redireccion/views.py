from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .models import redireccionamiento

class LalalaRedirect(View):
    def get(self, request, shortcode=None, *args, **kwargs):
        print(args)
        print(kwargs)
        print("shortcode = {sc}".format(sc=shortcode))
        obj = get_object_or_404(redireccionamiento, shortcode=shortcode)
        return HttpResponseRedirect(obj.url)


	# def post(self, request, *args, **kwargs):
	# 	