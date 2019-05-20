# from tkinter import *
import tkinter
import math
import sys

def calc_area(*args):
    area_result = (float(radius.get())**2)*math.pi
    area.set(round(area_result,2))
    os_name.set(sys.platform)


#root_win=Tk()
root_win=tkinter.Tk()
root_win.geometry("200x100")
root_win.title("Area Calculator")


radius = tkinter.StringVar()
radius.set("0")
area = tkinter.StringVar()
os_name = tkinter.StringVar()

area_label = tkinter.Label(root_win, text="Area:").grid(column =1,row=1)
area_value= tkinter.Label(root_win, textvariable = area).grid(column =2, row=1)

radius_label = tkinter.Label(root_win, text="Radius:").grid(column=1, row = 2)
radius_entry= tkinter.Entry(root_win,width =7,textvariable =radius).grid(column=2, row=2)

calc_button = tkinter.Button(root_win,text="Calc",command =calc_area).grid(column =2, row=3)

OS_Lable= tkinter.Label(root_win,textvariable=os_name).grid(column=1, row=4)

# my_label = tkinter.Label(root_win, text="Usmans GUI app")
# my_label.pack()

root_win.mainloop()