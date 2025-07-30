from pathlib import Path
from decouple import config, Csv

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)


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
    'myapi.middleware.schema_middleware.SchemaMiddleware',

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
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
        'OPTIONS': {
            'options': f"-c search_path={config('DB_SCHEMA', default='public')}"
        }
    }
}



LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
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



