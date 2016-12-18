from flask import Flask, render_template, flash, request, url_for, redirect
from cms import content

topic_dict = content()

app = Flask(__name__)
app.secret_key = 'some_secret'

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/slashboard/')
@app.route('/dashboard/')
def dashboard():
    flash("test")
    return render_template("dashboard.html", t_dict = topic_dict)


@app.route('/login/', methods = ["GET","POST"])
def login_page():
    error = ''
    try:
        if request.method == "POST":
            a_username = request.form["username"]
            a_password = request.form["password"]
            # flash(a_username)
            # flash(a_password)
            if a_username == "admin" and a_password == "123":
                return redirect(url_for("dashboard"))
            else:
                error = "Invalid Login"
        return render_template("login.html", error = error)
    except Exception as e:
        flash(e)
        return render_template("login.html", error=error)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html",error = e)



# @app.route('/shboard/')
# def shboard():
#     try:
#         return render_template("dashboard.html", t_dict = topic_dic)
#     except Exception as e:
#         return(str(e))


if __name__ == "__main__":
    app.debug = True
    app.run(debug = True)
    app.run()
