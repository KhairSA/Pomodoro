from tkinter import *
from PIL import ImageTk, Image
import time, math

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = True
check = ""

#function to start timer
def start_timer():
    global reps, timer, check
    reps += 1
    window.attributes("-topmost", 1)
    window.bell()
    window.attributes("-topmost", 0)
    if reps > 0:
        start_button.config(text="In Progress", state="disabled")
    print(reps)
    if reps == 8:
        reset_timer()
    elif reps == 7:
        count_down(LONG_BREAK_MIN*60)
        title_label.config(text="Break", fg= RED)
    elif reps % 2 != 0:
        count_down(WORK_MIN*60)
        title_label.config(text="Study Time", fg= GREEN)
    else:
        count_down(SHORT_BREAK_MIN*60)
        title_label.config(text="Short Break", fg= RED)


def reset_timer():
    global reps, timer, check
    window.after_cancel(timer)
    reps = 0
    check = ""
    title_label.config(text="Timer", fg= GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_mark.config(text=check)
    start_button.config(text="Start", state="normal")

# function to start countdown
def count_down(count):
    global check, timer, reps
    minutes = math.floor(count / 60)
    seconds = (count % 60)
    timer_string = f"{minutes}:{seconds:02d}"
    canvas.itemconfig(timer_text, text=timer_string)
    if count >= 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            check += "✓"
        check_mark.config(text=check)
        check = ""

#window code plus title
window = Tk()
window.title("Pomodoro")
window.config(padx= 75, pady= 75, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
title_label.grid(column=1, row=0)


#picture
canvas = Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomoto_img = ImageTk.PhotoImage(Image.open(r"red.jpg"))
canvas.create_image(150, 150, image= tomoto_img)
timer_text = canvas.create_text(150, 150, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

#start and reset button
start_button = Button(text="Start", command=start_timer, highlightthickness=0, font=(FONT_NAME, 12), bg="white")
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0, font=(FONT_NAME, 12), bg="white")
reset_button.grid(column=2, row=2)

#add checkmarks
check_mark = Label(text="", font=(FONT_NAME, 16, "bold"), bg=YELLOW, fg=GREEN)
check_mark.grid(column=1, row=3)








window.mainloop()
