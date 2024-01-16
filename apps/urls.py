from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from apps.views import UserModelView, delete_product, AddProductView

urlpatterns = [
    path('', UserModelView.as_view(), name='index'),
    path('add_product',AddProductView.as_view(),name='add_product'),
    path('del/<int:pk>',delete_product,name='delete_product'),


]


