DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "0f9e1e31-ae17-45c8-a333-7c00d9296f833f2b6ef4-9749-4fc5-97ad-8ab40b68e558c28c1cae-c8bb-4bbc-af8f-b00fda8fbee9"
NEVERCACHE_KEY = "0645be0f-86bb-4a29-b1cf-da149b54d8b33a84de56-2e12-40f7-b638-03f8369281a1a1f82d31-8b8d-4873-9c50-84392c20386e"


DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME': '_marie_django_tesxt',
        'USER': '_marie_django_test',
        'PASSWORD': 'patate04%',
        'HOST': 'harryX.cybergeneration.com'
    }
}
