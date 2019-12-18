from flask import Flask
from flask import render_template
#from app import config


from app import views
from app import admin_views

app = Flask(__name__)
#config.init()


@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(500)
def ma_page_erreur(error):
 return "hello"
 #   return render_template("public/errorpage.html", err=error, config=config.current)
