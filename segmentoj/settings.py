"""
Django settings for segmentoj project.

Generated by 'django-admin startproject' using Django 3.0.2.

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
SECRET_KEY = (
    "sx!y=avrq(g1o+-7o2ef_4e*slekh5vtd-+6rs&c-nbfzw0*b^"  # CHANGE HERE ON PRODUCTION
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True  # CHANGE HERE ON PRODUCTION

ALLOWED_HOSTS = ["*"]  # CHANGE HERE ON PRODUCTION


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # API Framework
    "rest_framework",
    # CORS Control
    "corsheaders",
    # SegmentOJ Apps
    "account",
    "problem",
    "status",
    "captcha",
    "judger",  # Judger API
]

MIDDLEWARE = [
    "segmentoj.middleware.DisableCSRFCheck",  # Disable CSRF chack
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # Control CORS
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "segmentoj.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR + "/template"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "segmentoj.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases
# change here if want to change to MySQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",},
]

AUTH_USER_MODEL = "account.User"


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

# Time Zone, CHANGE HERE
TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"  # DON'T CHANGE THIS
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

# Session ID
# SESSION_SAVE_EVERY_REQUEST = False
# SESSION_COOKIE_AGE = 1209600

# User uploads file placses
MEDIA_ROOT = os.path.join(BASE_DIR, "uploads").replace("\\", "/")
MEDIA_URL = "/media/"  # DON'T CHANGE THIS

# CAPTCHA settings
# The height of each captcha pic
CAPTCHA_HEIGHT = 40
# The width of each captcha pic
CAPTCHA_WIDTH = 130
# The length of each captcha pic
CAPTCHA_LENGTH = 4
# font size on captcha
# you may change this if modified height/width
# try it until you find the best value
CAPTCHA_FONTSIZE = 30
# the font file of font
CAPTCHA_FONTTYPE = "/usr/share/fonts/truetype/noto/NotoMono-Regular.ttf"
# The number of dots on the pic to interfare
CAPTCHA_DOTNUM = 100
# The number of lines on the pic to interfare
CAPTCHA_LINENUM = 4
# how long a captcha expire (min)
CAPTCHA_AGE = 5

# CORS settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
SESSION_COOKIE_SAMESITE = "none"
# SESSION_COOKIE_SECURE = True     # ENABLE THIS if you server is based on HTTPS
SESSION_COOKIE_HTTPONLY = True  # DISABLE THIS ON PRODUCTION

REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_CLASSES": (
        "rest_framework.throttling.ScopedRateThrottle",  # use throttle_scope = 'xxx'
    ),
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 5,
}
