
from django.urls import path
from .views import *

urlpatterns = [
    path('',  MainPage.index_view),
    path('testing',  MainPage.testing_view_get),
    path('testing_post',  MainPage.testing_view_post),
    path('result',  MainPage.result_view),
    path('initial',  MainPage.initial_view)
]
