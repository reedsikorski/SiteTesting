import urllib.request
from tkinter import *
import tkinter as tk
import webbrowser
import subprocess
import requests

window=Tk()
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
window.geometry("1000x400")
window.title("Site Checker")
head=Label(window, text="Website Connectivity Checker", font=('Calibri 15'))
head.grid(row=1,column=1, pady=25)
listbox = tk.Listbox(window,height=10,width=100)
listbox.grid(row=0,column=0,padx=25, rowspan=6)
url=tk.StringVar()
entry = Entry(window, textvariable=url)
entry.grid(row=2, column=1)

def check():
    web=(url.get())
    if "," in web:
        urlList = [u.strip() for u in web.split(",")]
        num = 1
        for web1 in urlList:
            web1 = "https://" + web1
            execute(web1)
    else:
        if url.get().startswith("https://"):
            execute(url.get())
        else:
            execute("https://" + url.get()) 
           
                    

def execute(webpage):
    try:
        # status_code = urllib.request.urlopen(webpage).getcode()
        # website_is_up = status_code == 200
        r = requests.get(webpage)
        if r.status_code == 200:
            listbox.insert(END,webpage + " is available with a status code of 200")
            if (var1.get() == 1):
                subprocess.Popen([chrome_path, "--incognito","--new-window", webpage])
        else:
            listbox.insert(END,webpage + " responded with a code of " + r.status_code)
    except Exception as e:
        listbox.insert(END,webpage + " responded with an error of " + str(e))

var1 = tk.IntVar()
var2 = tk.IntVar()
button = Button(window, text="Check", command=check)
button.grid(row=3,column=1)
check1 = Checkbutton(window, text="Open in browser?",variable=var1,onvalue=1, offvalue=0)
check1.grid(row=4,column=1)
check2=Checkbutton(window, text="Save results to CSV?",variable=var2,onvalue=1, offvalue=0)
check2.grid(row=5,column=1)
window.mainloop()

