import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from time import sleep
from tkhtmlview import HTMLLabel
import userAlive
import os

txt_user = userAlive.giveUser()
session = userAlive.giveSS()


userAlive.banner(session, "Uruchomiona instancja")
userAlive.sysColorconsole("0", "4", "Uruchomiona instancja")


class Obszar_Roboczy:
    def __init__(self, root, txt_user, session):
        self.root = root
        self.root.title("Street HacKer v 1.001")
        self.root.geometry("330x720+820+20")
        self.root.resizable(False, False)   
        self.root.overrideredirect(True)  
        # self.root.attributes('-alpha', 0.95)
        self.txt_user = txt_user
        self.bg=ImageTk.PhotoImage(file="img/main_logoff.png")
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        def move_app(e):                   
            root.geometry(f'+{e.x_root-155}+{e.y_root-690}')

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
        

        self.widget_screen_main_okolica = ImageTk.PhotoImage(file='img/area_main_okolica0.png')
        self.widget_screen_main_dom = ImageTk.PhotoImage(file='img/area_main_dom0.png')
        self.widget_screen_main_adept = ImageTk.PhotoImage(file='img/area_main_login_adept.png')
        self.widget_screen_main_adept2 = ImageTk.PhotoImage(file='img/area_main_login_adept2.png')
        

        #######################################

        # Root/Okolica - Ramka Area

        ####################################### 
        arearea_ramka=Frame(self.root, bg="white")
        arearea_ramka.place(x=10, y=10, height=685, width=310)
        Label(arearea_ramka, image=self.widget_screen_main_adept).place(x=0, y=0, relwidth=1, relheight=1)
        Label(
                        arearea_ramka, 
                        text="Miejsca " + txt_user + "a", 
                        font=("Impact", 18),
                        fg="white", 
                        bg="black"
                        ).place(x=5, y=5)             
                
        
        self.list_oznaczone_news = []
        self.list_oznaczone_news_index = []
        self.list_oznaczone_tytul = userAlive.dataGeneral('fav_places' + str(self.txt_user), "kolumna1")   
        if self.list_oznaczone_tytul[0] == 'None':
            pass
        else:
            # print('To nie jest str None')
        
            idexes_list = len(self.list_oznaczone_tytul)
            
            for post in range(int(idexes_list)):
                insPos = " " + self.list_oznaczone_tytul[post]
                self.list_oznaczone_news_index.append(post)
                self.list_oznaczone_news.append(insPos)
                post += 1

            Label(
                            arearea_ramka, 
                            text="Lista zapisanych miejsc",
                            font=("Corbel", 15, "bold"),
                            fg="white", 
                            bg="black", 
                            justify="left"
                            ).place(x=5, y=50)


            self.my_listBox = Listbox(                            
                            arearea_ramka,                         
                            borderwidth=0, 
                            highlightthickness=0,
                            font=("Corbel", 12, "normal"),
                            fg="white", 
                            bg="black", 
                            justify="left"
                            )
            self.my_listBox.place(x=5, y=84, height=545, width=310)


            for item in self.list_oznaczone_news:
                self.my_listBox.insert(END, item)
            
            Button(
                    arearea_ramka, 
                    text="Leć tam",
                    command=self.teleportToPlace,
                    highlightbackground = "black", 
                    highlightthickness = 2,
                    bd=0,                        
                    font=("Impact", 18, "bold"),
                    fg="orange", 
                    bg="black", 
                    justify="left" 
                    ).place(x=5, y=630, width=310, height=30)


        
        ################################################################

        # MENU BOTTOM PAGE

        ################################################################

        checkSessions()
        menu_main=Frame(self.root, bg="black")
        menu_main.place(x=6, y=673, height=37, width=320)
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
                text="Miejsca", 
                fg="#79ffff", 
                bg="black", 
                bd=0, 
                font=("Arial", 10)
                ).place(x=55, y=9, width=45, height=20)
        
        Button(
                menu_main,
                command=self.exit,
                text="</> Console", 
                fg="gray", 
                bg="black", 
                bd=0, 
                font=("Arial", 10, "bold")
                ).place(x=220, y=9, width=85, height=20)

    def exit(self):
        userAlive.goTodo('okolica.py')
        userAlive.exitSys()

    def teleportToPlace(self):
        
        choice = self.my_listBox.get(ANCHOR) 
        choice = choice.strip()       
        
        lat = userAlive.dataUserSELECT('fav_places', str(txt_user), "kolumna1", str(choice), 'kolumna2')
        lng = userAlive.dataUserSELECT('fav_places', str(txt_user), "kolumna1", str(choice), 'kolumna3')

        userid = userAlive.dataUserSELECT('users_main', '', 'user', str(txt_user), 'identyfikator')
        useridforchanged = userid[0]
        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_y', str(lat[0]), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_x', str(lng[0]), useridforchanged)
        
        googlePart1 = """https://earth.google.com/web/@"""
        googlePart2 = str(lat[0])
        googlePart3 = ","
        googlePart4 = str(lng[0])
        googlePart5 = """,80.88106533a,3324.79213989d,1y,0h,0t,0r" """
        prepareLinkGoogleE = googlePart1 + googlePart2 + googlePart3 + googlePart4 + googlePart5
        userAlive.goTodo('StreetHackerBrowser.py -a ' + prepareLinkGoogleE)       
        userAlive.goTodo('okolica.py')
        userAlive.goTodo('detector3dgoogledron.py')
        
        userAlive.exitSys()



        

root = tkinter.Tk()
area = Obszar_Roboczy(root, txt_user, session)

root.mainloop()