

from django.urls import include, re_path

from soapexample.views import my_soap_application

urlpatterns = [
    
    re_path(r'^soap_service/', my_soap_application),
]
