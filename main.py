from tkinter import *
import math

# constants and globals
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = 'Courier'
WORK = 25 * 60
SHORT_BREAK = 5 * 60
LONG_BREAK = 20 * 60
reps = 0
timer = None

# reset all f the gui elements and cancel the timer
def reset():
    global reps
    canvas.itemconfig(timer_text, text='00:00')
    checkmarks.config(text='')
    title.config(text='Pomodoro')
    window.after_cancel(timer)
    reps = 0

def start_timer():
    global reps
    # every time the start_timer function is called increae reps by 1
    reps += 1

    # if there have been 8 reps(4 work breaks) then user gets a long break
    if reps % 8 == 0:
        countdown(LONG_BREAK)
        title.config(text='Long Break', fg=RED)
    # if reps is an even number then user gets a short break
    elif reps % 2 == 0:
        countdown(SHORT_BREAK)
        title.config(text='Short Break', fg=PINK)
    # else user is working
    else:
        countdown(WORK)
        title.config(text='Work', fg=GREEN)

def countdown(time):
    global reps 
    global timer

    # set the time in mins and secs for easier display 
    time_min = math.floor(time / 60)
    time_sec = time % 60

    # if statement to make sure the time always displays a 0 in front of the current secs/mins when below 10
    if time_sec < 10:
        time_sec = f'0{time_sec}'
    if time_min < 10:
        time_min = f'0{time_min}'

    # set the canvas item timer_test to be equal to the time in mins and secs, formatted properly
    canvas.itemconfig(timer_text, text=f'{time_min}:{time_sec}')

    # ensure time doesn't go below 0
    if time > 0:
        timer = window.after(1000, countdown, time - 1)
    # if time goes below zero, call start_timer function and begin the next round
    else:
        start_timer()
        # variable for holding checkmarks displayed on screen
        marks = ""
        # every 2 reps means 1 work session done, so add a checkmark to checks and update the display
        for i in range(0, math.floor(reps / 2)):
            marks += '✓'
            checkmarks.config(text=marks)

# create the gui window
window = Tk()
window.title('PyPomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

# create a canvas for displaying the pomodoro image and the timer text and set it in the window grid
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=img)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT, 35, 'bold'))
canvas.grid(row=1, column=2, padx=10)

# create the button and label elements to display in the window and set them on the grid
title = Label(text='Pomodoro', fg=GREEN, bg=YELLOW, font=(FONT, 20, 'bold'))
title.grid(row=0, column=2, pady=10, padx=10)
button_start = Button(text='Start', bg='white', highlightthickness=0, command=start_timer).grid(row=2, column=0, pady=10, padx=10)
button_reset = Button(text='Reset', bg='white', highlightthickness=0, command=reset).grid(row=2, column=3, pady=10)
checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT, 18, 'bold'))
checkmarks.grid(row=2, column=2, pady=10, padx=10)

window.mainloop()