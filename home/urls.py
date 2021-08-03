from django.contrib import admin
from django.urls import path, include
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name = 'home'),
    path('accounts/', include('allauth.urls')),
    path('upload/', views.upload, name="upload"),
    path('download/', views.download, name="download"),
    path('paid/',views.get_paid),
    path('free/',views.get_free),
    path('everyone/',views.get_ev),
    path('everyone_ten/',views.get_ev_ten),
    path('teen/',views.get_teen),
    path('mature/',views.get_mature),
    path('unrated/',views.get_unrated),
    path('adult/',views.get_adult),
    path('round/',views.get_round),


]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)