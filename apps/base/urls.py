from django.urls import path
from apps.base.views import index

urlpatterns = [
    path('', index, name='index')
]