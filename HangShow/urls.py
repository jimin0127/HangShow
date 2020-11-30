from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('HS/',include('HS.urls')),
    path('admin/', admin.site.urls),
    path('index/', include('HS.urls')),
]
