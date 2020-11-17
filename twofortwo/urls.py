from django.urls import path, include
from django.contrib import admin

app_name = 'twofortwo'
urlpatterns = [
  path('', include('tradefood.urls')),
  path('admin/', admin.site.urls),
]
