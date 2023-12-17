from django.urls import path, include

urlpatterns = [
    path('weather/', include('weather.urls')),
]
