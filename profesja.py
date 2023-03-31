import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

import os
import random
from time import sleep

from tkhtmlview import HTMLLabel

import userAlive

txt_user = userAlive.giveUser()
session = userAlive.giveSS()

userAlive.banner(session, "Uruchomiona instancja")
userAlive.sysColorconsole("0", "4", "Uruchomiona instancja")

class Obszar_Roboczy:
    def __init__(self, root):
        self.root = root
        self.root.title("Street HacKer v 1.001")
        self.root.geometry("480x640+520+20")
        self.root.resizable(False, False)   
        self.root.overrideredirect(True)       
        self.root.attributes('-alpha', 0.9)
        self.txt_user = txt_user
        self.bg=ImageTk.PhotoImage(file="img/main_logoff.png")
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        def move_app(e):        
            root.geometry(f'+{e.x_root-260}+{e.y_root-600}')
        #######################################
        #
        # linki do obrazkow
        #
        #######################################
        self.widget_screen_main = ImageTk.PhotoImage(file='img/area_main_logoff.png')
        self.logo_main_image2 = ImageTk.PhotoImage(file='img/logo.png')
       
        #######################################
        #
        # Root/Profill - Ramka Area
        #
        ####################################### 
        area_ramka=Frame(self.root, bg="white")
        area_ramka.place(x=10, y=10, height=570, width=460)
        Label(area_ramka, image=self.widget_screen_main).place(x=0, y=0, relwidth=1, relheight=1)
        Label(
                        area_ramka, 
                        text="Profesja", 
                        font=("Impact", 42),
                        fg="white", 
                        bg="black"
                        ).place(x=5, y=5)
        
        Label(
                        area_ramka, 
                        text="Hackowanie pojazdów", 
                        font=("Corbel", 18, "bold"),
                        fg="orange", 
                        bg="black"
                        ).place(x=5, y=75)
        Label(
                        area_ramka, 
                        text="Za pomoca specjanych narzedzi Hacker uzyskuje informacje o wybranym\ncelu attacku. Daje mu to mozliwość oznaczenia wybranego celu\nataku i skuteczną jego realizację.", 
                        font=("Corbel", 10),
                        fg="gray", 
                        bg="black",
                        justify="left"
                        ).place(x=5, y=110)
        Button(
                        area_ramka,
                        # command=self.cel_samochodowy,
                        text="</>CEL ", 
                        fg="#b4fffa", 
                        bg="black", 
                        bd=0, 
                        justify="left",
                        font=("Arial", 7)
                        ).place(x=260, y=80, height=15)
        Button(
                        area_ramka,
                        # command=self.cel_samochodowy,
                        text="</>HCK ", 
                        fg="#b4fffa", 
                        bg="black", 
                        bd=0, 
                        justify="left",
                        font=("Arial", 7)
                        ).place(x=300, y=80, height=15)
        
        Label(
                        area_ramka, 
                        text="Hackowanie e-money", 
                        font=("Corbel", 15, "bold"),
                        fg="orange", 
                        bg="black"
                        ).place(x=5, y=165)
        Label(
                        area_ramka, 
                        text="Po uzyskaniu informacji na temat ofiary, Hacker rozpoczyna atak. Jego \ncelem jest przejęcie portfeli krypto i kont bankowych. Ofiara mogła źle \nzabepieczyć swoje hasła dostępu. Skuteczność ataku się zwiekszy.", 
                        font=("Corbel", 10),
                        fg="gray", 
                        bg="black",
                        justify="left"
                        ).place(x=5, y=195)
        Button(
                        area_ramka,
                        # command=self.cel_samochodowy,
                        text="</>INFO ", 
                        fg="#b4fffa", 
                        bg="black", 
                        bd=0, 
                        justify="left",
                        font=("Arial", 7)
                        ).place(x=220, y=165, height=15)
        Button(
                        area_ramka,
                        # command=self.cel_samochodowy,
                        text="</>METS ", 
                        fg="#b4fffa", 
                        bg="black", 
                        bd=0, 
                        justify="left",
                        font=("Arial", 7)
                        ).place(x=270, y=165, height=15)         
 
        Label(
                        area_ramka, 
                        text="Ataki brutalnej siły", 
                        font=("Corbel", 15, "bold"),
                        fg="orange", 
                        bg="black"
                        ).place(x=5, y=255)
        Label(
                        area_ramka, 
                        text="Zestaw narzędzi, jakimi dysponuje hacker, daje wiele szans powodzenia. \nOznaczona ofiara ataku nawet nie podejrzewa nadchodzącego zagrożenia. \nUrządzenia, aplikacje i sieć domowa zostaną zhakowane bez powiadomienia", 
                        font=("Corbel", 10),
                        fg="gray", 
                        bg="black",
                        justify="left"
                        ).place(x=5, y=285) 
        Button(
                        area_ramka,
                        # command=self.cel_samochodowy,
                        text="</>CEL ", 
                        fg="#b4fffa", 
                        bg="black", 
                        bd=0, 
                        justify="left",
                        font=("Arial", 7)
                        ).place(x=190, y=255, height=15)
        Button(
                        area_ramka,
                        # command=self.cel_samochodowy,
                        text="</>LISTA ", 
                        fg="#b4fffa", 
                        bg="black", 
                        bd=0, 
                        justify="left",
                        font=("Arial", 7)
                        ).place(x=230, y=255, height=15)
        Button(
                        area_ramka,
                        # command=self.cel_samochodowy,
                        text="</>ATAK ", 
                        fg="#b4fffa", 
                        bg="black", 
                        bd=0, 
                        justify="left",
                        font=("Arial", 7)
                        ).place(x=280, y=255, height=15)        

        Label(
                        area_ramka, 
                        text="Lekki hacking", 
                        font=("Corbel", 15, "bold"),
                        fg="orange", 
                        bg="black"
                        ).place(x=5, y=338)
        Label(
                        area_ramka, 
                        text="Hacking to zabawa, nauka i przyjemność a trening czyni mistrza. Praktyka \n daje użytek z posiadanej wiedzy, a hacker uśmiecha się zerakjąc na\nswoją ofiarę ataku, bystrym wzrokiem z pod kapelusza.", 
                        font=("Corbel", 10),
                        fg="gray", 
                        bg="black",
                        justify="left"
                        ).place(x=5, y=368) 
        Button(
                        area_ramka,
                        command=self.scan,
                        text="</>SCAN ", 
                        fg="#b4fffa", 
                        bg="black", 
                        bd=0, 
                        justify="left",
                        font=("Arial", 7)
                        ).place(x=140, y=338, height=15)
        Button(
                        area_ramka,
                        command=self.phone,
                        text="</>PHONE ", 
                        fg="#b4fffa", 
                        bg="black", 
                        bd=0, 
                        justify="left",
                        font=("Arial", 7)
                        ).place(x=187, y=338, height=15)        

        Label(
                        area_ramka, 
                        text="Hackowanie za pomocą DarkNet", 
                        font=("Corbel", 15, "bold"),
                        fg="orange", 
                        bg="black"
                        ).place(x=5, y=422)
        Label(
                        area_ramka, 
                        text="DarkNet świetne miejsce na złapanie w sidła jakieś bezbronnej rybki. \nPrzejżyj zastawione pułapki, publikuj lub poprostu przegladaj DarkNet.", 
                        font=("Corbel", 10),
                        fg="gray", 
                        bg="black",
                        justify="left"
                        ).place(x=5, y=452)
        Button(
                        area_ramka,
                        # command=self.cel_samochodowy,
                        text="</>TRAP ", 
                        fg="#b4fffa", 
                        bg="black", 
                        bd=0, 
                        justify="left",
                        font=("Arial", 7)
                        ).place(x=292, y=422, height=15)
        Button(
                        area_ramka,
                        # command=self.cel_samochodowy,
                        text="</>DARK ", 
                        fg="#b4fffa", 
                        bg="black", 
                        bd=0, 
                        justify="left",
                        font=("Arial", 7)
                        ).place(x=340, y=422, height=15)        

        Label(
                        area_ramka, 
                        text="Hacker base", 
                        font=("Corbel", 15, "bold"),
                        fg="orange", 
                        bg="black"
                        ).place(x=5, y=494)
        Label(
                        area_ramka, 
                        text="Przejrzyj newsy lub rusz się w poszukiwaniu doswiadczenia. Zbieraj \ninformacje o swojej okolicy i pomyśl nad jakimś skutecznym atakiem.", 
                        font=("Corbel", 10),
                        fg="gray", 
                        bg="black",
                        justify="left"
                        ).place(x=5, y=524) 
        Button(
                        area_ramka,
                        command=self.news,
                        text="</>NEWS ", 
                        fg="#b4fffa", 
                        bg="black", 
                        bd=0, 
                        justify="left",
                        font=("Arial", 7)
                        ).place(x=166, y=494, height=15)
        Button(
                        area_ramka,
                        command=self.walk,
                        text="</>WALK ", 
                        fg="#b4fffa", 
                        bg="black", 
                        bd=0, 
                        justify="left",
                        font=("Arial", 7)
                        ).place(x=218, y=494, height=15)
        Button(
                        area_ramka,
                        command=self.tools,
                        text="</>TOOLS ", 
                        fg="#b4fffa", 
                        bg="black", 
                        bd=0, 
                        justify="left",
                        font=("Arial", 7)
                        ).place(x=270, y=494, height=15)
        #######################################
        #
        # Root/Profill - Ramka MAIN MENU
        #
        #######################################
        menu_main=Frame(self.root, bg="black")
        menu_main.place(x=6, y=596, height=37, width=468)
        menu_main.bind("<B1-Motion>", move_app)

        Label(
                        menu_main, 
                        text="Widget: ", 
                        font=("Sylfaen", 11),
                        fg="gray", 
                        bg="black"
                        ).place(x=5, y=5)
        Label(
                        menu_main,
                        text="Profesja", 
                        fg="#79ffff", 
                        bg="black", 
                        bd=0, 
                        font=("Arial", 10)
                        ).place(x=55, y=9, width=65, height=20)
        
        Button(
                        menu_main,
                        command=self.exit,
                        text="</> Console", 
                        fg="gray", 
                        bg="black", 
                        bd=0, 
                        font=("Arial", 10, "bold")
                        ).place(x=375, y=9, width=85, height=20)
    def exit(self):
        userAlive.exitSys()
    
    def tools(self):
        userAlive.goTodo("tools.py")
        userAlive.sendUser(txt_user)
        userAlive.writeSS(txt_user)
    
    def news(self):
        userAlive.goTodo("news.py")
        userAlive.sendUser(txt_user)
        userAlive.writeSS(txt_user)
    
    def walk(self):
        userAlive.goTodo("okolica.py")
        userAlive.sendUser(txt_user)
        userAlive.writeSS(txt_user)

    def scan(self):
        userAlive.goTodo("szukaj.py")
        userAlive.sendUser(txt_user)
        userAlive.writeSS(txt_user)
    
    def phone(self):
        userAlive.goTodo("telefon.py")
        userAlive.sendUser(txt_user)
        userAlive.writeSS(txt_user)
        

userAlive.checking_bar("Profesje" + txt_user, 100, 0.03)
root = tkinter.Tk()
area = Obszar_Roboczy(root)
root.mainloop()