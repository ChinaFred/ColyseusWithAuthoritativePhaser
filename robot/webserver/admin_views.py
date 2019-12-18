from robot import webserver
from flask import render_template
from robot import config

app = config.current.app


@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")





