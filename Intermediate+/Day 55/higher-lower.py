from flask import Flask
import random

app = Flask(__name__)

number = random.randint(0,9)

@app.route("/")
def higher_lower():
  return "<h1 style='middle-align'>Higher or Lower</h1>" \
  "<h2>Guess a number between 0 and 9<h2>"

@app.route("/<int:num>")
def guessed(num):
  if num == number:
    return "<h1>Correct</h1>"
  elif num > number:
    return "<h1>Too Big</h1>"
  else:
    return "<h1>Too small</h1>"

if __name__ == "__main__":
  app.run(debug=True)
