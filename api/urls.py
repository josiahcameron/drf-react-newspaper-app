from django.urls import path, include


urlpatterns = [
    path('', include('articles.urls')),
    path('', include('accounts.urls')),
]