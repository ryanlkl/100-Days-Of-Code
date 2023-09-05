from flask import Flask, render_template
import requests


app = Flask(__name__)

url = "https://api.npoint.io/c790b4d5cab58020d391"
response = requests.get(url)
data = response.json()

@app.route('/')
def home():
    return render_template("index.html",posts=data)

@app.route('/post/<num>')
def post(num):
    for post in data:
        if post["id"] == int(num):
            return render_template("post.html",post=post)

if __name__ == "__main__":
    app.run(debug=True)
