from . import views
from django.urls import path

urlpatterns = [
    path('', views.tb, name='tb'),
    path('face/', views.face, name='face'),

]
