from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path
app_name='ecartapp'
urlpatterns = [
path('',views.allproduct,name='allproduct'),
path('<slug:c_slug>/',views.allproduct,name='product_by_category'),
path('<slug:c_slug>/<slug:product_slug>/',views.prodetail,name='prodcat_detail')
    ]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                        document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)
