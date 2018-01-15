
import tkinter
import random

window = tkinter.Tk()
window.minsize(550,550)
label = tkinter.Label(window, fg = 'Red', text="Score: 0")
label.place(x=0, y=0)
counter = 0


seconds=5
label2 = tkinter.Label(window, fg = 'Yellow', text="Timer: %s" % seconds)
label2.place(x=0, y=20)

button = tkinter.Button(window, bg = 'Green', fg = 'Blue', text="Start")
button.place(x=100, y=100)

def onClick():
    
    global counter
    global label
    global button
    if button["text"] == "Start":
        button.after(100, onTimer)
        button["text"] = "Click"
    counter += 1
    label["text"] = "Score: %s" % counter
    button.place(x=random.randint(0, 300), y=random.randint(0, 300))
button.configure(command = onClick)

def onTimer():
    global counter
    global label2
    global button
    global seconds
    seconds -= 1
    label2["text"] = "Timer: %s" % seconds
    if seconds <= 0:
        button.config(state='disabled')
        tkinter.messagebox.showinfo("END OF THE GAME", "Score: %s" % counter)
    else:
        button.after(1000, onTimer)

window.mainloop()