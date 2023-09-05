from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route("/")
def home():
  year = datetime.now().year
  print(year)
  random_number = random.randint(1,10)
  return render_template("index.html", random=random_number,current_year=str(year))

@app.route("/guess/<string:name>")
def guess(name):
  agify_response = requests.get(f"https://api.agify.io?name={name.title()}")
  agify_data = agify_response.json()
  age = agify_data["age"]
  genderize_response = requests.get(f"https://api.genderize.io?name={name.title()}")
  genderize_data = genderize_response.json()
  gender = genderize_data["gender"]
  return render_template("guess.html",age=age,gender=gender,name=name.title())

@app.route("/blog")
def blog():
  blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
  response = requests.get(blog_url)
  all_posts = response.json()
  return render_template("blog.html",posts=all_posts)

if __name__ == "__main__":
  app.run(debug=True)
