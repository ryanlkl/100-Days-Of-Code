from flask import Flask, render_template
import requests

app = Flask(__name__)
url = "https://api.npoint.io/76037bcbac27fbe13bda"

response = requests.get(url)
data = response.json()

@app.route("/")
def home():
  return render_template("index.html",posts=data)

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/contact")
def contact():
  return render_template("contact.html")

@app.route('/post/<num>')
def post(num):
  for post in data:
    if post["id"] == int(num):
      return render_template("post.html",post=post)


if __name__ == "__main__":
  app.run(debug=True)
