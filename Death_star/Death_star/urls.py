from django.contrib import admin
from django.urls import path, include
from core.views import index_redirect

urlpatterns = [
    path('root_of_evil/', admin.site.urls),
    path('', index_redirect, name='index'),
    path('core/', include('core.urls', namespace='core')),
]
