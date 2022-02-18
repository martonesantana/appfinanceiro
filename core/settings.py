"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zk)44mhsc7cei6#h%_-6s*p5jv8f2chze4-7$u^_)4^j=&^^l5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'baton',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rangefilter',
    'phonenumber_field',
    'localflavor',
    'apps.config',
    'apps.financeiro',
    'baton.autodiscover',
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

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Bahia'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

#settings.py

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, '/static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BATON = {
    'SITE_HEADER': 'Financeiro',
    'SITE_TITLE': 'Financeiro',
    'SUPPORT_HREF': 'https://github.com/martonesantana/appfinanceiro',
    'COPYRIGHT': 'copyright © 2020 | martonesantana', # noqa
    'POWERED_BY': '<a href="https://www.linkedin.com/in/martonesantos/">Martone Santana</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'MENU_ALWAYS_COLLAPSED': False,
    'MENU_TITLE': 'Menu',
    'MESSAGES_TOASTS': False,
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'LOGIN_SPLASH': '/static/core/img/login-splash.png',
    'MENU': (
        { 'type': 'title', 'label': 'Administrativo', 'apps': ('auth', ) },
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Autenticação',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'user',
                    'label': 'Usuários',
                    'icon': 'fas fa-user-alt',
                },
                {
                    'name': 'group',
                    'label': 'Grupos',
                    'icon': 'fas fa-users',
                },
            )
        },
        {
            'type': 'app',
            'name': 'config',
            'label': 'Cadastros',
            'icon': 'fas fa-edit',
            'models': (
                {
                    'name': 'empresa',
                    'label': 'Empresas',
                    'icon': 'fas fa-building',
                },
                {
                    'name': 'planocontas',
                    'label': 'Plano de Contas',
                    'icon': 'fas fa-clipboard',
                },
                {
                    'name': 'categoria',
                    'label': 'Categorias',
                    'icon': 'fas fa-layer-group',
                },
                {
                    'name': 'fornecedor',
                    'label': 'Fornecedores',
                    'icon': 'fas fa-handshake',
                },
                {
                    'name': 'conta',
                    'label': 'Contas',
                    'icon': 'fas fa-landmark',
                },
                {
                    'name': 'centrocustos',
                    'label': 'Centros de Custos',
                    'icon': 'fas fa-boxes',
                },
            )
        },
                
        { 'type': 'title', 'label': 'Financeiro', 'app': 'financeiro' },
        {
            'type': 'app',
            'name': 'financeiro',
            'label': 'Financeiro',
            'icon': 'fas fa-coins',
            'models': (
                {
                    'name': 'contasapagar',
                    'label': 'Contas a Pagar',
                    'icon': 'fas fa-file-invoice-dollar',
                },
                
            )
        },
    ),        
    
}