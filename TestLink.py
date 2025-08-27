import urllib.request
from tkinter import *
import tkinter as tk
import webbrowser
import subprocess

window=Tk()
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
window.geometry("700x350")
window.title("Site Checker")
head=Label(window, text="Website Connectivity Checker", font=('Calibri 15'))
head.pack(pady=20, side=tk.RIGHT)
listbox = tk.Listbox(window,height=6)
listbox.pack(padx=10, pady=10, expand=True, fill=tk.BOTH, side=tk.LEFT)
url=tk.StringVar()
Entry(window, textvariable=url).place(x=450,y=80,height=30,width=240)

def check():
    web=(url.get())
    if "," in web:
        urlList = [u.strip() for u in web.split(",")]
        print(urlList)
        num = 1
        for web1 in urlList:
            web1 = "https://" + web1
            execute(web1, num)
            num = num+1
    else:
        urlList = [web.strip()]  
           
                    

def execute(webpage, num):
    try:
        if (var1.get() == 1):
            subprocess.Popen([chrome_path, "--incognito","--new-window", webpage])
        status_code = urllib.request.urlopen(webpage).getcode()
        website_is_up = status_code == 200
        if website_is_up:
            listbox.insert(END,webpage + " is available")
        else:
            listbox.insert(END,webpage + " is available")
    except Exception as e:
        Label(window, text=f"Error: {e}", font=('Calibri', 10), fg="red").place(x=460, y=250)

var1 = tk.IntVar()
Button(window, text="Check", command=check).place(x=550, y=200)
Checkbutton(window, text="Open in browser?",variable=var1,onvalue=1, offvalue=0).place(x=500, y=250)
window.mainloop()

