from django.views.generic import TemplateView
from mysite.settings import DEBUG

class HomeView(TemplateView):
    template_name = 'home.html'