import logging
import logging.config
import logging.handlers


log_config = {
    'version': 1,

    'handlers': {
        'h1': {
            'class': 'logging.StreamHandler',
        }
    },

    'loggers': {
        'logr1': {
            'handlers': ['h1'],
            'level': 'INFO'
        },
        'logr2': {
            'handlers': ['h1'],
            'level': 'ERROR'
        }
    }
}

logging.config.dictConfig(log_config)


l1 = logging.getLogger('logr1')
l2 = logging.getLogger('logr2')

l1.info("logr1 hello")
l2.info("logr2 hello")
l2.error('ahem')
