from django.contrib import admin
from django.urls import path, include  # include ekliyoruz

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatbot_app.urls')),  # chatbot_app'in URL'lerini ana projeye bağlıyoruz
]
