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
            return redirect(url_for("search"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")
    
@app.route("/search", methods=["GET", "POST"])
def search():
    if "user" not in session:
        return redirect(url_for("login"))

    if request.method == "POST":
        # 仮の検索結果
        hotels = [
            "Hotel Tokyo Central",
            "Tokyo Business Hotel",
            "Luxury Stay Tokyo"
        ]
        session["hotels"] = hotels
        return redirect(url_for("search_results"))

    return render_template("search.html")

@app.route("/search-results")
def search_results():
    if "user" not in session:
        return redirect(url_for("login"))

    hotels = session.get("hotels", [])
    return render_template("search_results.html", hotels=hotels)

@app.route("/select", methods=["POST"])
def select():
    if "user" not in session:
        return redirect(url_for("login"))

    selected_hotel = request.form["hotel"]
    session["selected_hotel"] = selected_hotel
    return redirect(url_for("dashboard"))

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    
    hotel = session.get("selected_hotel")
    return render_template("dashboard.html", user=session["user"], hotel=hotel)

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)