from django.contrib import admin
from django.urls import path
from homepage import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index , name="index"),
    path('video', views.video , name="video"),
    path('music', views.music , name="music"),

]