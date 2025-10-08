import turtle
import pandas

screen = turtle.Screen()
screen.title("US state game")
image = "blank_states_img.gif"
screen.addshape(image)# Add the image to the turtle shapes
turtle.shape(image)

data = pandas.read_csv("states.csv")
all_states = data.state.to_list()

guessed_state = []
while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)} / 50 states" , prompt="whats another state name")
    if answer_state is None:  # Handle if user cancels the dialog
        break
    
    # Make comparison case-insensitive by converting to title case
    answer_state = answer_state.title()
    
    if answer_state in all_states and answer_state not in guessed_state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()
