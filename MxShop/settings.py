"""
Django settings for MxShop project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os, sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#r@h(x*x2jc5o^-y#9=9w)o7iiv7jd^zxp@1s5*nj-n*s)v#o*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['*']
ALLOWED_HOSTS = [ ]

#重载系统的用户，让UserProfile生效
AUTH_USER_MODEL = 'users.UserProfile'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'users',
    'goods',
    'trade',
    'user_operation',
    'rest_framework',
    'xadmin',
    'crispy_forms',
    'DjangoUeditor',
    'django_filters',
    'corsheaders',
    'reversion',
    'coreschema',
    'rest_framework.authtoken',
    'social_django',
]


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
)

ROOT_URLCONF = 'MxShop.urls'

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
                #第三方登录
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'MxShop.wsgi.application'


AUTHENTICATION_BACKENDS = (
    'users.views.CustomBackend',
    'social_core.backends.weibo.WeiboOAuth2',
    'social_core.backends.qq.QQOAuth2',
    'social_core.backends.weixin.WeixinOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mxshop4',        #数据库名字
        'USER': 'root',          #账号
        'PASSWORD': 'm',    #密码
        # 'HOST': '47.93.198.159',     #IP
        'HOST': '127.0.0.1',     #IP
        'PORT': '3306',          #端口
        #这里引擎用innodb（默认myisam）
        #因为后面第三方登录时，要求引擎为INNODB
        # 'OPTIONS':{'init_command': 'SET storage_engine=INNODB'},    #按照课程会报错，改为
        "OPTIONS":{"init_command":"SET default_storage_engine=INNODB;"}
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

# 设置上传文件的路径
MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media")

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    #限速设置
    'DEFAULT_THROTTLE_CLASSES': (
            'rest_framework.throttling.AnonRateThrottle',   #未登陆用户
            'rest_framework.throttling.UserRateThrottle'    #登陆用户
        ),
    'DEFAULT_THROTTLE_RATES': {
        'anon': '20000000/minute',                   #每分钟可以请求两次
        'user': '20000000/minute'                    #每分钟可以请求五次
    }
}

import datetime
#有效期限
JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=7),    #也可以设置seconds=20
    'JWT_AUTH_HEADER_PREFIX': 'JWT',                       #JWT跟前端保持一致，比如“token”这里设置成JWT
}

#手机号验证
REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
#云片网APIKEY
APIKEY = "2e87d17327d4be01608f7c6da23ecea2"
# 支付宝相关的key
private_key_path = os.path.join(BASE_DIR, 'apps/trade/keys/private_2048.txt')
ali_pub_key_path = os.path.join(BASE_DIR, 'apps/trade/keys/alipay_key_2048.txt')
#缓存配置
REST_FRAMEWORK_EXTENSIONS = {
    'DEFAULT_CACHE_RESPONSE_TIMEOUT': 5   #5s过期，时间自己可以随便设定
}

# # redis缓存
# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379",
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }

# 第三方登录，里面的值是你的开放平台对应的值
SOCIAL_AUTH_WEIBO_KEY = '224188xxxx'
SOCIAL_AUTH_WEIBO_SECRET = '76daf2e9xxxxx'

SOCIAL_AUTH_QQ_KEY = 'xxxxxxx'
SOCIAL_AUTH_QQ_SECRET = 'xxxxxxx'

SOCIAL_AUTH_WEIXIN_KEY = 'xxxxxxx'
SOCIAL_AUTH_WEIXIN_SECRET = 'xxxxxxx'
#登录成功后跳转到首页
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/index/'





