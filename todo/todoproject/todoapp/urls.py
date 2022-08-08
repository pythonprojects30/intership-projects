from django.urls import path

from todoapp import views

app_name = 'todoapp'

urlpatterns = [
        path('',views.home,name='home'),
    # path('details',views.details,name='details')
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('listview/',views.tasklistview.as_view(),name='listview'),
    path('detailview/<int:pk>/',views.taskdetail.as_view(),name='detailview'),
    path('updateview/<int:pk>/',views.taskupdateview.as_view(),name='updateview'),
    path('deleteview/<int:pk>/',views.taskdeleteview.as_view(),name='deleteview'),
    ]