# Project 1
from tkinter import *
from tkinter import ttk
import tkcalendar

root = Tk()
root.title('Data Entry Form')
root.geometry('470x340')

# title
title = Label(root, text='Data Entry Form', font='Calibre 20 bold')
title.grid(row=0, column=0, columnspan=4, pady=5)

# first and last name
fname_label = Label(root, text='First Name')
fname_label.grid(row=1, column=0, padx=8, sticky='w')

fname_entry = Entry(root, width=20)
fname_entry.grid(row=1, column=1)

lname_label = Label(root, text='Lirst Name')
lname_label.grid(row=1, column=2, padx=8)

lname_entry = Entry(root, width=20)
lname_entry.grid(row=1, column=3)

# birth date
birth_label = Label(root, text='Birth Date')
birth_label.grid(row=2, column=0, padx=8, sticky='w')

birth_entry = tkcalendar.DateEntry(root, width=20)
birth_entry.grid(row=2, column=1, pady=5, sticky='we', columnspan=3)

# gender
gender_label = Label(root, text='Gender')
gender_label.grid(row=3, column=0, sticky='w', padx=8)

gender = StringVar()
gender.set('none')

male = Radiobutton(root, text='Male', value='Male', variable=gender)
male.grid(row=3, column=1, sticky='w')

female = Radiobutton(root, text='Female', value='Female', variable=gender)
female.grid(row=3, column=2, sticky='w')

# country
country_label = Label(root, text='Country')
country_label.grid(row=4, column=0, sticky='w', padx=8, pady=5)

country_choices = ttk.Combobox(root, width=20, values=['Saudi Arabia', 'Palestine', 'Eqypt', 'UAE', 'Jordan', 'Morocco'])
country_choices.grid(row=4, column=1, columnspan=3, sticky='we')

# address
address_label = Label(root, text='Address')
address_label.grid(row=5, column=0, sticky='nw', padx=8)

address_text = Text(root, width=20, height=5)
address_text.grid(row=5, column=1, sticky='we', columnspan=3)


# buttons

def record(): # to CSV
    first_name = fname_entry.get()
    last_name = lname_entry.get()
    birth_date = birth_entry.get()
    gend = gender.get()
    country = country_choices.get()
    address = address_text.get('1.0', 'end-1c') # get('Num. line'.'index Char.', 'to end text - 1 Char.') becouse many lines
    text = first_name + ',' + last_name + ',' + birth_date + ',' + gend + ',' + country + ',' + address +'\n' # new line to ready to record anthor data 
    with open(r"C:\Users\mohdh\Desktop\file.csv", "a") as file:
        file.write(text)
    clear_all()
        
def clear_all():
    fname_entry.delete(0, 'end')
    lname_entry.delete(0, 'end')
    birth_entry.delete(0, 'end')
    gender.set('none')
    country_choices.delete(0, 'end')
    address_text.delete('1.0', 'end')
    fname_entry.focus_set()

save_button = Button(root, text='Save', command=record)
save_button.grid(row=6, column=1, padx=8, pady=5, sticky='e', ipadx=10)

clear_button = Button(root, text='Clear', command=clear_all)
clear_button.grid(row=6, column=2, padx=8, sticky='w', ipadx=10)

root.mainloop()