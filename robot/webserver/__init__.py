from flask import Flask
from flask import render_template
from robot import config

app = Flask(__name__)
config.init()
config.set_app(app)

print("----------------------------------server init----------------------------------------")


@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(500)
def ma_page_erreur(error):
    return render_template("public/errorpage.html", err=error, config=config.current)

print("--------------------------------Loading routes---------------------------------------")
from robot.webserver import views
from robot.webserver import admin_views
