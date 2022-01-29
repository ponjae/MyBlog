from email.mime import message
from black import re
from flask import Flask, render_template, request
from post import Post
import requests

app = Flask(__name__)


def _generate_posts():
    response = requests.get(
        "https://api.npoint.io/a09d1034f2e7bbe70b6e")
    data = response.json()
    posts = []
    for post in data:
        posts.append(Post(post["id"], post["title"],
                     post["subtitle"], post["body"],
                     post["author"], post["date"]))
    return posts


posts = _generate_posts()


@app.route("/")
def home():
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    elif request.method == "POST":
        name = request.form["name"]
        return f"<h1>Successfully sent message, well done {name}</h1>"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = None
    for post in posts:
        if post.id == post_id:
            requested_post = post
            break
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
