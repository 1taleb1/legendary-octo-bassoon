from datetime import datetime, timedelta
from hashlib import sha256
from time import sleep
from sqlalchemy import create_engine, MetaData, Table
import requests
import json
import urllib

from params import server, database, username, password, driver, schm


def to_ts(x):
    if x == '0':
        return None
    elif x == '':
        return None
    else:
        return datetime.fromtimestamp(int(x))
