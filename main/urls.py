from django.urls import path
from main.views import index, set_language, automation, about, service, partners, contact, shop
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path(_(''), index, name='index'),
    path('set_language/<str:lang_code>/', set_language, name='set_language'),
    path(_("automation/"), automation, name='automation'),
    path(_("about/"), about, name='about'),
    path(_("service/"), service, name='service'),
    path(_("partners/"), partners, name='partners'),
    path(_("contact/"), contact, name='contact'),
    path(_("shop/"), shop, name="shop")
    
    
]