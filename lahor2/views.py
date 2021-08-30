from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Lahore, Countie
from django.core.serializers import serialize
from django.http import HttpResponse


class HomePageView(TemplateView):
	template_name = 'index.html'

def lahore_datasets(request):
	lahores_shape = serialize('geojson', Lahore.objects.all())
	return HttpResponse(lahores_shape,content_type='json')


# Create your views here.
