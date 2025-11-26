from .settings import *

# قاعدة بيانات في الذاكرة للاختبارات
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

# أي إعدادات أخرى خاصة بالاختبارات
DEBUG = False
