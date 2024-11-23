import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "100Days-Python/US-State/Guess/blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title="GUESS THE STATE", prompt="What's another state")



