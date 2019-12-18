from flask import Flask

app = Flask(__name__)
botName = "Terminator"

from app import views
from app import admin_views


@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(500)
def ma_page_erreur(error):
    return "Ma jolie page {}".format(error.code), error.code
