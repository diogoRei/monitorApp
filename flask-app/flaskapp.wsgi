import sys
import logging

sys.path.insert(0,'/var/www/flask-app')
sys.path.insert(0,'/var/www/monitorApp/flask-app/venv/lib/python3.10/site-packages/')

#set up logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# import and run flask app
from app import app as application