import userAlive as ua
import tkinter
from tkinter import Label, Frame, Button, Entry, Text, Listbox, END, ANCHOR
from tkinter import messagebox
from PIL import Image, ImageTk
from folium import plugins
import userAlive

txt_user = userAlive.giveUser()
session = userAlive.giveSS()

def checkSessions():
    if txt_user != session:
        userAlive.exitSys()

userAlive.banner(session, "Uruchomiona instancja")
userAlive.sysColorconsole("0", "4", "Uruchomiona instancja")

userAlive.dataUserCREATE6('fav_places', txt_user)
userAlive.dataUserCREATE6("victims_hacked", txt_user)

class Obszar_Roboczy:
    def __init__(self, root, txt_user, session):
        self.root = root
        self.root.title("Street HacKer v 1.001")
        self.root.geometry("340x680+1060+60")
        self.root.resizable(False, False)   
        self.root.overrideredirect(True)  
        self.root.attributes('-alpha', 0.9)
        self.root.wm_attributes('-transparentcolor', '#171717')
        self.txt_user = txt_user
        self.bg=ImageTk.PhotoImage(file="img/phone_main_bg.png")
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        def move_app(e):                   
            root.geometry(f'+{e.x_root-170}+{e.y_root-600}')

        self.txt_user = txt_user
        self.session = session





        #######################################
        #
        # linki do obrazkow
        #
        #######################################        
        self.widgetScreenPhoneMain = ImageTk.PhotoImage(file='img/phone_main_bg_home.png')
        self.widgetScreenMainPhoneOkolica = ImageTk.PhotoImage(file='img/phone_main_bg_teren.png')


        #######################################
        # Root - phone Screen
        ####################################### 
        self.phoneScreen =Frame(self.root, bg="white")        
        self.phoneScreen.place(x=10, y=10, height=660, width=320)

    
        Label(self.phoneScreen, image=self.widgetScreenMainPhoneOkolica).place(x=0, y=0, relwidth=1, relheight=1)
        Label(
            self.phoneScreen, 
            text="AirCrack for WiFi & nets", 
            font=("DejaVu Sans", 12, "bold"),
            fg="white", 
            bg='#505050'
            ).place(x=35, y=42) 

        Label(
            self.phoneScreen, 
            text="Autoryzacja dla < "+str(self.txt_user) + " >", 
            font=("Corbel", 11, "normal"),
            fg="white", 
            bg="#505050", 
            justify="left"
            ).place(x=35, y=65)
        
        self.listSelectingTargets = []
        self.listSelectingTargets_index = set()
        self.listSelectingTargets_tytul = userAlive.dataGeneral('victims_hacked' + self.txt_user, "kolumna1")
        self.listSelectingTargets_kategoria = userAlive.dataGeneral('victims_hacked' + self.txt_user, "kolumna2")
        self.listSelectingTargets_hack = userAlive.dataGeneral('victims_hacked' + self.txt_user, "kolumna3")
        
                
        for post in self.listSelectingTargets_tytul:   
            self.listSelectingTargets_index.add(post)
           
        i = 0
        for insSetToList in self.listSelectingTargets_index:
            if self.listSelectingTargets_kategoria[i] == 'Bluetooth Detector 600V':
                self.listSelectingTargets.append(str(insSetToList))                
            i += 1

        Label(
                        self.phoneScreen, 
                        text="Oznaczone tagety",
                        font=("DejaVu Sans", 8, "normal"),
                        fg="white", 
                        bg="#505050", 
                        justify="left"
                        ).place(x=25, y=95)
        Label(
                        self.phoneScreen, 
                        text="",
                        bg="#404040", 
                        justify="left"
                        ).place(x=25, y=115, height=225, width=272)


        self.my_listBox = Listbox(                            
                        self.phoneScreen,                         
                        borderwidth=0, 
                        highlightthickness=0,
                        font=("Impact", 16, "normal"),
                        fg="#c5ffbb", 
                        bg="#404040", 
                        justify="left"
                        )
        self.my_listBox.place(x=35, y=120, height=220, width=252)


        for item in self.listSelectingTargets:
            self.my_listBox.insert(END, item)
        
        Button(
                self.phoneScreen, 
                text=" ZDALNY DOSTĘP ",
                command=self.getControl,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Arial", 10, "normal"),
                fg="#79ffff", 
                bg="black", 
                justify="left" 
                ).place(x=25, y=345, width=130, height=30) 
        
        Button(
                self.phoneScreen, 
                text=" USUŃ TARGET ",
                command=self.deleteTarget,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Arial", 10, "normal"),
                fg="#79ffff", 
                bg="black", 
                justify="left" 
                ).place(x=168, y=345, width=130, height=30)

        Button(
                self.phoneScreen, 
                text="ZRÓB PAYLOAD",
                # command=self.airCrank,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Arial", 10, "normal"),
                fg="#79ffff", 
                bg="black", 
                justify="left" 
                ).place(x=25, y=380, width=130, height=30) 
        
        Button(
                self.phoneScreen, 
                text="SKASUJ LOGI",
                # command=self.airCrank,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Arial", 10, "normal"),
                fg="#79ffff", 
                bg="black", 
                justify="left" 
                ).place(x=168, y=380, width=130, height=30) 
        
        Button(
                self.phoneScreen, 
                text="REINSTALUJ SYSTEM HACKER",
                # command=self.airCrank,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Arial", 10, "normal"),
                fg="#79ffff", 
                bg="black", 
                justify="left" 
                ).place(x=25, y=420, width=272, height=30) 

        Button(
                self.phoneScreen, 
                text="ZAZNACZ DOM NA MAPIE",
                command=self.addUlubione,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Arial", 10, "normal"),
                fg="#79ffff", 
                bg="black", 
                justify="left" 
                ).place(x=25, y=460, width=272, height=30) 

        Button(
                self.phoneScreen, 
                text="DODAJ ZHACKOWANYCH",
                # command=self.airCrank,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Arial", 10, "normal"),
                fg="#79ffff", 
                bg="black", 
                justify="left" 
                ).place(x=25, y=500, width=272, height=30)
        
        Button(
                self.phoneScreen, 
                text="POZBAW NARZĘDZI",
                # command=self.airCrank,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Arial", 10, "normal"),
                fg="#79ffff", 
                bg="black", 
                justify="left" 
                ).place(x=25, y=540, width=272, height=30)

        #######################################
        #
        # Root/Profill - Ramka MAIN MENU
        #
        #######################################
        checkSessions()
        phoneFooter=Frame(self.root, bg="black")
        phoneFooter.place(x=26, y=587, height=37, width=292)
        phoneFooter.bind("<B1-Motion>", move_app)

        
        Label(
                phoneFooter,
                text="AirCrack for WiFi & nets", 
                fg="#79ffff", 
                bg="black", 
                bd=0, 
                font=("Arial", 9)
                ).place(x=5, y=9, width=135, height=20)
        
        Button(
                phoneFooter,
                command=self.exit,
                text="</> Console", 
                fg="gray", 
                bg="black", 
                bd=0, 
                font=("Arial", 10, "bold")
                ).place(x=200, y=9, width=85, height=20)
   
    def exit(self):
        userAlive.exitSys()

    def deleteTarget(self):
        choice = self.my_listBox.get(ANCHOR)
        Label(self.phoneScreen, text='Target ' + str(choice) + ' został usunięty.', fg="#005c6d", bg="white", bd=0, justify="center", font=("Arial", 8, 'bold')).place(x=35, y=410, height=70, width=250)
        userAlive.dataUserDELETE('victims_hacked', str(self.txt_user), 'kolumna1', str(choice))
        userAlive.goTodo('aircrack.py')
        userAlive.exitSys()

    def getControl(self):
        choice = self.my_listBox.get(ANCHOR)
        vPass = userAlive.dataUserProfil(choice, 'haslo')
        userAlive.goTodo('hacker.py -l "'+str(choice)+'" -p "'+str(vPass)+'"')
        userAlive.exitSys()

    def addUlubione(self):
        choice = self.my_listBox.get(ANCHOR)
        userAlive.dataUserCREATE6('fav_places', self.txt_user)
        
        placesname = userAlive.dataGeneral('fav_places' + self.txt_user, 'kolumna1')
        placesY = userAlive.dataGeneral('fav_places' + self.txt_user, 'kolumna2')
        placesX = userAlive.dataGeneral('fav_places' + self.txt_user, 'kolumna3')
        lokalizacja_dom_y  = userAlive.dataUserProfil(choice, 'lokalizacja_dom_y')
        lokalizacja_dom_x = userAlive.dataUserProfil(choice, 'lokalizacja_dom_x')        
        alreadyEgsit = []
        for i in range(len(placesname)):
                if  lokalizacja_dom_y == placesY[i] and lokalizacja_dom_x == placesX[i]:                        
                        alreadyEgsit.append(placesname[i])
                i += 1        
        lending = len(alreadyEgsit)
        if lending > 0:
                userAlive.czytajTo('Masz już zapisane to miejsce pod nazą: ' + alreadyEgsit[0])
                userAlive.goTodo('aircrack.py')
                root.quit()
        else:
                userAlive.dataUserINSERT6('fav_places', str(self.txt_user), 'HOME: ' + str(choice), str(lokalizacja_dom_y), str(lokalizacja_dom_x), "", "", "")
                print("Miejsce zostało zapisane")
                userAlive.goTodo('aircrack.py')
                root.quit()

root = tkinter.Tk()
area = Obszar_Roboczy(root, txt_user, session)

root.mainloop()