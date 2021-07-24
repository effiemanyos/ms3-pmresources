import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_resources")
def get_resources():
    resources = list(mongo.db.resources.find())
    return render_template("resources.html", resources=resources)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successfull")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                    session["user"] = request.form.get("username").lower()
                    flash("Welcome, {}".format(
                        request.form.get("username")))
                    return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:        
        return render_template("profile.html", username=username)
    
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_resource", methods=["GET", "POST"])
def add_resource():
    if request.method == "POST":
        is_done = "on" if request.form.get("is_done") else "off"
        resource = {
            "resource_title": request.form.get("resource_title"),
            "resource_author": request.form.get("resource_author"),
            "creation_date": request.form.get("creation_date"),
            "is_done": is_done,
            "category_name": request.form.get("category_name"),
            "source_name": request.form.get("source_name"),
            "resource_topic": request.form.get("resource_topic"),
            "resource_type": request.form.get("resource_type"),
            "resource_rating": request.form.get("resource_rating"),
            "resource_url": request.form.get("resource_url"),
            "resource_takeaway": request.form.get("resource_takeaway"),
            "created_by": session["user"]
        }
        mongo.db.resources.insert_one(resource)
        flash("Resource Successfully Added")
        return redirect(url_for("get_resources"))

    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_resource.html", categories=categories)


@app.route("/edit_resource/<resource_id>", methods=["GET", "POST"])
def edit_resource(resource_id):
    if request.method == "POST":
        is_done = "on" if request.form.get("is_done") else "off"
        submit = {
            "resource_title": request.form.get("resource_title"),
            "resource_author": request.form.get("resource_author"),
            "creation_date": request.form.get("creation_date"),
            "is_done": is_done,
            "category_name": request.form.get("category_name"),
            "source_name": request.form.get("source_name"),
            "resource_topic": request.form.get("resource_topic"),
            "resource_type": request.form.get("resource_type"),
            "resource_rating": request.form.get("resource_rating"),
            "resource_url": request.form.get("resource_url"),
            "resource_takeaway": request.form.get("resource_takeaway"),
            "created_by": session["user"]
        }
        mongo.db.resources.update({"_id": ObjectId(resource_id)}, submit)
        flash("Resource Successfully Updated")
        return redirect(url_for("get_resources"))

    resource = mongo.db.resources.find_one({"_id": ObjectId(resource_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_resource.html", resource=resource, categories=categories)


@app.route("/delete_resource/<resource_id>")
def delete_resource(resource_id):
    mongo.db.resources.remove({"_id": ObjectId(resource_id)})
    flash("Resouce Successfully Deleted")
    return redirect(url_for("get_resources"))


@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("category_name", 1))
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "category_name": request.form.get("category_name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True) # During development, we want to see the actual 
                        # errors that may appear, instead of a generic server warning
                        # Update to debug=False prior to actual deployment or project submission!
