
from django.urls import path

from movieapp import views
app_name = "movieapp"
urlpatterns = [
    path('',views.details,name='details'),
    path('movie/<int:movie_id>/',views.details1,name='details1'),
    path('add/',views.add,name='add'),
    path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/',views.delete,name='delete')
]
