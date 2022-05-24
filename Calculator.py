from tkinter import *



def click(event):
    global scvalue
    text = event.widget.cget('text')

    if text=='=':
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(entry.get())
            except Exception as e:
                value = "Error"


        scvalue.set(value)
        entry.update()


    elif text=='C':
        scvalue.set("")
        entry.update()

    else:
        scvalue.set(scvalue.get() + text)
        entry.update()


root = Tk()
root.geometry("390x482")
root.configure(background="powder blue")
root.wm_iconbitmap("C:/Users/Roman/Desktop/calculator.ico")
root.title("Calculator")

scvalue = StringVar()
scvalue.set("")

entry = Entry(root,textvariable=scvalue, font=("Calibri",30),justify="right",width=6,bg="#1E6FBA",fg="black",
                     disabledbackground="#1E6FBA",disabledforeground="yellow",highlightbackground="black",highlightcolor="red",highlightthickness=1,bd=15)
entry.place(x=2, y=10, width=387, height=80)


f=Frame(root, bg="grey")
b = Button(f, text="C", font="lucida 15 bold", padx=177)
b.pack(side="left")
b.bind('<Button-1>', click)
f.place(x=4, y=100)

f=Frame(root, bg="grey")
b= Button(f, text="9", font="lucida 15 bold", padx=35, pady=10)
b.pack(side="left")
b.bind('<Button-1>', click)

b= Button(f, text="8", font="lucida 15 bold", padx=35, pady=10)
b.pack(side="left")
b.bind('<Button-1>', click)


b= Button(f, text="7", font="lucida 15 bold", padx=35, pady=10)
b.pack(side="left")
b.bind('<Button-1>', click)

b= Button(f, text="/", font="lucida 15 bold", padx=35, pady=10)
b.pack(side="left")
b.bind('<Button-1>', click)
f.place(x=4, y=150)

f=Frame(root, bg="grey")
b= Button(f, text="4", font="lucida 15 bold", padx=35, pady=10)
b.pack(side="left")
b.bind('<Button-1>', click)

b= Button(f, text="5", font="lucida 15 bold", padx=35, pady=10)
b.pack(side="left")
b.bind('<Button-1>', click)


b= Button(f, text="6", font="lucida 15 bold", padx=35, pady=10)
b.pack(side="left")
b.bind('<Button-1>', click)

b= Button(f, text="*", font="lucida 15 bold", padx=33, pady=10)
b.pack(side="left")
b.bind('<Button-1>', click)
f.place(x=4, y=210)


f=Frame(root, bg="grey")
b= Button(f, text="1", font="lucida 15 bold", padx=35, pady=10)
b.pack(side="left")
b.bind('<Button-1>', click)

b= Button(f, text="2", font="lucida 15 bold", padx=35, pady=10)
b.pack(side="left")
b.bind('<Button-1>', click)


b= Button(f, text="3", font="lucida 15 bold", padx=35, pady=10)
b.pack(side="left")
b.bind('<Button-1>', click)

b= Button(f, text="-", font="lucida 15 bold", padx=35, pady=10)
b.pack(side="left")
b.bind('<Button-1>', click)
f.place(x=4, y=270)


f=Frame(root, bg="grey")
b= Button(f, text=".", font="lucida 15 bold", padx=51, pady=5)
b.pack(side="left")
b.bind('<Button-1>', click)

b= Button(f, text="0", font="lucida 15 bold", padx=51, pady=5)
b.pack(side="left")
b.bind('<Button-1>', click)


b= Button(f, text="+", font="lucida 15 bold", padx=52, pady=5)
b.pack(side="left")
b.bind('<Button-1>', click)
f.place(x=4, y=330)


f=Frame(root, bg="grey")
b= Button(f, text="%", font="lucida 15 bold", padx=49, pady=5)
b.pack(side="left")
b.bind('<Button-1>', click)

b= Button(f, text="^", font="lucida 15 bold", padx=49, pady=5)
b.pack(side="left")
b.bind('<Button-1>', click)


b= Button(f, text="00", font="lucida 15 bold", padx=45, pady=5)
b.pack(side="left")
b.bind('<Button-1>', click)
f.place(x=4, y=380)

f=Frame(root, bg="grey")
b= Button(f, text="=", font="lucida 15 bold", padx=178, pady=5)
b.pack(side="left")
b.bind('<Button-1>', click)
f.place(x=4, y=430)
root.mainloop()



