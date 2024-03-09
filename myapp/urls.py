from django.contrib import admin
from django.urls import path, include
from myapp import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('', views.index, name='index'),
    path('export_excel/', views.export_excel, name='export_excel'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


