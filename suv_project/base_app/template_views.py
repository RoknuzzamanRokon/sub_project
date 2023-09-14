from django.views.generic import TemplateView

class HomePageViews(TemplateView):
    template_name = 'home.html'
    

class AboutViews(TemplateView):
    template_name = 'about.html'


class ContactViews(TemplateView):
    template_name = 'contact.html'
    
    