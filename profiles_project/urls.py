from django.urls import path, include
from django.contrib import admin
from profiles_api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles_api.urls'))
]
