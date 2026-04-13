from flask import Flask, render_template, request, redirect, session
from pymongo import MongoClient

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = "secret123"

# MongoDB connection (replace with your Atlas URI)
client = MongoClient("mongodb://admin:123@localhost:27017/?authSource=admin") 
db = client["userdb"]
users = db["users"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "email": request.form["email"],
            "password": request.form["password"]
        }
        users.insert_one(data)
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = users.find_one({
            "email": request.form["email"],
            "password": request.form["password"]
        })
        if user:
            session["user"] = user["email"]
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        all_users = list(users.find())
        return render_template("dashboard.html", users=all_users)
    return redirect("/login")

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
