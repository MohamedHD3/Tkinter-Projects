# Project 2 (Youtube Downloader by Tkinter)
from tkinter import * 
from tkinter import filedialog
from pytube import YouTube
root = Tk()
root.title('Youtube Downloader')
root.geometry('600x320')

# Youtube Link
yt_label = Label(root, text='Youtube Link')
yt_label.place(x=25, y=150)

yt_link = Entry(root, width=60)
yt_link.place(x=140, y=150)

# Download Folder
folder_label = Label(root, text='Download Folder')
folder_label.place(x=25, y=183)

folder_link = Entry(root, width=50)
folder_link.place(x=140, y=183)

# Browse Button
browse = Button(root, text='Browse')
browse.place(x=455, y=180)

# Download Button
download = Button(root, text='Download')
download.place(x=280, y=220)


root.mainloop()
