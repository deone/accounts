DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'sql_mode': 'traditional',
        },
        'NAME': 'accounts_prod',
        'USER': 'accounts_user',
        'PASSWORD': 'Acc0untS',
        'HOST': '127.0.0.1',
        'PORT': '3306'
    }
}