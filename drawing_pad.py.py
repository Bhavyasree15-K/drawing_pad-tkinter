import tkinter as tk
from tkinter import colorchooser
from tkinter import Scale
from tkinter import*
root = tk.Tk()
root.configure(bg="#1E1E1E")
root.title("Drawing Pad")
root.geometry("800x600")
current_color="black"
old_x = None
old_y = None
def reset(event):
    global old_x,old_y
    old_x = None
    old_y = None   
def choose_color():
    global current_color
    color = colorchooser.askcolor()[1]
    if color:
        current_color = color
tool = "pen"
def sel_pen():
    global tool
    tool = "pen"
    status.config(text="Tool : Pen")
def sel_rect():
    global tool
    tool = "rectangle"
    status.config(text="Tool : Rectangle")
def sel_circle():
    global tool
    tool = "circle"
    status.config(text="Tool : Circle")
start_x = 0
start_y = 0
def start_shape(event):
    global start_x,start_y
    start_x = event.x
    start_y = event.y
def end_shape(event):
    if tool == "rectangle":
        canvas.create_rectangle(start_x,start_y,event.x,event.y,outline=current_color,width=brush_size)
    elif tool == "circle":
        canvas.create_oval(start_x,start_y,event.x,event.y,outline=current_color,width=brush_size)
brush_size = 5
def set_brush_size(value):
    global brush_size
    brush_size = int(value)
def eraser():
    global tool,current_color
    current_color = "white"
    status.config(text="Tool : Eraser")
    if tool not in ["pen", "eraser"]:
        return
eraser_size = 20
def set_eraser_size(value):
    global eraser_size
    eraser_size = int(value)
def erase_with_size(event):
    global old_x, old_y
    if tool!="pen":
        return
    if old_x is not None and old_y is not None:
            width = eraser_size if current_color == "white" else brush_size
            canvas.create_line(old_x,old_y,event.x,event.y,fill=current_color,width=width,capstyle=ROUND,smooth=True)
    old_x = event.x
    old_y = event.y
def clear_canvas():
    canvas.delete("all")
def release(event):
    if tool in ["rectangle","circle"]:
        
        end_shape(event)
    reset(event)
frame = Frame(root,bg = "sky blue")
frame.pack(fill=X)
frame.configure(bg = "white")
status = Label(root,text="Tool : Pen",bd=1,relief=SUNKEN,anchor=W,font=("Arial",10,"bold"))
status.pack(side=BOTTOM,fill=X)
Button(frame,text="Choose color",command=choose_color,bg="#444444",fg="white").pack(side=LEFT,padx=5,pady=5)
size_changer = Scale(frame,from_ = 1, to = 30,orient = HORIZONTAL,label = "Set your brush size",command = set_brush_size,length=120,bg="light pink")
size_changer.set(5)
size_changer.pack(padx=20,pady=20)
eraser_slider = Scale(frame,from_=20,to = 50,orient = HORIZONTAL,label = "Eraser sizer",command = lambda x:  set_eraser_size(x),width = 20,bg = "yellow")
eraser_slider.pack()
eraser_slider.set(20)
Button(frame,text="Eraser",command = eraser,bg="#4CAF50",fg="white",font=("Arial",10,"bold")).pack(side=LEFT,padx=5,pady=5)
Button(frame,text = "select pen",command=sel_pen,bg="#4CAF50",fg="white",font=("Arial",10,"bold")).pack(side=LEFT,padx=5,pady=5)
Button(frame,text="select rectangle",command=sel_rect,bg="#4CAF50",fg="white",font=("Arial",10,"bold")).pack(side=LEFT,padx=5,pady=5)
Button(frame,text="select circle",command=sel_circle,bg="#4CAF50",fg="white",font=("Arial",10,"bold")).pack(side=LEFT,padx=5,pady=5)
Button(frame,text="Clear",command=clear_canvas,bg="#4CAF50",fg="white",font=("Arial",10,"bold")).pack(side=LEFT,padx=5,pady=5)
Button(frame,text="Exit",command=root.destroy,bg="#4CAF50",fg="white",font=("Arial",10,"bold")).pack(side=LEFT,padx=5)
canvas = Canvas(root,width=600,height=400,bg="white")
canvas.pack(fill=BOTH,expand=True)
canvas.bind("<B1-Motion>",erase_with_size)
#canvas.bind("<ButtonRelease-1>",reset)
canvas.bind("<Button-1>",start_shape)
canvas.bind("<ButtonRelease-1>",release)
root.mainloop()
