from flask import render_template



@app.route("/simple")
def index_simple():
    return render_template("public/index_simple.html")


@app.route("/")
def index():
    config.display()
    return render_template("public/index.html")
    #return render_template("public/index.html", config=config.current)


@app.route("/about")
def about():
    return "All about terminator"



