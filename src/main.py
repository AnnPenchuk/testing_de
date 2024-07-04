# -*- coding: utf-8 -*-
import os
import sys
import logging
import asyncio

import pytest

from API.api import api_request
from Validation.valid import Users_valid, list_users
from pydantic import BaseModel, EmailStr
from datetime import date
from uuid import UUID, uuid4
import re

#from bot import Bot
#from settings import settings


# Logging settings
# log_dir = os.path.join(os.getcwd(), "logs")
# log_file = os.path.join(log_dir, "logfile.log")



if __name__ == "__main__":
    res=api_request()
    list_users(res)
    logging.basicConfig(level=logging.INFO, filename="py_log.log",filemode="w")
    logging.debug("A DEBUG Message")
    logging.info("An INFO")
    logging.warning("A WARNING")
    logging.error("An ERROR")
    logging.critical("A message of CRITICAL severity")


