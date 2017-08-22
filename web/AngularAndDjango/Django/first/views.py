from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class LinksPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'links.html', context=None)


class Customers(TemplateView):
    def getCust(request):
        name='liran'
        return HttpResponse('{ "name":"' + name + '", "age":31, "city":"New York" }')
