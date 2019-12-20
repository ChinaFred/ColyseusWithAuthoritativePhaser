import datetime
from flask import Flask
from flask import render_template
import brain.config as config
print("------------------------------creating webserver-------------------------------------")
app = Flask(__name__, static_url_path="/static")
config.set_app(app)
#print("app.root_path: " + config.current.app.root_path)
#print("app.instance_path: " + config.current.app.instance_path)
#print("app: " + str(app))


print("------------------------------prepare error messages---------------------------------")


@app.errorhandler(401)
@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def ma_page_erreur(error):
    print("--------------------------------Error during a call----------------------------------")
    print(str(error))
    return render_template("public/errorpage.html", err=error, config=config.current)


print("--------------------------------Loading routes---------------------------------------")
from face.webserver import views
from face.webserver import admin_views
from face.webserver import views_submit
from face.webserver import views_ajax


print("--------------------------Creating template filters----------------------------------")


@app.template_filter()
def datetimefilter(value, format='%d-%m-%Y'):
    ret = ""
    if value:
        """Convert a datetime to a different format."""
        ret = datetime.datetime.strftime(value, format)
    return " " + ret


app.jinja_env.filters['datetimefilter'] = datetimefilter


def test():
    print("oulala")
