from django.urls import path
from . import views as core_views


urlpatterns = [

    # Contracts View
    path('', core_views.home, name="home"),

]