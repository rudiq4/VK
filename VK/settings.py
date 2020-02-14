import os
from django.urls import reverse_lazy

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '(hvdi8nvk!ndffn^0_)7#@e^1-g93n6juh$7y9l#vijx9b_5h3'

DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1', 'cd1c4c34.ngrok.io']

INSTALLED_APPS = [
    'account.apps.AccountConfig',  # account
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'sorl.thumbnail',
    'content.apps.ContentConfig',
    'slugify',
    'actions.apps.ActionsConfig'
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

ROOT_URLCONF = 'VK.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
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

WSGI_APPLICATION = 'VK.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'uk'

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'

LOGIN_REDIRECT_URL = 'dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'



MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # main
    'account.authentication.EmailAuthBackend',  # alternative
    'social_core.backends.facebook.FacebookOAuth2',  # FB
    'social_core.backends.twitter.TwitterOAuth',  # TWITTER  (Doesnt work)
    'social_core.backends.google.GoogleOAuth2'  # Google
]

# for facebook

SOCIAL_AUTH_FACEBOOK_KEY = '707605776441143'  # Facebook App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '199167f3d6ddb572008c9b69db751290'  # Facebook App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

ABSOLUTE_URL_OVERRIDES = {  # same 'get_absolute_url'x
    'auth.user': lambda u: reverse_lazy('user_detail', args=[u.username])
}
# Django динамически добавляет метод get_absolute_url() для каждой модели перечисленной в настройке
