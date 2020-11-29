# from .celery.local import app as celery_local_app
from .celery.remote1 import app as celery_remote1_app

__all__ = ('celery_remote1_app',)
# __all__ = ('celery_local_app', 'celery_remote1_app',)
