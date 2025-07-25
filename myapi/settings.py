from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-secret-key'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    # Apps de Django
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    # Apps de terceros
    'corsheaders',
    'rest_framework',
    'drf_yasg',

    # Tus apps locales
    'api',
    'apps.users',
    'apps.products',
    'apps.payments',

]





# 🧱 Middleware: funciones que se ejecutan en cada request/response
MIDDLEWARE = [
    # 🔄 Permite peticiones desde otros orígenes (útil para frontend separado)
    # 'corsheaders.middleware.CorsMiddleware',

    # 🔐 Seguridad básica (HTTPS, headers seguros, etc.)
    'django.middleware.security.SecurityMiddleware',

    # ⚠️ Manejo de sesiones (puedes quitarlo si no usas sesiones o cookies)
    'django.contrib.sessions.middleware.SessionMiddleware',

    # 🔁 Middleware común (manejo de cabeceras, redirecciones, etc.)
    'django.middleware.common.CommonMiddleware',

    # ⚠️ Protección contra CSRF (puedes quitarlo si usas solo APIs sin cookies)
    # 'django.middleware.csrf.CsrfViewMiddleware',

    # 🔐 Autenticación de usuarios (necesario si usas `request.user`)
    'django.contrib.auth.middleware.AuthenticationMiddleware',

    # ⚠️ Sistema de mensajes (puedes quitarlo si no usas `messages`)
    # 'django.contrib.messages.middleware.MessageMiddleware',

    # 🛡️ Prevención de ataques por iframes
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🌐 Archivo principal de rutas
ROOT_URLCONF = 'myapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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


# 🚀 Configuración WSGI (para producción con Gunicorn, etc.)
WSGI_APPLICATION = 'myapi.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', 
        'NAME': 'django_api_test',              
        'USER': 'michael',
        'PASSWORD': '',
        'HOST': 'localhost',                       
        'PORT': '5432',
        'OPTIONS': {
            'options': '-c search_path=api'
        }
    }
}

# 🔐 Validadores de contraseña (vacío para desarrollo)
AUTH_PASSWORD_VALIDATORS = []

# 🌍 Configuración regional
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 📦 Archivos estáticos (necesario para documentación Swagger o Ninja)
STATIC_URL = '/static/'

# 🌐 Permitir peticiones desde cualquier origen (solo para desarrollo)
CORS_ALLOW_ALL_ORIGINS = True



