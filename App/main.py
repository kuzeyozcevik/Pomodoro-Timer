import tkinter
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
work_sec = WORK_MIN*60
short_break_sec = SHORT_BREAK_MIN*60
long_break_sec = LONG_BREAK_MIN*60

timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="Timer")
    tick.config(text="")
    global rep
    rep = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global rep
    rep += 1
    work = [1,3,5,7]
    short_break = [2,4,6]
    long_break = [8]
    if rep in work:
        count_down(work_sec)
        label.config(text="Work",fg="green",width=7)
    elif rep in short_break:
        label.config(text="Short Break",fg="pink",width=7)
        count_down(short_break_sec)
    elif rep in long_break:
        label.config(text="Long Break :)",fg="red",width=7)
        count_down(long_break_sec)
    if rep == 8:
        rep = 0
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer

    count = int(count)

    result = ""
    count_min = count // 60
    count_sec = count % 60

    result += f"{int(count_min)}:{count_sec:02d}"

    canvas.itemconfig(timer_text, text=result)
    if count > 0:
        timer = windows.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_session = rep//2
        for n in range(work_session):
            mark += "✓"
        tick.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #

windows = tkinter.Tk()
windows.title("Pomodoro")
windows.config(padx=100,pady=50,bg=YELLOW)




canvas = tkinter.Canvas()
canvas.config(width=200,height=224,bg=YELLOW,highlightthickness=False)
image = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"normal"))
canvas.grid(row=1,column=1)


label = tkinter.Label(text="Timer",font=(FONT_NAME,40,"normal"),fg="green",bg=YELLOW)
label.grid(row=0,column=1)

start_button = tkinter.Button(text="start",width=3,highlightthickness=0,bg=YELLOW,command=start_timer)
start_button.grid(row=2,column=0)

reset_button = tkinter.Button(text="reset",width=3,highlightthickness=0,bg=YELLOW,command=reset_timer)
reset_button.grid(row=2,column=2)

tick = tkinter.Label(  fg="green",bg=YELLOW)
tick.grid(row=3,column=1)

windows.mainloop()