import customtkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import csv

# Window settings
window = customtkinter.CTk()

window.geometry("1280x720")
window.configure(bg = "#a8a8a8")
window.title("Course Selector")

#Functions

filepath = None

def openFile(event=None):
    while True:
        try:
            global label1
            global filepath
            filepath = filedialog.askopenfilename(initialdir='*/Desktop',title='Choose your file',filetypes=[("Data Files","*.csv")])
            label1['text'] = filepath
            break
        except FileNotFoundError:
            messagebox.showinfo(title='Error',message="Please select a file.")
            break

def listbox_remove():
    x = listbox.curselection()
    y = listbox.size()
    z = []
    for i in range(0, y):
        if i in x:
            z.append(listbox.get(i))
    listbox.delete(0, END)
    for t in z:
        listbox.insert(END, t)
    listbox.select_set(0, len(x))

def remove_all():
    listbox.delete(0, END)

def display():
    try:
        mainscript()
    except:
        warning1.insert(END, "Please select a file")
    else:
        warning1.delete(0, END)


def save():
    x = listbox.curselection()
    y = listbox.size()
    z = []
    for i in range(0, y):
        if i in x:
            z.append((listbox.get(i)))
    x3 = []
    if len(x) > 6:
        warning1.delete(0, END)
        warning1.insert(END, "You can only pick 6 courses.")
    else:
        warning1.delete(0, END)
    for i in z:
        x1 = str(i)
        x2 = x1.split()
        x3.append(x2[-3:])
    counter = 0
    for i in x3:
        for j in x3:
            if j == i:
                counter += 1
    if counter > len(x):
        warning1.delete(0, END)
        warning1.insert(END, "Mismatching schedule.")
    if warning1.size() == 0:
        opened_file = filedialog.asksaveasfile(initialfile='timetable.csv')
        writer = csv.writer(opened_file)
        for i in z:
            writer.writerow(i)
        opened_file.close()

def mainscript():
    listbox_remove()
    x = filepath
    with open(x, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        read_csv = []
        for i in csv_reader:
            read_csv.append(i)
        read_csv = list(filter(lambda x: x, read_csv))
    for i in read_csv:
        asd = i[0].split()
        z_deg = dep.get()
        z_vit = year.get()
        if ((z_vit == " Select year " or z_vit == "All years") and (
                z_deg == " Select course " or z_deg == 'All courses')):
            listbox.insert(END, i)
        elif (z_deg == " Select course " or z_deg == 'All courses'):
            if z_vit == "All courses" or z_vit == " Select year":
                listbox.insert(END, i)
            else:
                z_vit_int = int(year.get()) * 100
                if ((int(asd[1]) >= z_vit_int and int(asd[1]) < (z_vit_int + 100))):
                    listbox.insert(END, i)
        elif (z_vit == " Select year " or z_vit == 'All years'):
            if (z_deg == asd[0]):
                listbox.insert(END, i)
        else:
            z_vit_int = int(year.get()) * 100
            if (asd[0] == z_deg and (int(asd[1]) >= z_vit_int and int(asd[1]) < (z_vit_int + 100))):
                listbox.insert(END, i)
######################

#Body
canvas = Canvas(
    window,
    bg = "#a8a8a8",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
# Shape settings

#Bottom Left
canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    68.0,
    402.0,
    603.0,
    688.0,
    fill="#7d7d7d",
    outline="black")

#Bottom Right
canvas.create_rectangle(
    673.0,
    402.0,
    1208.0,
    687.0,
    fill="#7d7d7d",
    outline="black")

#Middle Menu
canvas.create_rectangle(
    68.0,
    163.0,
    1208.0,
    360.0,
    fill="#7d7d7d",
    outline="black")

#Open File Button
button = customtkinter.CTkButton(text_font='constantia',hover_color='gray',text_color='black',fg_color='white', master=window, text="Select File",corner_radius=15,command=openFile)
button.place(x=90,y=75)

#Departament Text
canvas.create_text(
    903.0,
    179.0,
    anchor="nw",
    text="Departament",
    fill="#000000",
    font=("Constantia", 16 * -1)
)

#Top Menu
canvas.create_rectangle(
    68.0,
    55.0,
    1208.0,
    122.0,
    fill="#7d7d7d",
    outline="black")

#Courses Text
canvas.create_text(
    907.0,
    369.0,
    anchor="nw",
    text="Courses",
    fill="#000000",
    font=("Constantia", 16 * -1)
)

#Warnings Text
canvas.create_text(
    299.0,
    369.0,
    anchor="nw",
    text="Warnings",
    fill="#000000",
    font=("Constantia", 16 * -1)
)

#File Name Box
canvas.create_rectangle(
    246.0,
    76.0,
    1176.0,
    101.0,
    fill="#FFFFFF",
    outline="black")

#Listbox Name
label1 = Label(bd=0,bg='white',text='Please choose a file.',font='constantia')
label1.place(x=590,y=78)

#Buttons
display_button = customtkinter.CTkButton(text_font='constantia',hover_color='gray',text_color='black',fg_color='white', master=window, text="Display",corner_radius=20,command=display)
clear_button = customtkinter.CTkButton(text_font='constantia',hover_color='gray',text_color='black',fg_color='white', master=window, text="Clear",corner_radius=15, command=remove_all)
save_button =customtkinter.CTkButton(text_font='constantia',hover_color='gray',text_color='black',fg_color='white', master=window, text="Save",corner_radius=15, command=save)

display_button.place(x=290,y=300)
clear_button.place(x=570,y=300)
save_button.place(x=860,y=300)

#Warnings

#Courses

#Year Dropdown Menu
dropdown = Frame(window)
dropdown.place(x=310,y=210)
dropdown2 = Frame(window)
dropdown2.place(x=915,y=210)

year = StringVar(window)
year.set(" Select year ")
select_year = OptionMenu(dropdown, year, 'All years',1, 2, 3, 4, 5)
select_year.pack()

#Departament Dropdown Menu
dep = StringVar(window)
dept = ['All courses',"CHI",'CS','ECE','ECON','EE','EECS','ENGR','FRE','GER','IE','ISE','LIFE','MATH','MGY','UNI',]
dep.set(" Select course ")
select_dept = OptionMenu(dropdown2, dep,*dept)
select_dept.pack()

courses_frame = Frame(window,bg="#a8a8a8")
courses_frame.place(x=700,y=400)

listbox = Listbox(window,height=16,selectmode="multiple",width=83)
listbox.place(x=690,y=420)

warning1 = Listbox(window, width=83, height=16)
warning1.place(x=80,y=420)
#Year Text
canvas.create_text(
    322.0,
    179.0,
    anchor="nw",
    text="Year",
    fill="#000000",
    font=("Constantia", 16 * -1)
)

window.resizable(False, False)
window.mainloop()
