"""
Django settings for mutawebsite project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import json


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%3e8-dh-!f24(_r^uesuzca=a^snk5_t@p!%hr$*(y+94s3#g-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

####datos de configuración
ruta= os.path.dirname(os.path.abspath(__file__))
f = open('{}/conf.json'.format(ruta), 'r')
conf_string = f.read()
f.close()
conf = json.loads(conf_string)

RUTA=conf['ruta']
RUTA2=conf['ruta2']

# Application definition

INSTALLED_APPS = [
    # 'material',
    # 'material.admin',
    'admin_volt.apps.AdminVoltConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    
  
    
    
]

# MATERIAL_ADMIN_SITE = {
    
#     'FAVICON':  'path/to/favicon',  # Admin site favicon (path to static should be specified)
#     'MAIN_BG_COLOR':  '#d32f2f',  # Admin site main color, css color should be specified
#     'MAIN_HOVER_COLOR':  '#455a64',  # Admin site main hover color, css color should be specified
#     # 'PROFILE_PICTURE':  'path/to/image',  # Admin site profile picture (path to static should be specified)
#     # 'PROFILE_BG':  'path/to/image',  # Admin site profile background (path to static should be specified)
#     # 'LOGIN_LOGO':  'path/to/image',  # Admin site logo on login page (path to static should be specified)
#     # 'LOGOUT_BG':  'path/to/image',  # Admin site background on login/logout pages (path to static should be specified)
#     'SHOW_THEMES':  True,  #  Show default admin themes button
#     # 'TRAY_REVERSE': True,  # Hide object-tools and additional-submit-line by default
#     # 'NAVBAR_REVERSE': True,  # Hide side navbar by default
#     # 'SHOW_COUNTS': True, # Show instances counts for each model
#     # 'APP_ICONS': {  # Set icons for applications(lowercase), including 3rd party apps, {'application_name': 'material_icon_name', ...}
#     #     'sites': 'send',
#     # },
#     # 'MODEL_ICONS': {  # Set icons for models(lowercase), including 3rd party models, {'model_name': 'material_icon_name', ...}
#     #     'site': 'contact_mail',
#     # }
# }

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'website.urls'

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

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'basedato',
        'USER': 'root',
        'PASSWORD': 'asnaeb123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es'

# TIME_ZONE = 'America/Santiago'
TIME_ZONE = 'UTC'


USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL='/assets/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'assets'),
)

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


SESSION_COOKIE_AGE = 6000

SESSION_EXPIRE_AT_BROWSER_CLOSE = True


