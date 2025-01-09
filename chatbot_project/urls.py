from django.contrib import admin  # admin modülünü import ediyoruz
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin paneli
    path('', include('chatbot_app.urls')),  # Chatbot uygulaması için yönlendirme
]
