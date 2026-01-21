from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# 仮ユーザー
USERS = {
    "testuser": "password123"
}

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if USERS.get(username) == password:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")
    
@app.route("/search", methods=["GET", "POST"])
def search():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        location = request.form["location"]
        checkin = request.form["checkin"]
        checkout = request.form["checkout"]
        guests = request.form["guests"]

        return redirect(url_for("dashboard"))

    return render_template("search.html")


@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", user=session["user"])

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)