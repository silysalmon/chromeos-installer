import tkinter as tk
from tkinter import filedialog
from tkinter import PhotoImage
import webbrowser
import os

# master window
master = tk.Tk()

master.title("Chrome OS Installer")
master.geometry("260x420+500+200")
master.resizable(0, 0)

#icon
img = PhotoImage(file="/home/akash/pngwing.com (2).png")

#menubar
def about_menu():
    top = tk.Toplevel(master)
    top.title("About")
    top.geometry("150x200")
    top_label=tk.Label(top,image=img)
    top_label.pack()
    link = tk.Button(top,text="View Github Page",command=lambda: webbrowser.open("https://github.com/silysalmon/chromeos-installer"))
    link.pack()

top_menu = tk.Menu(master)
help_menu = tk.Menu(master,tearoff=0)
top_menu.add_cascade(label="Help",menu=help_menu,activebackground="teal",activeforeground="white")
help_menu.add_command(label="About",command=about_menu,activeforeground="teal")
help_menu.add_separator()
help_menu.add_command(label="Exit",command=master.quit,activeforeground="teal")
master.config(menu=top_menu)

# creating options
frame_icon = tk.Frame(master)
label_icon = tk.Label(frame_icon,image=img,width=100)
label_icon.pack()


frame_1 = tk.Frame(master)
label1 = tk.Label(frame_1, text="1.Download Latest ChromeOS Recovery: ")
label1.pack()

button1 = tk.Button(frame_1, text="Click here",
                    command=lambda: webbrowser.open("https://cros-updates-serving.appspot.com/"))
button1.pack()

frame_2 = tk.Frame(master)
label2 = tk.Label(frame_2, text="2.Create partitions:")
label2.pack()


def open_gparted():
    os.system("gparted")


button2 = tk.Button(frame_2, text="Gparted", command=open_gparted)
button2.pack()

frame_3 = tk.Frame(master)
label4 = tk.Label(frame_3, text="3.Enter the Partition Name(ex: /dev/sda3): ")
label4.pack()
entry1 = tk.Entry(frame_3, width=30)
entry1.pack()


frame_4 = tk.Frame(master)
label3 = tk.Label(frame_4, text="4.Source ChromeOS file(recovery.bin):")
label3.pack()

location = ""


def open_file():
    global location
    location = filedialog.askopenfilename(initialdir="/home", filetypes=(("BIN files", "*.bin"), ("All files", "*.*")))


button_file = tk.Button(frame_4, text="Choose file", command=open_file)
button_file.pack()


frame_5 = tk.Frame(master)
label_space = tk.Label(frame_5, text="5.Enter usable space (in GB,default 10GB):")
label_space.pack()

space_gb = tk.StringVar()
space_gb.set("10")
entry_space = tk.Entry(frame_5, width=30, textvariable=space_gb)
entry_space.pack()


def install():
    # os.system(
    #     "gnome-terminal -x sudo bash ./chromeos-install.sh -src " + location + " -dst " + entry1.get() + "-s " + entry_space.get())
    os.system("terminator -x sudo pacman -Syu")
frame_final = tk.Frame(master)
install_button = tk.Button(frame_final, text="Install", command=install,activebackground="teal",activeforeground="white",width=7,height=3)
install_button.pack()

#packing into window
frame_1.grid(row=1,column=0)
frame_2.grid(row=2,column=0)
frame_3.grid(row=3,column=0)
frame_4.grid(row=4,column=0)
frame_5.grid(row=5,column=0)
frame_final.grid(row=6,column=0)
frame_icon.grid(row=0,column=0)

master.mainloop()
