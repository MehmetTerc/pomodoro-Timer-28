import math
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
reps = 0
timer = None

# w

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    check.config(text="")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    pom_timer.config(text="TIMER")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    if reps % 2 == 0:
        if reps % 8 == 0:
            pom_timer.config(text="BREAK", fg=RED)
            count_down(LONG_BREAK_MIN * 60)
        else:
            count_down(SHORT_BREAK_MIN * 60)
            pom_timer.config(text="BREAK", fg=PINK)
    elif reps % 2 == 1:
        count_down(WORK_MIN * 60)
        pom_timer.config(text="WORK", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark =""
        for n in range(math.floor(reps/2)):
            mark +="✅"
        check.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=25, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

pom_timer = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40), bg=YELLOW)
pom_timer.grid(column=1, row=0)

check = Label(text="", bg=YELLOW, fg=GREEN)
check.grid(column=1, row=3)

startBtn = Button(text="Start", command=start_timer)
startBtn.grid(column=0, row=2)

resetBtn = Button(text="Reset", command=reset_timer)
resetBtn.grid(column=2, row=2)

window.mainloop()
