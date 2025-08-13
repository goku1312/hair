from django.urls import path
from . import views
from django.conf import settings # new
from  django.conf.urls.static import static #new
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('price/',views.price,name='price'),
    path('services/',views.services,name='services'),
 
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)