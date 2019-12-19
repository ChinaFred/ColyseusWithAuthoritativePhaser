import datetime
from flask import Flask
from flask import render_template
from robot import config

app = Flask(__name__)
config.init()
config.set_app(app)

print("----------------------------------server init----------------------------------------")


@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def ma_page_erreur(error):
    return render_template("public/errorpage.html", err=error, config=config.current)

print("--------------------------------Loading routes---------------------------------------")

from robot.webserver import views
from robot.webserver import admin_views
from robot.webserver import views_submit
from robot.webserver import views_ajax


print("--------------------------Creating template filters----------------------------------")


@app.template_filter()
def datetimefilter(value, format='%d-%m-%Y'):
    ret = ""
    if value:
        """Convert a datetime to a different format."""
        ret = datetime.datetime.strftime(value, format)
    return " " + ret


app.jinja_env.filters['datetimefilter'] = datetimefilter


