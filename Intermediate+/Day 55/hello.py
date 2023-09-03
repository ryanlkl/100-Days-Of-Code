from flask import Flask

app = Flask(__name__)

def make_bold(function):

  def inside():
    return f"<b>{function}</b>"

  return inside

def make_emphasis(function):

  def inside():
    return f"<em>{function}</em>"

  return inside

def make_underline(function):

  def inside():
    return f"<u>{function}</u>"

  return inside

@app.route("/")
def hello_world():
  return "<h1>Hello, World!</h1>" \
  '<p>Lorem ipsum</p>' \
  '<button>Submit</button>'

@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
  return "<h1>Bye</h1>!"

@app.route("/greet/<string:name>")
def greet(name):
  return f"<h1>Hello, {name}!</h1>"

if __name__ == "__main__":
  app.run(debug=True)
