import turtle
import pandas

screen = turtle.Screen()
screen.setup(width= 750, height=500)
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pandas.read_csv('50_states.csv')
state_list =  states['state'].to_list()
correct_guesses = 0
correct_guesses_list = []


while correct_guesses < 51:
    answer = screen.textinput(prompt='Guess All The States', title=f'{correct_guesses}/50').title()

    if answer == 'Exit':
        break
    if answer in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = states[states.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)
        correct_guesses += 1
        state_list.remove(answer)
        

state_list = pandas.Series(state_list)
state_list.to_csv('states_to_learn.csv')

