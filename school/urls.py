from django.urls import path
from .views import schoolView
urlpatterns = [
    path('', schoolView, name="school"),
]
