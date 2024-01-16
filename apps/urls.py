from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from apps.views import UserModelView, delete_product, add_product

urlpatterns = [
    path('', UserModelView.as_view(), name='index'),
    path('add_product',add_product,name='add_product')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
