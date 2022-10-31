from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('rodadua/', include('rodadua.urls')),
    path('rodatiga/', include('rodatiga.urls')),
    path('rodaempat/', include('rodaempat.urls')),
]
