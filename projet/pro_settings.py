from .settings import *
import dj_database_url


SECRET_KEY = '2fut8887t6^qr1uod-$4_#0&0o&b8%6=(j=p9rm1md4v_@!b_q'

DEBUG = False
DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['sneezyapp.herokuapp.com']

