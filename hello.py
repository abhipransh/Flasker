from flask import Flask, render_template

#create a flask instance
app = Flask(__name__)

#create a route decorator
@app.route('/')

# FILTERS
# safe
# capitalize
# lower
# upper
# title
# trim
# striptags

def index():
    first_name = "John"
    stuff = "This is bold text"
    favourite_pizza = ["Pepproni", "Cheese", "Mushroom", 41]
    return render_template("index.html", first_name=first_name, stuff=stuff, favourite_pizza=favourite_pizza)

@app.route('/user/<name>')

def user(name):
    return render_template("user.html", user_name = name)

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"),500