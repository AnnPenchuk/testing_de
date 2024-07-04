# -*- coding: utf-8 -*-
import os
import sys
import logging
import asyncio
from API.api import api_request
from Validation.valid import Users

#from bot import Bot
#from settings import settings


# Logging settings
#log_dir = os.path.join(os.getcwd(), "logs")
#log_file = os.path.join(log_dir, "logfile.log")


if __name__ == "__main__":
    api_request()
    Users()
    logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")
    logging.debug("A DEBUG Message")
    logging.info("An INFO")
    logging.warning("A WARNING")
    logging.error("An ERROR")
    logging.critical("A message of CRITICAL severity")


