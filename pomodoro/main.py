from tkinter import *
import math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25 
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20 
reps = 0
timer = None

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        countdown(10)
        timer_label.config(text='Break', fg=RED)
    elif reps % 2 == 0:
        countdown(10)
        timer_label.config(text='Break', fg=RED)

    else:
        countdown(10)
        timer_label.config(text='Work', fg=GREEN)
    
def countdown(count):
    global timer
    count_min = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_seconds}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        checkmarks = ""
        for rep in range(math.floor(reps/2)):
           checkmarks += "✔"
        checkmark_label.config(text=checkmarks)

def reset():
    window.after_cancel(timer)
    checkmark_label.config(text="")
    timer_label = Label(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady= 50, bg=(YELLOW))

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness= 0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato)

timer_text = canvas.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 42, "bold"), bg=YELLOW,
                    highlightthickness=0, fg=GREEN)
timer_label.grid(row=0, column=1)

checkmark_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, "bold"))
checkmark_label.grid(row=3, column=1)

start_button = Button(text='Start', command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text='Reset', command=reset)
reset_button.grid(row=2,column=2)

window.mainloop()