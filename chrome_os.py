import tkinter as tk
from tkinter import filedialog
import webbrowser
import os
import sh
#master window
master = tk.Tk()

master.title("Chrome OS Installer")
master.geometry("480x320+450+200")
master.resizable(0,0)

#creating options
label1 = tk.Label(master,text="Download Latest ChromeOS Recovery: ")
label1.grid(row=0,column=0,columnspan=3,rowspan=2)

button1 = tk.Button(master,text="Click here",command=lambda : webbrowser.open("https://cros-updates-serving.appspot.com/"))
button1.grid(row=0,column=3,rowspan=2)

label2 = tk.Label(master,text="Create partitions:")
label2.grid(row=3,column=0,columnspan=3,rowspan=2)


def open_gparted():
    os.system("gparted")




button2 = tk.Button(master,text="Gparted",command=open_gparted)
button2.grid(row=3,column=3,rowspan=2)

label4 = tk.Label(master,text="Enter the Partition Name(ex: /dev/sda3): ")
label4.grid(row=5,column=0,columnspan=3)

entry1 = tk.Entry(master,width=30)
entry1.grid(row=5,column=3)

label3 = tk.Label(master,text="Source ChromeOS file(recovery.bin):")
label3.grid(row=7,column=0,columnspan=3)

location = ""

def open_file():
    global location
    location = filedialog.askopenfilename(initialdir="/home",filetypes=(("BIN files" ,"*.bin"),("All files","*.*")))

button_file = tk.Button(master,text="Choose file",command=open_file)
button_file.grid(row=7,column=3)


label_space = tk.Label(master,text="Enter usable space (in GB,default 10GB):")
label_space.grid(row=8,column=0)

space_gb = tk.StringVar()
space_gb.set("10")
entry_space = tk.Entry(master,width=30,textvariable=space_gb)
entry_space.grid(row=8,column=3)

def install():
    os.system("xterm -e sudo bash chromeos-install.sh -src "+location+ " -dst "+entry1.get()+"-s "+ entry_space.get())

install_button = tk.Button(master,text="Install",command=install,anchor="center")
install_button.grid(row=9,column=0)



master.mainloop()
