from django.urls import path, include

app_name = 'Users'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]