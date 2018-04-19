from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class ContactView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'contact.html', context=None)
