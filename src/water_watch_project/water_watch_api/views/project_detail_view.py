from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class ProjectDetailView(TemplateView):

    def get(self, request, **kwargs):
        return render(request, 'projdetail.html', context=None)
