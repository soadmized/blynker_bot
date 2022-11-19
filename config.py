import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

TOKEN = os.environ.get("TOKEN")
SERVER_HOST = os.environ.get("SERVER_HOST")
TEMP_ENDP = os.environ.get("TEMP_ENDP")
LIGHT_ENDP = os.environ.get("LIGHT_ENDP")
PIR_ENDP = os.environ.get("PIR_ENDP")
ADMIN_ID = os.environ.get("ADMIN_ID")
