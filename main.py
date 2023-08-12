from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✓"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, timer
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="")
    checkmark_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count = 20 * 60  # Long Break
        title_label.config(text="Break", fg=GREEN)
        checkmark_label.config(text=f"{checkmark_label.cget('text') + CHECKMARK}")
    elif reps % 2 == 0:
        count = 5 * 60  # Short Break
        title_label.config(text="Break", fg=GREEN)
    else:
        count = 25 * 60  # Work
        title_label.config(text="Work", fg=RED)

    countdown(count)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = int(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=0, column=1)

tomato = PhotoImage(file="tomato.png")
canvas = Canvas(
    width=210,
    height=224,
    bg=YELLOW,
    highlightthickness=0)
canvas.create_image(105,
                    112,
                    image=tomato)
timer_text = canvas.create_text(105,
                                130,
                                text="00:00",
                                fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

start_button = Button(
    text="Start",
    bg="white",
    highlightthickness=0,
    borderwidth=0,
    width=7,
    background=PINK,
    command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(
    text="Reset",
    bg="white",
    highlightthickness=0,
    borderwidth=0,
    width=7,
    background=PINK,
    command=reset_timer)
reset_button.grid(row=2, column=3)

checkmark_label = Label(font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
checkmark_label.grid(row=3, column=1)

window.mainloop()
