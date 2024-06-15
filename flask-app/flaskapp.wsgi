import sys
import logging

sys.path.insert(0,'/var/www/monitorApp/flask-app')
sys.path.insert(0,'/var/www/monitorApp/flask-app/venv/Lib/site-packages/')
sys.path.insert(0,'/var/www/monitorApp')
#set up logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# import and run flask app
from app import app as application