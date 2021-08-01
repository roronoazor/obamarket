from core.views import about_us, contact_us, index, properties
from django.urls import path


urlpatterns = [
    path('', index, name='index'),
    path('properties', properties, name='properties'),
    path('contact', contact_us, name='contact'),
    path('about', about_us, name='about'),
]