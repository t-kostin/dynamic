from pathlib import Path
import environ

env = environ.Env(DEBUG=(bool, False))
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(BASE_DIR / 'devops.env')


DEVOPS_CONFIGURATION = {
    'DEBUG': env('DEBUG'),
    'SECRET_KEY': env('SECRET_KEY'),
    'DATABASES': {
        'default': env.db('DATABASE_URL'),
    },
    'ALLOWED_HOSTS': env.list('ALLOWED_HOSTS', default='localhost'),
    'CONSTANCE_BACKEND': env('CONSTANCE_BACKEND'),
}
