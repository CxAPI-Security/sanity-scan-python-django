
'''
CUSTOM - to create hello routes
'''

from django.urls import path

from . import views

# Custom
urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:param>', views.param, name='param'),
]