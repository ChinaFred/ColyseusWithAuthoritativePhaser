import face.server as server
from flask import render_template
import tools.general as general

app = server.current.app


@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")


general.log("-------------------------Admin Views initialized------------------------------------")





