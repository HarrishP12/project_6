from django.urls import path
from app.views import *
app_name='app'
urlpatterns=[
    path('harrish/',harrish,name='harrish')
]