import tkinter
from tkinter import Label, Button, Frame, Listbox, END, ANCHOR
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
        # self.root.attributes('-alpha', 0.5)
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
                        text="Selecting Taget Master", 
                        font=("Impact", 18),
                        fg="white", 
                        bg="black"
                        ).place(x=5, y=5)           
                
        
        self.listSelectingTargets = []
        self.listSelectingTargets_index = set()
        self.listSelectingTargets_tytul = userAlive.dataGeneral('terra_scan' + str(self.txt_user), "kolumna4")        
        
                
        for post in self.listSelectingTargets_tytul:   
            self.listSelectingTargets_index.add(post)            
           

        for insSetToList in self.listSelectingTargets_index:            
            self.listSelectingTargets.append(str(insSetToList))

        Label(
                        arearea_ramka, 
                        text="Rodzaj tagetu",
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


        for item in self.listSelectingTargets:
            self.my_listBox.insert(END, item)
        
        Button(
                arearea_ramka, 
                text="Leć tam",
                command=self.categoryScan,
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
        userAlive.exitSys()

    def categoryScan(self):
        choice = self.my_listBox.get(ANCHOR) 
        choice = choice.strip()


        #######################################

        # Root/Okolica - Ramka Area

        ####################################### 
        arearea_ramka=Frame(self.root, bg="white")
        arearea_ramka.place(x=10, y=10, height=685, width=310)
        Label(arearea_ramka, image=self.widget_screen_main_adept).place(x=0, y=0, relwidth=1, relheight=1)
        Label(
                        arearea_ramka, 
                        text="Selecting Taget Master", 
                        font=("Impact", 18),
                        fg="white", 
                        bg="black"
                        ).place(x=5, y=5)           
                
        
        self.listSelectingTargets1 = []        
        self.listSelectingTargets_tytul1 = userAlive.dataUserSELECT('terra_scan', str(self.txt_user), "kolumna4", str(choice), 'kolumna1') 

        for insSetToList in self.listSelectingTargets_tytul1:            
            self.listSelectingTargets1.append(str(insSetToList))

        Label(
                        arearea_ramka, 
                        text="Wybierz target",
                        font=("Corbel", 15, "bold"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        ).place(x=5, y=50)


        self.my_listBox1 = Listbox(                            
                        arearea_ramka,                         
                        borderwidth=0, 
                        highlightthickness=0,
                        font=("Corbel", 12, "normal"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        )
        self.my_listBox1.place(x=5, y=84, height=545, width=310)


        for item in self.listSelectingTargets1:
            self.my_listBox1.insert(END, item)
        
        Button(
                arearea_ramka, 
                text="GO TO TARGET",
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
        def move_app(e):                   
            root.geometry(f'+{e.x_root-155}+{e.y_root-690}')

        self.txt_user = txt_user
        self.session = session

        def checkSessions():
            if self.txt_user != self.session:                
                userAlive.exitSys()

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
                text="Target", 
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


    def teleportToPlace(self):
        
        choice = self.my_listBox1.get(ANCHOR) 
        # choice = choice.strip()       
        
        lat = userAlive.dataUserSELECT('terra_scan', str(self.txt_user), "kolumna1", str(choice), 'kolumna2')
        lng = userAlive.dataUserSELECT('terra_scan', str(self.txt_user), "kolumna1", str(choice), 'kolumna3')
        print((choice))
        

        userid = userAlive.dataUserSELECT('users_main', '', 'user', str(self.txt_user), 'identyfikator')
        useridforchanged = userid[0]
        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_y', str(lat[0]), str(useridforchanged))
        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_x', str(lng[0]), str(useridforchanged))
        
        googlePart1 = """https://earth.google.com/web/@"""
        googlePart2 = str(lat[0])
        googlePart3 = ","
        googlePart4 = str(lng[0])
        googlePart5 = """,80.88106533a,3324.79213989d,1y,0h,0t,0r" """
        prepareLinkGoogleE = googlePart1 + googlePart2 + googlePart3 + googlePart4 + googlePart5
        userAlive.goTodo('streethackerbrowser.py -a' + prepareLinkGoogleE)
        userAlive.goTodo('detector3dgoogledron.py')
        userAlive.goTodo('okolica.py')
        userAlive.exitSys()



        

root = tkinter.Tk()
area = Obszar_Roboczy(root, txt_user, session)

root.mainloop()