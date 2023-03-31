import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
import os
import random
from time import sleep
import time
from tkhtmlview import HTMLLabel
import folium
import userAlive

txt_user = userAlive.giveUser()
session = userAlive.giveSS()

userAlive.banner(session, "Uruchomiona instancja")





class Obszar_Roboczy:
    def __init__(self, root, txt_user, session):
        self.root = root
        self.root.title("Street HacKer v 1.001")
        self.root.geometry("480x640+20+20")
        self.root.resizable(False, False)   
        self.root.overrideredirect(True)  
        # self.root.attributes('-alpha', 0.5)
        self.txt_user = txt_user
        self.bg=ImageTk.PhotoImage(file="img/main_logoff.png")
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        def move_app(e):                   
            root.geometry(f'+{e.x_root-260}+{e.y_root-600}')

        self.txt_user = txt_user
        self.session = session

        def checkSessions():
            if self.txt_user != self.session:                
                userAlive.exitSys()


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
        widget_screen_main_image=Label(area_ramka, image=self.widget_screen_main).place(x=0, y=0, relwidth=1, relheight=1)
        
        area_title=Label(
                        area_ramka, 
                        text="Hacker profil", 
                        font=("Impact", 45, "normal"),
                        fg="white", 
                        bg="black"
                        ).place(x=5, y=5) 
        area_LvL=Label(
                        area_ramka, 
                        text="Poziom gracza", 
                        font=("Helvetica", 8, "normal"),
                        fg="gray", 
                        bg="black",
                        justify="left"
                        ).place(x=325, y=417)
        rang_playa = "Hacker Anonymous" # Uczeń hakerstwa, Praktyk hakerstwa, Hacker najemnik, Hacker z ekipy, Hacker leader, Boss hacker, Hacker Anonymous  
        area_LvL=Label(
                        area_ramka, 
                        text="Ranga\n" + str(rang_playa), 
                        font=("Helvetica", 8, "normal"),
                        fg="gray", 
                        bg="black",
                        justify="left"
                        ).place(x=325, y=465)
        LvL_nr = 1
        area_LvL_nr=Label(
                        area_ramka, 
                        text="# " + str(LvL_nr), 
                        font=("Times New Roman", 11, "normal"),
                        fg="orange", 
                        bg="black",
                        justify="left"
                        ).place(x=325, y=438) 
        area_profesje=Label(
                        area_ramka, 
                        text=str(self.txt_user), 
                        font=("Corbel", 30, "normal"),
                        fg="white", 
                        bg="black", 
                        justify="right"
                        ).place(x=5, y=80)
        list_profesje = ['Hacker Adept', 'Hacking Light', 'Brutal Force', 'Darknet Hacking', 'Hacking Maklerski', 'Hacking samochodowy']
        area_profesje=Label(
                        area_ramka, 
                        text="Profesje:",
                        font=("Corbel", 12, "normal"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        ).place(x=5, y=135)
        
        profesja_pozycja = 165
        for kolejna_profesja in list_profesje:
            area_profesja_nazwy=Label(
                            area_ramka, 
                            text=str(kolejna_profesja),
                            font=("Corbel", 7, "normal"),
                            fg="gray", 
                            bg="black", 
                            justify="left"
                            ).place(x=10, y=profesja_pozycja)
            profesja_pozycja += 20
        
        list_zbroje = ['Keblarowa kamizelka', 'Plecak kuloodporny', 'Rękawice złodziejki', 'Plecak kuloodporny', 'Rękawice złodziejki']
        area_zbroja=Label(
                        area_ramka, 
                        text="Zbroja:",
                        font=("Corbel", 12, "normal"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        ).place(x=105, y=135)
        zbroja_pozycja = 165
        for rzecz_zbroja in list_zbroje:
            area_bron_nazwy=Label(
                            area_ramka, 
                            text=str(rzecz_zbroja),
                            font=("Corbel", 7, "normal"),
                            fg="gray", 
                            bg="black", 
                            justify="left"
                            ).place(x=110, y=zbroja_pozycja)
            zbroja_pozycja += 20
        

        list_bron = ['Kij baseballowy', 'Nóż bojowy', 'Gaz żel', 'Nóż bojowy', 'Gaz żel', 'Nóż bojowy', 'Gaz żel', 'Nóż bojowy']
        area_bron=Label(
                        area_ramka, 
                        text="Uzbrojenie:",
                        font=("Corbel", 12, "normal"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        ).place(x=265, y=135)
        bron_pozycja = 165
        for rzecz_bron in list_bron:
            area_bron_nazwy=Label(
                            area_ramka, 
                            text=str(rzecz_bron),
                            font=("Corbel", 7, "normal"),
                            fg="gray", 
                            bg="black", 
                            justify="left"
                            ).place(x=270, y=bron_pozycja)
            bron_pozycja += 20

        list_plecak = ['Laptop asus', 'Adapter bluetooth', 'penDrive 100GB', 'Adapter bluetooth', 'penDrive 100GB', 'Adapter bluetooth', ]
        area_plecak=Label(
                        area_ramka, 
                        text="Plecak:",
                        font=("Corbel", 12, "normal"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        ).place(x=375, y=135)
        plecak_pozycja = 165
        for rzecz_plecak in list_plecak:
            area_plecak_nazwy=Label(
                            area_ramka, 
                            text=str(rzecz_plecak),
                            font=("Corbel", 7, "normal"),
                            fg="gray", 
                            bg="black", 
                            justify="left"
                            ).place(x=380, y=plecak_pozycja)
            plecak_pozycja += 20
        ilosc__Vcrypto = 9.007501
        area_Vcrypto=Label(
                        area_ramka, 
                        text="Witrualne krypto-waluty:",
                        font=("Corbel", 10, "bold"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        ).place(x=10, y=330)
        area_Vcrypto_saldo=Label(
                        area_ramka, 
                        text=str(ilosc__Vcrypto) + " VCV",
                        font=("Corbel", 14, "bold"),
                        fg="black", 
                        bg="white", 
                        justify="left"
                        ).place(x=70, y=355)
        ilosc__Vcoin = 9998.75
        area_Vcoin=Label(
                        area_ramka, 
                        text="Witrualne dolary: ",
                        font=("Corbel", 10, "bold"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        ).place(x=10, y=395)
        area_Vcoin_saldo=Label(
                        area_ramka, 
                        text="VS$ " + str(ilosc__Vcoin),
                        font=("Corbel", 14, "bold"),
                        fg="black", 
                        bg="white", 
                        justify="left"
                        ).place(x=70, y=418)
        ilosc__RUSD = 728.05
        area_RUSD=Label(
                        area_ramka, 
                        text="Dolary Amerykańskie:",
                        font=("Corbel", 10, "bold"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        ).place(x=10, y=455)
        area_RUSD_saldo=Label(
                        area_ramka, 
                        text="USD $ " + str(ilosc__RUSD),
                        font=("Corbel", 14, "bold"),
                        fg="black", 
                        bg="white", 
                        justify="left"
                        ).place(x=70, y=480)
        ilosc__XBTC =  8.00002555
        area_XBTC=Label(
                        area_ramka, 
                        text="BitCoin BTC:",
                        font=("Corbel", 10, "bold"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        ).place(x=10, y=515)
        area_XBTC_saldo=Label(
                        area_ramka, 
                        text="BTC " + str(ilosc__XBTC),
                        font=("Corbel", 14, "bold"),
                        fg="black", 
                        bg="white", 
                        justify="left"
                        ).place(x=70, y=540)
        

        ilosc_pulapki =  11
        area__pulapki=Label(
                        area_ramka, 
                        text="Zastawione pułapki: " + str(ilosc_pulapki),
                        font=("Corbel", 8, "bold"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        ).place(x=230, y=504)                            
        ilosc_oznaczonych_cel =  17
        area_oznaczonych_cel=Label(
                        area_ramka, 
                        text="Oznaczonych ofiar ataku: " + str(ilosc_oznaczonych_cel),
                        font=("Corbel", 8, "bold"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        ).place(x=230, y=521)                
        ilosc__attaks_succes =  9
        area_attaks_succes=Label(
                        area_ramka, 
                        text="Udane ataki: " + str(ilosc__attaks_succes),
                        font=("Corbel", 8, "bold"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        ).place(x=230, y=538)
        ilosc__attaks_loses =  3
        area_attaks_loses=Label(
                        area_ramka, 
                        text="Nieudane próby ataku: " + str(ilosc__attaks_loses),
                        font=("Corbel", 8, "bold"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        ).place(x=230, y=555)

        area_ramka_image2=Frame(self.root, bg="green")
        area_ramka_image2.place(x=237, y=428, height=83, width=92)                
        logo_main_image2=Label(area_ramka_image2, image=self.logo_main_image2).place(x=1, y=1, height=81, width=90)
        #######################################
        #
        # Root/Profill - Ramka MAIN MENU
        #
        #######################################
        checkSessions()
        menu_main=Frame(self.root, bg="black")
        menu_main.place(x=6, y=596, height=37, width=468)
        menu_main.bind("<B1-Motion>", move_app)

        menu_title=Label(
                        menu_main, 
                        text="Widget: ", 
                        font=("Sylfaen", 11),
                        fg="gray", 
                        bg="black"
                        ).place(x=5, y=5)
        m_profil=Label(
                        menu_main,
                        text="Profil", 
                        fg="#79ffff", 
                        bg="black", 
                        bd=0, 
                        font=("Arial", 10)
                        ).place(x=55, y=9, width=45, height=20)
        
        m_widget_dolny=Button(
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
    
    
        


root = tkinter.Tk()
area = Obszar_Roboczy(root, txt_user, session)

root.mainloop()