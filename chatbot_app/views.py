from django.shortcuts import render
from django.http import JsonResponse

# Chatbot adı
CHATBOT_NAME = "Selly"

# Çoklu dil desteği için cevaplar
responses = {
    "tr": {
        "merhaba": f"Merhaba! Ben {CHATBOT_NAME}, sizin chatbot'unuz. Size nasıl yardımcı olabilirim?",
        "nasılsın": f"Ben bir chatbotum, ama iyi olduğumu söyleyebilirim! Peki, sen nasılsın?",
        "şarkı öner": "Billie Eilish dinlemeyi seviyorsanız 'Birds of a Feather', 'Blue', 'The Greatest' şarkılarını öneririm. Slow şarkılar seviyorsanız Gigi Perez'den 'Sailor Song', Girl in Red'in 'Midnight Love' veya Lana Del Rey'in şarkılarını ('White Mustang', 'Cinnamon Girl', 'California', 'Born to Die', 'Dark Paradise') dinleyebilirsiniz. Eğer hareketli bir şeyler istiyorsanız Imagine Dragons'tan 'Enemy', 'Sharks', 'Monster', 'Wake Up' şarkılarını veya daha sert bir tarz için Fall Out Boy'dan 'The Phoenix', 'Death Valley' şarkılarını öneririm.",
        "kitap öner": "Kesinlikle 'Körlük' kitabını okumalısınız. Ayrıca, Freud'un psikoloji kitaplarını veya bilim kurgu için 'Harry Potter' serisini deneyebilirsiniz.",
        "film öner": "'Harry Potter' serisi büyü dolu bir dünyayı keşfetmek için harika bir seçimdir!", 
        "teşekkürler": "Rica ederim, başka bir sorunuz var mı?",
        "default": "Üzgünüm, bunu anlayamadım."
    },
    "en": {
        "hello": f"Hello! I'm {CHATBOT_NAME}, your chatbot. How can I assist you?",
        "how are you": "I'm a chatbot, but I can say I'm fine! How about you?",
        "song suggestion": "If you like Billie Eilish, I recommend 'Birds of a Feather', 'Blue', 'The Greatest'. For slower songs, try Gigi Perez's 'Sailor Song', Girl in Red's 'Midnight Love', or Lana Del Rey's hits ('White Mustang', 'Cinnamon Girl', 'California', 'Born to Die', 'Dark Paradise'). For more upbeat tracks, Imagine Dragons' 'Enemy', 'Sharks', 'Monster', 'Wake Up' are great, or for a harder style, try Fall Out Boy's 'The Phoenix', 'Death Valley'.",
        "book suggestion": "I suggest reading 'Blindness' by José Saramago. For psychology, try Freud's books, or explore the 'Harry Potter' series for sci-fi!",
        "movie suggestion": "The 'Harry Potter' series is a magical journey you shouldn't miss!",
        "thanks": "You're welcome! Do you have any other questions?",
        "default": "Sorry, I didn't understand that."
    },
    "es": {
        "hola": f"¡Hola! Soy {CHATBOT_NAME}. ¿Cómo puedo ayudarte?",
        "cómo estás": "¡Soy un chatbot, pero puedo decir que estoy bien! ¿Y tú?",
        "sugerencia de canción": "Si te gusta Billie Eilish, recomiendo 'Birds of a Feather', 'Blue', 'The Greatest'. Para canciones más lentas, prueba 'Sailor Song' de Gigi Perez, 'Midnight Love' de Girl in Red o los éxitos de Lana Del Rey ('White Mustang', 'Cinnamon Girl', 'California', 'Born to Die', 'Dark Paradise'). Para canciones más animadas, Imagine Dragons con 'Enemy', 'Sharks', 'Monster', 'Wake Up' son ideales, o para un estilo más duro, prueba Fall Out Boy con 'The Phoenix', 'Death Valley'.",
        "sugerencia de libro": "Te sugiero leer 'Ensayo sobre la ceguera' de José Saramago. Para psicología, prueba los libros de Freud o explora la serie 'Harry Potter'.",
        "sugerencia de película": "La serie de 'Harry Potter' es un viaje mágico que no debes perderte.",
        "gracias": "¡De nada! ¿Tienes alguna otra pregunta?",
        "default": "Lo siento, no entendí eso."
    },
    "fr": {
        "bonjour": f"Bonjour! Je m'appelle {CHATBOT_NAME}. Comment puis-je vous aider?",
        "comment ça va": "Je suis un chatbot, mais je peux dire que je vais bien! Et vous?",
        "suggestion de chanson": "Si vous aimez Billie Eilish, je recommande 'Birds of a Feather', 'Blue', 'The Greatest'. Pour des chansons plus douces, essayez 'Sailor Song' de Gigi Perez, 'Midnight Love' de Girl in Red ou les succès de Lana Del Rey ('White Mustang', 'Cinnamon Girl', 'California', 'Born to Die', 'Dark Paradise'). Pour des morceaux plus entraînants, Imagine Dragons avec 'Enemy', 'Sharks', 'Monster', 'Wake Up' sont excellents, ou pour un style plus dur, essayez Fall Out Boy avec 'The Phoenix', 'Death Valley'.",
        "suggestion de livre": "Je vous recommande de lire 'L'Aveuglement' de José Saramago. Pour la psychologie, essayez les livres de Freud ou explorez la série 'Harry Potter'.",
        "suggestion de film": "La série 'Harry Potter' est un voyage magique à ne pas manquer!",
        "merci": "De rien! Avez-vous d'autres questions?",
        "default": "Désolé, je n'ai pas compris cela."
    },
    "de": {
        "hallo": f"Hallo! Ich bin {CHATBOT_NAME}. Wie kann ich Ihnen helfen?",
        "wie geht es dir": "Ich bin ein Chatbot, aber ich kann sagen, dass es mir gut geht! Und dir?",
        "song empfehlung": "Wenn Sie Billie Eilish mögen, empfehle ich 'Birds of a Feather', 'Blue', 'The Greatest'. Für langsamere Songs probieren Sie 'Sailor Song' von Gigi Perez, 'Midnight Love' von Girl in Red oder die Hits von Lana Del Rey ('White Mustang', 'Cinnamon Girl', 'California', 'Born to Die', 'Dark Paradise'). Für lebhaftere Songs sind Imagine Dragons mit 'Enemy', 'Sharks', 'Monster', 'Wake Up' großartig, oder für einen härteren Stil probieren Sie Fall Out Boy mit 'The Phoenix', 'Death Valley'.",
        "buch empfehlung": "Ich empfehle Ihnen, 'Die Blendung' von José Saramago zu lesen. Für Psychologie versuchen Sie Freuds Bücher oder erkunden Sie die 'Harry Potter'-Serie.",
        "film empfehlung": "Die 'Harry Potter'-Serie ist eine magische Reise, die Sie nicht verpassen sollten!",
        "danke": "Bitte schön! Haben Sie noch weitere Fragen?",
        "default": "Entschuldigung, das habe ich nicht verstanden."
    },
    "ja": {
        "こんにちは": f"こんにちは！私は{CHATBOT_NAME}です。どのようにお手伝いできますか？",
        "お元気ですか": "私はチャットボットですが、元気です！あなたはどうですか？",
        "おすすめの歌": "Billie Eilishが好きなら、'Birds of a Feather'、'Blue'、'The Greatest'をおすすめします。スローな曲が好きなら、Gigi Perezの'Sailor Song'、Girl in Redの'Midnight Love'やLana Del Reyの曲 ('White Mustang', 'Cinnamon Girl', 'California', 'Born to Die', 'Dark Paradise')を試してみてください。もっとアップテンポな曲ならImagine Dragonsの'Enemy', 'Sharks', 'Monster', 'Wake Up'や、Fall Out Boyの'The Phoenix', 'Death Valley'がおすすめです。",
        "おすすめの本": "ジョゼ・サラマーゴの『ブラインドネス』を読むことをおすすめします。心理学にはフロイトの本や、SFなら『ハリー・ポッター』シリーズを試してみてください。",
        "おすすめの映画": "『ハリー・ポッター』シリーズは、見逃せない魔法の旅です！",
        "ありがとう": "どういたしまして！他に質問がありますか？",
        "default": "すみません、それは理解できませんでした。"
    }
}

# Chatbot cevap mantığı
def chatbot_response(user_message, language):
    language = language if language in responses else "en"
    user_message = user_message.lower()

# Şarkı türü seçimine göre yanıtlar
def chatbot_response(user_message, language):
    language = language if language in responses else "en"
    user_message = user_message.lower()

    # Şarkı türü seçimine göre yanıtlar
    if user_message in ["şarkı öner", "song suggestion", "sugerencia de canción", "suggestion de chanson", "song empfehlung", "おすすめの歌"]:
        return "Ne tür şarkılar dinlemeyi seversiniz? Slow, hareketli, sert, pop rock, alternatif rock veya pop punk mı?"

    if user_message in ["slow", "yavaş", "lent", "langsam", "スロー"]:
        return "Slow şarkılar için Billie Eilish'ten 'Birds of a Feather', Gigi Perez'den 'Sailor Song', Girl in Red'in 'Midnight Love' veya Lana Del Rey'in şarkılarını öneririm ('White Mustang', 'Cinnamon Girl', 'California')."

    if user_message in ["hareketli", "energetic", "movido", "énergique", "lebhaft", "エネルギッシュ"]:
        return "Imagine Dragons'tan 'Enemy', 'Sharks', 'Monster' şarkılarını dinleyebilirsiniz."

    if user_message in ["sert", "hard", "duro", "dur", "hart", "ハード"]:
        return "Fall Out Boy'dan 'The Phoenix', 'Death Valley' şarkılarını öneririm."

    if user_message in ["pop rock", "pop-rock", "poprock"]:
        return "Pop rock için Imagine Dragons'tan 'Enemy', 'Sharks', 'Monster', Coldplay'den 'Yellow', 'Sparks', 'Viva La Vida' veya Linkin Park'tan 'In the End', 'Numb', 'Castle of Glass' şarkılarını öneririm."

    if user_message in ["alternatif rock", "alternative rock", "rock alternativo", "rock alternatif", "オルタナティブロック"]:
        return "Alternatif rock için Radiohead'den 'Creep', 'Karma Police', 'No Surprises' veya Linkin Park'tan 'In the End', 'Numb', 'Castle of Glass' şarkılarını öneririm."

    if user_message in ["pop punk", "pop-punk", "poppunk"]:
        return "Pop punk için Fall Out Boy'dan 'The Phoenix', 'Death Valley', ayrıca Paramore'dan 'Misery Business', 'Decode' şarkılarını öneririm."

    return responses[language].get(user_message, responses[language]["default"])


# Kitap önerileri kategorilere göre çoklu dil desteğiyle
book_recommendations = {
    "fantastik": {
        "tr": [
            {"title": "Alacakaranlık", "author": "Stephenie Meyer"},
            {"title": "Odysseia", "author": "Homeros"},
            {"title": "Harry Potter", "author": "J.K. Rowling"}
        ],
        "en": [
            {"title": "Twilight", "author": "Stephenie Meyer"},
            {"title": "The Odyssey", "author": "Homer"},
            {"title": "Harry Potter", "author": "J.K. Rowling"}
        ],
        "es": [
            {"title": "Crepúsculo", "author": "Stephenie Meyer"},
            {"title": "La Odisea", "author": "Homero"},
            {"title": "Harry Potter", "author": "J.K. Rowling"}
        ],
        "fr": [
            {"title": "Twilight", "author": "Stephenie Meyer"},
            {"title": "L'Odyssée", "author": "Homère"},
            {"title": "Harry Potter", "author": "J.K. Rowling"}
        ],
        "de": [
            {"title": "Bis(s) zum Morgengrauen", "author": "Stephenie Meyer"},
            {"title": "Die Odyssee", "author": "Homer"},
            {"title": "Harry Potter", "author": "J.K. Rowling"}
        ],
        "ja": [
            {"title": "トワイライト", "author": "ステファニー・メイヤー"},
            {"title": "オデュッセイア", "author": "ホメロス"},
            {"title": "ハリー・ポッター", "author": "J.K.ローリング"}
        ]
    }
}

# Kitap önerisi yanıtlarını çok dilli hale getiren fonksiyon
def get_book_recommendations(category, language):
    if category in book_recommendations and language in book_recommendations[category]:
        books = book_recommendations[category][language]
        return ", ".join([f"{book['title']} ({book['author']})" for book in books])
    return "Üzgünüm, bu kategori için öneri bulunamadı."

# Chatbot cevap mantığı
def chatbot_response(user_message, language):
    language = language if language in responses else "en"
    user_message = user_message.lower()

    # Kitap türü sorusu
    if user_message in ["kitap öner", "book suggestion", "sugerencia de libro", "suggestion de livre", "buch empfehlung", "本のおすすめ"]:
        return "Hangi tür kitaplardan hoşlanıyorsunuz? Fantastik, psikoloji, klasikler, modern edebiyat veya felsefe mi?"

    if user_message in ["fantastik", "fantasy", "fantasía", "fantastique", "fantastisch", "ファンタジー"]:
        return get_book_recommendations("fantastik", language)

    # Varsayılan yanıtlara dön
    return responses[language].get(user_message, responses[language]["default"])

# Chat görünüm fonksiyonu
def chat(request):
    if request.method == "POST":
        user_message = request.POST.get('message')
        language = request.POST.get('language', 'en')  # Varsayılan dil İngilizce
        bot_response = chatbot_response(user_message, language)
        return JsonResponse({"response": bot_response}, json_dumps_params={"ensure_ascii": False})
    return render(request, "chatbot_app/chat.html", {"response": f"Ben {CHATBOT_NAME}, sizin chatbot'unuz. Mesajınızı yazın ve gönderin."})
