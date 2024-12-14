from django.shortcuts import render, redirect
from django.utils import translation
from django.contrib.sessions.models import Session
from django.shortcuts import redirect
from django.conf import settings






def set_language(request, lang_code):

    translation.activate(lang_code)

    request.session[settings.LANGUAGE_SESSION_KEY] = lang_code
    
  
    return redirect(request.META.get('HTTP_REFERER', '/'))




def index(request):
    return render(request, 'main/index.html')



def automation(request):
    return render(request, 'main/avtomatlashtirish.html')
    
    
 
def about(request):
    return render(request, "main/about.html")    



def service(request):
    return render(request, "main/service.html")



def partners(request):
    return render(request, "main/partners.html")




def contact(request):
    return render(request, "main/contact.html")



def shop(request):
    return render(request, "main/shop.html")