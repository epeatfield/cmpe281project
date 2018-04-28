from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class HomeAuthPageView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'home_auth.html', context=None)
