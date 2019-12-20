
from flask import render_template
import brain.config as config

app = config.current.app


@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")





