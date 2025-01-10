from django.urls import path
from .views import chat  # Chat fonksiyonunu import ediyoruz

urlpatterns = [
    path('chat/', chat, name='chat'),  # /chat/ endpointini tanımlıyoruz
]
