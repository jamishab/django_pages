# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
    # if someone goes to the about page it shows "about" and if someone goes to the home page it shows "home"
]
