from django.shortcuts import render
import datetime  
from django.http import HttpResponse  
from django.views.generic import DetailView


# Create your views here.  
def index(request):  
    now = datetime.datetime.now()  
    html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
    
    return HttpResponse(html)    # rendering the template in HttpResponse  


class Index_2(DetailView):
    def index(request):  
        now = datetime.datetime.now()  
        html = "<html><body><h3>Now time is %s.</h3></body></html>" % now  
        
        return HttpResponse(html)
    
    
    
    