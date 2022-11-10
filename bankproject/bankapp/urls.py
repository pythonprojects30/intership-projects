from django.conf import settings
from django.conf.urls.static import static



from . import views
from django.urls import path


urlpatterns = [

    path('', views.index, name='index'),

    path('register/', views.register, name='register'),


    path('login/', views.login, name='login'),
    path('new/', views.new, name='new'),

    path('logout', views.logout, name='logout'),
    path('form/', views.form, name='form'),
    path('message/', views.msg, name='msg'),

]




#
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)