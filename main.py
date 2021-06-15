from tkinter import *
import math

# constants
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

def reset():
    global reps
    canvas.itemconfig(timer_text, text='00:00')
    checkmarks.config(text='')
    title.config(text='Pomodoro')
    window.after_cancel(timer)
    reps = 0

def start_timer():
    global reps
    global session
    reps += 1

    if reps % 8 == 0:
        countdown(LONG_BREAK)
        title.config(text='Long Break', fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK)
        title.config(text='Short Break', fg=PINK)
    else:
        countdown(WORK)
        title.config(text='Work', fg=GREEN)

# countdown
def countdown(time):
    global reps 
    global timer

    time_min = math.floor(time / 60)
    time_sec = time % 60

    if time_sec < 10:
        time_sec = f'0{time_sec}'
    if time_min < 10:
        time_min = f'0{time_min}'

    canvas.itemconfig(timer_text, text=f'{time_min}:{time_sec}')

    if time > 0:
        timer = window.after(1000, countdown, time - 1)
    else:
        start_timer()
        marks = ""
        for i in range(0, math.floor(reps / 2)):
            marks += '✓'
            checkmarks.config(text=marks)

# UI
window = Tk()
window.title('PyPomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=img)
timer_text = canvas.create_text(103, 130, text='00:00', fill='white', font=(FONT, 35, 'bold'))
canvas.grid(row=1, column=2, padx=10)

title = Label(text='Pomodoro', fg=GREEN, bg=YELLOW, font=(FONT, 20, 'bold'))
title.grid(row=0, column=2, pady=10, padx=10)
button_start = Button(text='Start', bg='white', highlightthickness=0, command=start_timer).grid(row=2, column=0, pady=10, padx=10)
button_reset = Button(text='Reset', bg='white', highlightthickness=0, command=reset).grid(row=2, column=3, pady=10)
checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT, 18, 'bold'))
checkmarks.grid(row=2, column=2, pady=10, padx=10)

window.mainloop()