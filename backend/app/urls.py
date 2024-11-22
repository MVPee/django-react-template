from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('srcs.api.urls')),
    path('', include('srcs.user.urls')),
]
