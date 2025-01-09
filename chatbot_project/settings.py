from pathlib import Path
from decouple import config  # python-decouple kullanımı için

# Projenin temel dizini
BASE_DIR = Path(__file__).resolve().parent.parent

# Gizli anahtar ve debug ayarı
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Uygulama tanımları
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'chatbot_app',  # Sizin uygulamanız
]

# Ara katmanlar (Middleware)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Ana URL ayarları
ROOT_URLCONF = 'chatbot_project.urls'

# Şablon ayarları
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # Şablon dosyalarınız varsa buraya dizin ekleyebilirsiniz
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI ayarları
WSGI_APPLICATION = 'chatbot_project.wsgi.application'

# Veritabanı ayarları
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='3306'),
    }
}

# Şifre doğrulama
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Uluslararasılaştırma (Internationalization)
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Statik dosya ayarları
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # Statik dosyalar için dizin
STATIC_ROOT = BASE_DIR / 'staticfiles'   # Üretim ortamı için statik dosyaların toplandığı yer

# CSRF güvenlik ayarları
CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', default='http://127.0.0.1,http://localhost').split(',')

# Varsayılan birincil anahtar alan tipi
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
