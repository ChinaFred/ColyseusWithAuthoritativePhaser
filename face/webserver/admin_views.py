import face.server as server
from face.server import log
from flask import render_template


app = server.current.app


@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")


log("-------------------------Admin Views initialized------------------------------------")





