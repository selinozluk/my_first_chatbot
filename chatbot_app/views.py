from django.shortcuts import render
from django.http import JsonResponse

# Türkçe ve İngilizce cevaplar
responses = {
    "tr": {
        "merhaba": "Merhaba! Size nasıl yardımcı olabilirim?",
        "nasılsın": "Ben bir chatbotum, ama iyi olduğumu söyleyebilirim!",
        "teşekkürler": "Rica ederim, başka bir sorunuz var mı?",
        "default": "Üzgünüm, bunu anlayamadım."
    },
    "en": {
        "hello": "Hello! How can I assist you?",
        "how are you": "I'm a chatbot, but I can say I'm fine!",
        "thanks": "You're welcome! Do you have any other questions?",
        "default": "Sorry, I didn't understand that."
    }
}

# Chatbot cevap mantığı
def chatbot_response(user_message, language):
    language = language if language in responses else "en"
    user_message = user_message.lower()
    return responses[language].get(user_message, responses[language]["default"])

# Chat görünüm fonksiyonu
def chat(request):
    if request.method == "POST":
        user_message = request.POST.get('message')
        language = request.POST.get('language', 'en')  # Varsayılan dil İngilizce
        bot_response = chatbot_response(user_message, language)
        return JsonResponse({"response": bot_response})
    return render(request, "chatbot_app/chat.html")  # Şablon dosyasını render ediyor