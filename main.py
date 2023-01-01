from tkinter import *
import math

BACKGROUND_COLOUR = "#FFF6C3"
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


def reset():
    window.after_cancel(timer)
    canvas.itemconfig(time_remaining, text="00:00")
    canvas.itemconfig(title_label, text="Timer", fill=GREEN)
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(20 * 60)
        canvas.itemconfig(title_label, text="Long Break", fill=GREEN)
    elif reps % 2 == 1:
        count_down(25 * 60)
        canvas.itemconfig(title_label, text="Work", fill=RED)
    else:
        count_down(5 * 60)
        canvas.itemconfig(title_label, text="Short Break", fill=GREEN)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(time_remaining, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


window = Tk()
window.title("Work Timer")
window.config(padx=100, pady=50, bg=BACKGROUND_COLOUR)

canvas = Canvas(width=300, height=350, bg=BACKGROUND_COLOUR, highlightthickness=0)
sycamore_gap_pic = PhotoImage(file="sycamore_gap.png")
canvas.create_image(150, 155, image=sycamore_gap_pic)
time_remaining = canvas.create_text(150, 150, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.pack()
title_label = canvas.create_text(150, 15, text="Timer", fill=GREEN, font=(FONT_NAME, 35, "bold"))
check_tracker = canvas.create_text(150, 320, text=" ")

reset_button = Button(text="Reset", command=reset)
reset_button.place(x=55, y=275)

start_button = Button(text="Start", command=start_timer)
start_button.place(x=200, y=275)

window.mainloop()
