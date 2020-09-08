from django.urls import path

from betterchoise import views

urlpatterns = [
    path('',views.index, name='index')
]
