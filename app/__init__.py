import os
from flask import Flask

app = Flask(__name__)

from app import routes

# Check db file and if None create app.db
if os.path.exists('app.db') == False:
    from app.database import init_db
    database.init_db()