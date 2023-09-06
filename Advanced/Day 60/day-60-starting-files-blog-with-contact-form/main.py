from flask import Flask, render_template, request
import requests
import smtplib
from decouple import config

# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")

def send_email(name,email,phone,message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone number: {phone}\nMessage:\n{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
     connection.starttls()
     connection.login(EMAIL,PASSWORD)
     connection.sendmail(from_addr=EMAIL,
                         to_addrs="EMAIL",
                         msg=f"Subject:New Message\n\n{email_message}".encode("utf-8"))

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",methods=["POST","GET"])
def contact():
    if request.method == "POST":
        info = request.form
        send_email(name=info["name"], email=info["email"], phone=info["phone"], message=info["message"])
        return render_template("contact.html",message="Successfully sent message")

    return render_template("contact.html",message="Contact Me")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)




if __name__ == "__main__":
    app.run(debug=True, port=5001)
