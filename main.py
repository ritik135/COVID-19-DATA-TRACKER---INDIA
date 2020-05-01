# import all the libraries required

import requests
import bs4
import plyer
import tkinter as tk
import time
import datetime
import threading


def get_html_data(url):
    data = requests.get(url)
    return data


def get_corona_details_of_india():
    url = "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div",class_="site-stats-count")
    all_details=""

    count=info_div.find("li",class_="bg-blue").find("strong").get_text()
    text=info_div.find("li",class_="bg-blue").find("span").get_text()
    all_details = all_details + text + " : " + count + "\n"


    count = info_div.find("li", class_="bg-green").find("strong").get_text()
    text = info_div.find("li", class_="bg-green").find("span").get_text()
    all_details = all_details + text + " : " + count + "\n"


    count = info_div.find("li", class_="bg-red").find("strong").get_text()
    text = info_div.find("li", class_="bg-red").find("span").get_text()
    all_details = all_details + text + " : " + count + "\n"


    count = info_div.find("li", class_="bg-orange").find("strong").get_text()
    text = info_div.find("li", class_="bg-orange").find("span").get_text()
    all_details = all_details + text + " : " + count + "\n"

    return ( all_details )


#print(get_corona_details_of_india())

#function to reload data from website

def refresh():
    new_data = get_corona_details_of_india()
    print("Refreshing...")
    mainLabel['text']=new_data

#function to notify

def notify_me():
    while True:
        plyer.notification.notify(
            title="COVID-19 CASES OF INDIA",
            message=get_corona_details_of_india(),
            timeout=10,
            app_icon='icon.ico'
        )
        time.sleep(1000)

# creating GUI

root = tk.Tk()
root.geometry("600x600")
root.iconbitmap("icon.ico")
root.title("COVID-19 LIVE DATA TRACKER - INDIA")
root.configure(background='white')
f=("poppins",25,"bold")
banner=tk.PhotoImage(file="virus.png")
bannerLabel=tk.Label(root,image=banner)
bannerLabel.pack()
mainLabel=tk.Label(root,text=get_corona_details_of_india(),font=f,bg='white')
mainLabel.pack()

reBtn=tk.Button(root,text="REFRESH",font=f,relief='solid',command=refresh)
reBtn.pack()

#create a new thread

th1=threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()

root.mainloop()
