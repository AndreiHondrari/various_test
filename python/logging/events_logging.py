

import logging

class CustomHandler(logging.Handler):

    def emit(self, record):
        print(f"SIKTEER {record} \n\n")
