from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length, Email
from flask_bootstrap import Bootstrap5

'''
Red underlines? Install the required packages first:
Open the Terminal in PyCharm (bottom left).

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''


app = Flask(__name__)
bootstrap = Bootstrap5(app)
app.secret_key = "secret-key"

class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[Email(), InputRequired(), DataRequired()])
    password = PasswordField(label="Password", validators=[Length(min=8, message="Password needs to be atleast 8 characters"), InputRequired(), DataRequired()])
    submit =  SubmitField(label="log in")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login",methods=["GET","POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        form_email = login_form.email.data
        form_password = login_form.password.data
        if form_email == "admin@email.com" and form_password == "12345678":
            return render_template("success.html")
        return render_template("denied.html")
    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
