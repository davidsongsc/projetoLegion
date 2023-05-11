from django.urls import path
from portifolio.views import home

urlpatterns = [
    path('', home, name='home'),
]
