from django.urls import path
from hangout.views import *

urlpatterns = [
    path('', index, name='index'),
    path('hangout/', hangout, name='hangout'),
    path('confirm/', confirm, name='confirm'),
    path('redirectfb/', redirect_facebook, name='redirectfb'),
    path('thinking/', thinking, name='thinking'),
]