from django.urls import include, path

urlpatterns = [
    #http://127.0.0.1:8000/api/v1/jwt/create/
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
