from tkinter import *

# constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = 'Courier'
WORK = 25
SHORT_BREAK = 5
LONG_BREAK = 20


# countdown
def countdown(time):
    canvas.itemconfig(timer_text, text=time)
    window.after(1000, countdown, time - 1)

# UI
window = Tk()
window.title('PyPomodoro')
window.config(padx=100, pady=50, bg=YELLOW)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canvas.create_image(102, 112, image=img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT, 35, 'bold'))
canvas.grid(row=2, column=2)

countdown(5)

button_start = Button(text='Start', bg='white', highlightthickness=0).grid(row=3, column=0, pady=10)
button_reset = Button(text='Reset', bg='white', highlightthickness=0).grid(row=3, column=3, pady=10)
checkmarks = Label(text='✓', fg=GREEN, bg=YELLOW, font=(FONT, 18, 'bold')).grid(row=3, column=2, pady=10)

window.mainloop()