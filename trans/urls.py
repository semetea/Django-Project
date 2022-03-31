from unicodedata import name
from django.urls import path
from . import views

app_name="trans"
urlpatterns = [
    path('index/', views.index, name="index")

]