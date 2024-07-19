# code
from operator import index
from . import views
from django.contrib import admin
from django.urls import path


urlpatterns = [
	path('admin/', admin.site.urls),
	path("", views.home),
	path("predict/", views.predict),
	path("predict/result", views.result),
]
