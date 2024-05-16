import os
import platform
import pyrubi
import pyfiglet
import colorama
import time
import tkinter as tk
from tkinter import messagebox

def clear_screen():
    if platform.uname()[0] == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def report():
    Ty = choice.get()
    Li = link_entry.get()
    Te = description_entry.get("1.0", "end-1c")
    
    if Ty == "2" or Ty == "۲" or Ty == "[2]":
        Get = bot.join_chat(Li)
        guid = Get['group']['group_guid']
        Name = Get['group']['group_title']
    elif Ty == "3" or Ty == "۳" or Ty == "[3]":
        if Li.startswith("https://rubika.ir/joinc/"):
            Get = bot.join_chat(Li)
            guid = Get['channel']['channel_guid']
            Name = Get['channel']['channel_title']
        else:
            Get = bot.get_chat_info_by_username(Li)
            guid = Get['channel']['channel_guid']
            Name = Get['channel']['channel_title']
    elif Ty == "1" or Ty == "۱" or Ty == "[1]":
        Get = bot.get_chat_info_by_username(Li)
        guid = Get['user']['user_guid']
        Name = Get['user']['first_name'] + Get['user']['last_name']
    else:
        clear_screen()
        messagebox.showerror("Error", "Not available!")
        return

    clear_screen()
    report_text = f"Name >>> {Name}\nGuid >>> {guid}\n\n{Te}"
    result_label.config(text=report_text)
    time.sleep(1)
    
    n = 0
    while True:
        try:
            bot.report_chat(guid, description=Te)
            n += 1
            result_label.config(text=f"Report OK [{n}]")
            root.update()
            time.sleep(1)
        except:
            pass

clear_screen()

try:
    import pyrubi
except:
    os.system("pip install pyrubi")
try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")
try:
    import colorama
except:
    os.system("pip install colorama")

colorama.init()
bot = pyrubi.Client("P-D99999")
root = tk.Tk()
root.title("Rubika Reporter")
root.geometry("400x400")

font = pyfiglet.Figlet()
title_label = tk.Label(root, text=font.renderText(" RASOUL "), fg="cyan")
title_label.pack()

dev_label = tk.Label(root, text="Dev >>> @Rasoul_adz", fg="cyan")
dev_label.pack()

choice_label = tk.Label(root, text="Choose Report Type:")
choice_label.pack()

choice = tk.StringVar(root)
choice.set("2")  # default value

radio_frame = tk.Frame(root)
radio_frame.pack()

radio_button1 = tk.Radiobutton(radio_frame, text="Report User Rubika", variable=choice, value="1")
radio_button2 = tk.Radiobutton(radio_frame, text="Report Group Rubika", variable=choice, value="2")
radio_button3 = tk.Radiobutton(radio_frame, text="Report Channel Rubika", variable=choice, value="3")

radio_button1.pack(anchor=tk.W)
radio_button2.pack(anchor=tk.W)
radio_button3.pack(anchor=tk.W)

link_label = tk.Label(root, text="Enter Link or ID:")
link_label.pack()

link_entry = tk.Entry(root, width=30)
link_entry.pack()

description_label = tk.Label(root, text="Enter Description (code filtering):")
description_label.pack()

description_entry = tk.Text(root, width=40, height=6)
description_entry.pack()

submit_button = tk.Button(root, text="Submit", command=report)
submit_button.pack()

result_label = tk.Label(root, text="", fg="green")
result_label.pack()

root.mainloop()
