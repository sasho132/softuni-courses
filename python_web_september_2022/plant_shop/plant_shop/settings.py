import os
from pathlib import Path
from django.urls import reverse_lazy
from django.contrib.messages import constants as messages

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = bool(os.environ.get('DEBUG'))

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(' ')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'plant_shop.accounts',
    'plant_shop.store',
    'plant_shop.category',
    'plant_shop.cart',
    'plant_shop.orders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'plant_shop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'plant_shop.category.context_processors.menu_links',
                'plant_shop.cart.context_processors.counter',
            ],
        },
    },
]

WSGI_APPLICATION = 'plant_shop.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

AUTH_PWD_MODULE = "django.contrib.auth.password_validation."
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': f"{AUTH_PWD_MODULE}UserAttributeSimilarityValidator",
    },
    {
        'NAME': f"{AUTH_PWD_MODULE}MinimumLengthValidator",
    },
    {
        'NAME': f"{AUTH_PWD_MODULE}CommonPasswordValidator",
    },
    {
        'NAME': f"{AUTH_PWD_MODULE}NumericPasswordValidator",
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = reverse_lazy('login-user')
LOGIN_REDIRECT_URL = reverse_lazy('store')

AUTH_USER_MODEL = 'accounts.AppUser'

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}
