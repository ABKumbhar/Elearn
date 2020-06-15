"""
Django settings for Elearn project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#dyt^$y@b)qcfq9yf__v$29b1@=en9(co25wbwg(d=yir^w=p6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['elearn-rest.herokuapp.com','127.0.0.1','Aniket1999.pythonanywhere.com','aniket1999.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework.authtoken',
    'rest_framework',
    'django_cleanup.apps.CleanupConfig',
    'corsheaders',
     'Main',
    'djoser',
    'authdjoser',
    'rest_framework_swagger',

    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Elearn.urls'

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

WSGI_APPLICATION = 'Elearn.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

#Rest Framework configuration
REST_FRAMEWORK = {
 'DEFAULT_AUTHENTICATION_CLASSES' : (

        'rest_framework.authentication.TokenAuthentication',

         'rest_framework.authentication.SessionAuthentication',





 ),
 'DEFAULT_PERMISSIONS_CLASSES' : (
  'rest_framework.permissions.IsAuthenticated',
 ),

}

#Auth user model 
AUTH_USER_MODEL = 'authdjoser.User'
#Djoser
DJOSER = {
'PASSWORD_RESET_CONFIRM_URL' : '#/auth/users/reset_password_confirm/{uid}/{token}',
'USERNAME_RESET_CONFIRM_URL' : '#/username/reset/confirm/{uid}/{token}',
'ACTIVATION_URL' : '#/activate/{uid}/{token}',
'SEND_ACTIVATION_EMAIL': True,
'PASSWORD_CHANGED_EMAIL_CONFIRMATION' :True,
'LOGIN_FIELD' : 'email' ,
'USER_CREATE_PASSWORD_RETYPE' : True,
'SERIALIZERS' : {
'user' : 'authdjoser.serializers.UserSerializer',
'user_create' : 'authdjoser.serializers.UserCreateSerializer',

}
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
MEDIA_URL = '/document/'
STATICFILES_DIRS = [
os.path.join(BASE_DIR,'static')
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'static/document')
CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST =[
#     "http://localhost:3000",
#     "http://localhost:8000",
# ]

#Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

