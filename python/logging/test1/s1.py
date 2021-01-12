
import logging
import logging.config
import logging.handlers

class CustomHandler(logging.Handler):

    def emit(self, record, *args, **kwargs):
        print(args)
        print(kwargs)
        x = record.bla if hasattr(record, 'bla') else None
        print(x)
        print(f"{record}\n{record.args}\n")



log_config = {
    'version': 1,
    'handlers': {
        'events': {
            'class': f'{__name__}.CustomHandler'
        }
    },

    'loggers': {
        'events': {
            'handlers': ['events'],
            'level': 'DEBUG'
        }
    }
}

logging.config.dictConfig(log_config)

events_logger = logging.getLogger('events')

events_logger.debug("Debggg", extra={'bla': 'zama'})
events_logger.info("enfo")
events_logger.warning("waneng")
events_logger.error("errar")
