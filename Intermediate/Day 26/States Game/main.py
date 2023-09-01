import pandas
import turtle

# Initiatescreen
screen = turtle.Screen()
screen.title("U.S States Game")

# Set U.S map bg
image = "Day 25\\States Game\\blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
guessed_states = []


data = pandas.read_csv("Day 25\\States Game\\50_states.csv")
all_states = data.state.to_list()
while len(guessed_states) < 50:
  answer_state = screen.textinput(title=f"({len(guessed_states)}/50) Guess the state: ", prompt="State name").title()
  if answer_state == "Exit":
    missing_states = [state for state in all_states if state not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("Day 25\\States Game\\states_to_learn.csv")
    break
  if answer_state in all_states:
      guessed_states.append(answer_state)
      t = turtle.Turtle()
      t.hideturtle()
      t.penup()
      state_data = data[data.state == answer_state]
      t.goto(int(state_data.x),int(state_data.y))
      t.write(answer_state)



print(missing_states)
