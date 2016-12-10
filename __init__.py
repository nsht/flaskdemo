from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("main.html")

@app.route('/slashboard/')
@app.route('/dashboard/')
def dashboard():
    #return("Hello dashboard")
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run()