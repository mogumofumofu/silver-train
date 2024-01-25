from tkinter import *
from tkinter import messagebox as mb
import math
import time
import json
import sys
import logging
import atexit
import ast
flags_debug = False
flags_logging = False


def closing():
    print(f"[DEBUG] END OF LOG")
atexit.register(closing)

def read_log():
    with open("log.log", "r") as f:
        data = f.read()
        return data

class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        # this flush method is needed for python 3 compatibility.
        # this handles the flush command by doing nothing.
        # you might want to specify some extra behavior here.
        pass

if flags_logging == True:
    sys.stdout = Logger("log.log")



print(f"[DEBUG] BEGINING OF LOG")
data = {"debug_flag": False}

def read_data():
    with open("data.json", "r") as f:
        data = json.load(f)
        if flags_debug == True:
            print(f"[DEBUG] Read json data file: {data}")
        return data
def write_data(data):
    with open("data.json", "w") as f:
        json.dump(data,f)
        if flags_debug == True:
            print(f"[DEBUG] Wrote json data to file, data: {data}")
data = read_data()

flags_debug = data["debug_flag"]
flags_logging = data["logging_flag"]





#package = 'tkinter'
#try:
#    __import__(package)
#except ImportError:
#    print("ERROR: tkinter not installed")
#    time.sleep(1)
#    exit()


master = Tk()


variable = StringVar(master)
variable.set("Area") # default value

var2 = StringVar(master)
var2.set("cm")

var3 = StringVar(master)
var3.set("Radie")

entry = Entry(master=master)
entry.grid(row=1,column=1)
entry.delete(0, END)
entry.insert(0, "")

def only_numbers(char):
    return char.isdigit() or char == "."
validate_command = master.register(only_numbers)

entry.config(textvariable="1",validate="key",validatecommand=(validate_command, '%S'))
lenght = OptionMenu(master, var2, "cm", "mm", "m")
lenght.grid(row=1,column=2)
type = OptionMenu(master, variable, "Area", "Omkrets", "Diameter", "Radie")
type.grid(row=1,column=3)



label = Label(master,text="Convert To: ")
label.grid(row=2,column=1)
convert_to = OptionMenu(master, var3, "Area", "Omkrets", "Diameter", "Radie")
convert_to.grid(row=2,column=2)

def ok():
    value = entry.get()
    lenght_type = var2.get()
    cirkel_type = variable.get()
    convert_type = var3.get()
    if flags_debug == True:
        print(f"[DEBUG] {value}, {lenght_type}, {cirkel_type}, {convert_type}")
    if cirkel_type == "Area":
        area = float(value)
        radie = math.sqrt(area / math.pi)
        diameter = 2 * radie
        omkrets = 2 * math.pi * radie
        if flags_debug == True:
            print(f"[DEBUG] area: {area} radie: {radie} diameter: {diameter} omkrets: {omkrets}")
        
        if convert_type == "Area":
            print(area)
            mb.showinfo("",area)
            return area
        if convert_type == "Radie":
            print(radie)
            mb.showinfo("",radie)
            return radie
        if convert_type == "Diameter":
            print(diameter)
            mb.showinfo("",diameter)
            return diameter
        if convert_type == "Omkrets":
            print(omkrets)
            mb.showinfo("",omkrets)
            return omkrets
    elif cirkel_type == "Radie":
        radie = float(value)
        diameter = 2 * radie
        omkrets = 2 * math.pi * radie
        area = math.pi * radie**2
        if flags_debug == True:
            print(f"[DEBUG] area: {area} radie: {radie} diameter: {diameter} omkrets: {omkrets}")
        
        if convert_type == "Area":
            print(area)
            mb.showinfo("",area)
            return area
        if convert_type == "Radie":
            print(radie)
            mb.showinfo("",radie)
            return radie
        if convert_type == "Diameter":
            print(diameter)
            mb.showinfo("",diameter)
            return diameter
        if convert_type == "Omkrets":
            print(omkrets)
            mb.showinfo("",omkrets)
            return omkrets
    elif cirkel_type == "Omkrets":
        omkrets = float(value)
        radie = omkrets / (2 * math.pi)
        diameter = 2 * radie
        area = math.pi * radie**2
        if flags_debug == True:
            print(f"[DEBUG] area: {area} radie: {radie} diameter: {diameter} omkrets: {omkrets}")
        
        if convert_type == "Area":
            print(area)
            mb.showinfo("",area)
            return area
        if convert_type == "Radie":
            print(radie)
            mb.showinfo("",radie)
            return radie
        if convert_type == "Diameter":
            print(diameter)
            mb.showinfo("",diameter)
            return diameter
        if convert_type == "Omkrets":
            print(omkrets)
            mb.showinfo("",omkrets)
            return omkrets
    elif cirkel_type == "Diameter":
        diameter = float(value)
        radie = diameter / 2
        omkrets = 2 * math.pi * radie
        area = math.pi * radie**2
        if flags_debug == True:
            print(f"[DEBUG] area: {area} radie: {radie} diameter: {diameter} omkrets: {omkrets}")
        
        if convert_type == "Area":
            print(area)
            mb.showinfo("",area)
            return area
        if convert_type == "Radie":
            print(radie)
            mb.showinfo("",radie)
            return radie
        if convert_type == "Diameter":
            print(diameter)
            mb.showinfo("",diameter)
            return diameter
        if convert_type == "Omkrets":
            print(omkrets)
            mb.showinfo("",omkrets)
            return omkrets

button = Button(master,text="Calculate", command=ok)
button.grid(row=2,column=3)



if flags_debug == True:
    text_box = Text(master,width=30,height=10)
    text_box.grid(row=5,column=1)
    def show_log():
        data = str(read_log())
        mb.showinfo("[DEBUG] LOG",data)
    def show_data():
        data = read_data()
        text_box.delete(1.0, 'end')
        text_box.insert('end', data)
    def write_new_data():
        data_str = text_box.get(1.0,'end')
        data = ast.literal_eval(data_str)
        write_data(data)
    debug_section_label = Label(master,text="[DEBUG]")
    debug_section_label.grid(row=3,column=1)
    show_log_button = Button(master,text="SHOW LOG",command=show_log)
    show_log_button.grid(row=4,column=1)
    read_data_button = Button(master,text="READ DATA",command=show_data)
    read_data_button.grid(row=4,column=2)
    write_data_button = Button(master,text="WRITE DATA",command=write_new_data)
    write_data_button.grid(row=4,column=3)





mainloop()