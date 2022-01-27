from flask import Flask, render_template
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


@app.route("/about.html")
def about():
    return render_template("about.html")


@app.route("/contact.html")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
