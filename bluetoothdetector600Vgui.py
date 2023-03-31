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
userAlive.dataUserCREATE6("terra_scan", txt_user)
userAlive.dataUserDELETE('terra_scan', txt_user, 'kolumna6', 'del')

class Obszar_Roboczy:
    def __init__(self, root, txt_user, session):
        self.root = root
        self.root.title("Street HacKer v 1.001")
        self.root.geometry("340x680+660+60")
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

        ###############################
        ####
        #### FIREWALL
        ####
        ###############################

        self.licznikKlikow = 0
        self.liczFF = 0

        self.hackUserChoice = {}
        self.hackUserChoice['vpnTurn'] = ('OFF')
        self.hackUserChoice['a1'] = ('NONE')
        self.hackUserChoice['a2'] = ('NONE')
        self.hackUserChoice['a3'] = ('NONE')
        self.hackUserChoice['a4'] = ('NONE')

        self.hackUserChoice['b1'] = ('NONE')
        self.hackUserChoice['b2'] = ('NONE')
        self.hackUserChoice['b3'] = ('NONE')
        self.hackUserChoice['b4'] = ('NONE')

        self.hackUserChoice['c1'] = ('NONE')
        self.hackUserChoice['c2'] = ('NONE')
        self.hackUserChoice['c3'] = ('NONE')
        self.hackUserChoice['c4'] = ('NONE')

        self.hackUserChoice['d1'] = ('NONE')
        self.hackUserChoice['d2'] = ('NONE')
        self.hackUserChoice['d3'] = ('NONE')
        self.hackUserChoice['d4'] = ('NONE')

        # SHOTS
        self.shots = []
        

        # aktualna lokacja
        akl_y = userAlive.dataUserProfil(self.txt_user, 'aktualna_lokalizacja_y')
        akl_x = userAlive.dataUserProfil(self.txt_user, 'aktualna_lokalizacja_x')

        self.list_obecna_loc = [akl_y, akl_x]   

        # lokacja DOM
        akd_y = userAlive.dataUserProfil(self.txt_user, 'lokalizacja_dom_y')
        akd_x = userAlive.dataUserProfil(self.txt_user, 'lokalizacja_dom_x')

        self.lokalizacja_dom = [akd_y, akd_x]

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
            text="Bluetooth Detector 600V", 
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
        self.listSelectingTargets_tytul = userAlive.dataGeneral('selected_targets' + self.txt_user, "kolumna1")
        self.listSelectingTargets_kategoria = userAlive.dataGeneral('selected_targets' + self.txt_user, "kolumna2")
        self.listSelectingTargets_hack = userAlive.dataGeneral('selected_targets' + self.txt_user, "kolumna3")
        
                
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
                        ).place(x=25, y=115, height=325, width=272)


        self.my_listBox = Listbox(                            
                        self.phoneScreen,                         
                        borderwidth=0, 
                        highlightthickness=0,
                        font=("Impact", 16, "normal"),
                        fg="#c5ffbb", 
                        bg="#404040", 
                        justify="left"
                        )
        self.my_listBox.place(x=35, y=120, height=320, width=252)


        for item in self.listSelectingTargets:
            self.my_listBox.insert(END, item)
        
        Button(
                self.phoneScreen, 
                text=" HACKUJ TARGET ",
                command=self.selectedTarget,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Impact", 12, "normal"),
                fg="#79ffff", 
                bg="black", 
                justify="left" 
                ).place(x=25, y=445, width=130, height=30) 
        
        Button(
                self.phoneScreen, 
                text=" USUŃ TARGET ",
                command=self.deleteTarget,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Impact", 12, "normal"),
                fg="#79ffff", 
                bg="black", 
                justify="left" 
                ).place(x=168, y=445, width=130, height=30)

        Button(
                self.phoneScreen, 
                text="AirCrack 4.0.10.203",
                command=self.airCrank,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Impact", 15, "normal"),
                fg="orange", 
                bg="black", 
                justify="left" 
                ).place(x=25, y=484, width=272, height=30) 

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
                text="Bluetooth Detector 600V", 
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
    
    def selectedTarget(self):
        choice = self.my_listBox.get(ANCHOR)
        if choice != "":
            Label(self.phoneScreen, image=self.widgetScreenPhoneMain).place(x=0, y=0, relwidth=1, relheight=1)
            Label(
                self.phoneScreen, 
                text="Bluetooth Detector 600V", 
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

            Label(
                self.phoneScreen, 
                text="Łamanie zapory w maszynie < "+str(choice) + " >", 
                font=("Corbel", 8, "normal"),
                fg="orange", 
                bg="#505050", 
                justify="left"
                ).place(x=35, y=90)

            Label(
                self.phoneScreen,            
                text="TARGET FIREWALL ", 
                fg="white", 
                bg="#666667", 
                bd=0, 
                justify="left",
                font=("Impact", 9)
                ).place(x=35, y=125, height=15)
            
            Label(
                self.phoneScreen,            
                text="TWÓJ FIREWALL ", 
                fg="white", 
                bg="#666667", 
                bd=0, 
                justify="left",
                font=("Impact", 9)
                ).place(x=170, y=125, height=15)
            
            Button(
                    self.phoneScreen,
                    command=self.licznikKlikowPrint,
                    text="Sprawdź konfigurację", 
                    fg="white", 
                    bg="black", 
                    bd=0, 
                    justify="left",
                    font=("Impact", 12)
                    ).place(x=35, y=385, height=25, width=250)

            Button(
                    self.phoneScreen,
                    command=self.exitFirewall,
                    text="ZAMKNIJ     USTAWIENIA", 
                    fg="orange", 
                    bg="black", 
                    bd=0, 
                    justify="left",
                    font=("Impact", 12)
                    ).place(x=35, y=540, height=25, width=250)
            
            
            poka = userAlive.usersFirewall(self.txt_user)
            
            if poka != None:            
                
                a1 = poka[1]
                a2 = poka[2]
                a3 = poka[3]
                a4 = poka[4]

                b1 = poka[5]
                b2 = poka[6]
                b3 = poka[7]
                b4 = poka[8]

                c1 = poka[9]
                c2 = poka[10]
                c3 = poka[11]
                c4 = poka[12]

                d1 = poka[13]
                d2 = poka[14]
                d3 = poka[15]
                d4 = poka[16]

                if a1 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=145, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=145, height=25, width=25)
                if a2 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=175, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=175, height=25, width=25)
                if a3 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=205, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=205, height=25, width=25)
                if a4 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=235, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=235, height=25, width=25)

                if b1 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=145, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=145, height=25, width=25)
                if b2 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=175, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=175, height=25, width=25)
                if b3 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=205, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=205, height=25, width=25)
                if b4 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=235, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=235, height=25, width=25)

                if c1 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=145, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=145, height=25, width=25)
                if c2 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=175, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=175, height=25, width=25)
                if c3 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=205, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=205, height=25, width=25)
                if c4 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=235, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=235, height=25, width=25)

                if d1 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=145, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=145, height=25, width=25)
                if d2 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=175, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=175, height=25, width=25)
                if d3 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=205, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=205, height=25, width=25)
                if d4 == 'ON':
                    Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=235, height=25, width=25)
                else:
                    Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=235, height=25, width=25)

                Button(self.phoneScreen, command=self.a1, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=145, height=25, width=25)
                Button(self.phoneScreen, command=self.a2, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=175, height=25, width=25)
                Button(self.phoneScreen, command=self.a3, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=205, height=25, width=25)
                Button(self.phoneScreen, command=self.a4, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=235, height=25, width=25)

                Button(self.phoneScreen, command=self.b1, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=145, height=25, width=25)
                Button(self.phoneScreen, command=self.b2, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=175, height=25, width=25)
                Button(self.phoneScreen, command=self.b3, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=205, height=25, width=25)
                Button(self.phoneScreen, command=self.b4, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=235, height=25, width=25)

                Button(self.phoneScreen, command=self.c1, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=145, height=25, width=25)
                Button(self.phoneScreen, command=self.c2, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=175, height=25, width=25)
                Button(self.phoneScreen, command=self.c3, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=205, height=25, width=25)
                Button(self.phoneScreen, command=self.c4, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=235, height=25, width=25)

                Button(self.phoneScreen, command=self.d1, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=145, height=25, width=25)
                Button(self.phoneScreen, command=self.d2, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=175, height=25, width=25)
                Button(self.phoneScreen, command=self.d3, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=205, height=25, width=25)
                Button(self.phoneScreen, command=self.d4, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=235, height=25, width=25)

                Label(
                    self.phoneScreen,            
                    text="HACK -V-P-N-", 
                    fg="white", 
                    bg="#8d8b8b", 
                    bd=0, 
                    justify="left",
                    font=("Impact", 9)
                    ).place(x=35, y=275, height=15)
                
                Label(self.phoneScreen, text="", fg="black", bg="#242424", bd=0, justify="left", font=("Arial", 9)).place(x=45, y=295, height=60, width=225)
                Button(self.phoneScreen, command=self.vpnOff, text="OFF", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 13)).place(x=55, y=300, height=50, width=100)
                Button(self.phoneScreen, command=self.vpnOn, text="ON", fg="#b4fffa", bg="#8d8b8b", bd=0, justify="left", font=("Arial", 13)).place(x=165, y=300, height=50, width=100)
                Label(self.phoneScreen, text="Hack VPN is off line", fg="red", bg="#9d9d9d", bd=0, justify="left", font=("Arial", 9)).place(x=100, y=355)
            
            

    def exitFirewall(self):
        userAlive.goTodo('bluetoothdetector600Vgui.py')
        userAlive.exitSys()

    
        
    def a1(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.a1n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=145, height=25, width=25)
            self.hackUserChoice['a1'] = ('ON')
            self.licznikKlikow += 1
    def a1n(self):
        Button(self.phoneScreen, command=self.a1z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=145, height=25, width=25)
        self.hackUserChoice['a1'] = ('OFF')
        self.liczFF += 1
    def a1z(self):
        Button(self.phoneScreen, command=self.a1, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=145, height=25, width=25)
        self.hackUserChoice['a1'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1
    
    def a2(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.a2n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=175, height=25, width=25)
            self.hackUserChoice['a2'] = ('ON')
            self.licznikKlikow += 1
    def a2n(self):
        Button(self.phoneScreen, command=self.a2z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=175, height=25, width=25)
        self.hackUserChoice['a2'] = ('OFF')
        self.liczFF += 1
    def a2z(self):
        Button(self.phoneScreen, command=self.a2, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=175, height=25, width=25)
        self.hackUserChoice['a2'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1

    def a3(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.a3n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=205, height=25, width=25)
            self.hackUserChoice['a3'] = ('ON')
            self.licznikKlikow += 1
    def a3n(self):
        Button(self.phoneScreen, command=self.a3z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=205, height=25, width=25)
        self.hackUserChoice['a3'] = ('OFF')
        self.liczFF += 1
    def a3z(self):
        Button(self.phoneScreen, command=self.a3, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=205, height=25, width=25)
        self.hackUserChoice['a3'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1
       
    def a4(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.a4n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=235, height=25, width=25)
            self.hackUserChoice['a4'] = ('ON')
            self.licznikKlikow += 1
    def a4n(self):
        Button(self.phoneScreen, command=self.a4z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=235, height=25, width=25)
        self.hackUserChoice['a4'] = ('OFF')
        self.liczFF += 1
    def a4z(self):
        Button(self.phoneScreen, command=self.a4, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=235, height=25, width=25)
        self.hackUserChoice['a4'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1

    def b1(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.b1n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=145, height=25, width=25)
            self.hackUserChoice['b1'] = ('ON')
            self.licznikKlikow += 1
    def b1n(self):
        Button(self.phoneScreen, command=self.b1z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=145, height=25, width=25)
        self.hackUserChoice['b1'] = ('OFF')
        self.liczFF += 1
    def b1z(self):
        Button(self.phoneScreen, command=self.b1, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=145, height=25, width=25)
        self.hackUserChoice['b1'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1

    def b2(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.b2n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=175, height=25, width=25)
            self.hackUserChoice['b2'] = ('ON')
            self.licznikKlikow += 1
    def b2n(self):
        Button(self.phoneScreen, command=self.b2z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=175, height=25, width=25)
        self.hackUserChoice['b2'] = ('OFF')
        self.liczFF += 1
    def b2z(self):
        Button(self.phoneScreen, command=self.b2, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=175, height=25, width=25)
        self.hackUserChoice['b2'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1

    def b3(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.b3n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=205, height=25, width=25)
            self.hackUserChoice['b3'] = ('ON')
            self.licznikKlikow += 1
    def b3n(self):
        Button(self.phoneScreen, command=self.b3z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=205, height=25, width=25)
        self.hackUserChoice['b3'] = ('OFF')
        self.liczFF += 1
    def b3z(self):
        Button(self.phoneScreen, command=self.b3, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=205, height=25, width=25)
        self.hackUserChoice['b3'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1

    def b4(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.b4n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=235, height=25, width=25)
            self.hackUserChoice['b4'] = ('ON')
            self.licznikKlikow += 1
    def b4n(self):
        Button(self.phoneScreen, command=self.b4z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=235, height=25, width=25)
        self.hackUserChoice['b4'] = ('OFF')
        self.liczFF += 1
    def b4z(self):
        Button(self.phoneScreen, command=self.b4, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=65, y=235, height=25, width=25)
        self.hackUserChoice['b4'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1
    
    def c1(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.c1n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=145, height=25, width=25)
            self.hackUserChoice['c1'] = ('ON')
            self.licznikKlikow += 1
    def c1n(self):
        Button(self.phoneScreen, command=self.c1z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=145, height=25, width=25)
        self.hackUserChoice['c1'] = ('OFF')
        self.liczFF += 1
    def c1z(self):
        Button(self.phoneScreen, command=self.c1, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=145, height=25, width=25)
        self.hackUserChoice['c1'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1

    def c2(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.c2n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=175, height=25, width=25)
            self.hackUserChoice['c2'] = ('ON')
            self.licznikKlikow += 1
    def c2n(self):
        Button(self.phoneScreen, command=self.c2z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=175, height=25, width=25)
        self.hackUserChoice['c2'] = ('OFF')
        self.liczFF += 1
    def c2z(self):
        Button(self.phoneScreen, command=self.c2, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=175, height=25, width=25)
        self.hackUserChoice['c2'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1

    def c3(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.c3n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=205, height=25, width=25)
            self.hackUserChoice['c3'] = ('ON')
            self.licznikKlikow += 1
    def c3n(self):
        Button(self.phoneScreen, command=self.c3z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=205, height=25, width=25)
        self.hackUserChoice['c3'] = ('OFF')
        self.liczFF += 1
    def c3z(self):
        Button(self.phoneScreen, command=self.c3, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=205, height=25, width=25)
        self.hackUserChoice['c3'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1

    def c4(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.c4n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=235, height=25, width=25)
            self.hackUserChoice['c4'] = ('ON')
            self.licznikKlikow += 1
    def c4n(self):
        Button(self.phoneScreen, command=self.c4z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=235, height=25, width=25)
        self.hackUserChoice['c4'] = ('OFF')
        self.liczFF += 1
    def c4z(self):
        Button(self.phoneScreen, command=self.c4, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=95, y=235, height=25, width=25)
        self.hackUserChoice['c4'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1

    def d1(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.d1n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=145, height=25, width=25)
            self.hackUserChoice['d1'] = ('ON')
            self.licznikKlikow += 1
    def d1n(self):
        Button(self.phoneScreen, command=self.d1z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=145, height=25, width=25)
        self.hackUserChoice['d1'] = ('OFF')
        self.liczFF += 1
    def d1z(self):
        Button(self.phoneScreen, command=self.d1, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=145, height=25, width=25)
        self.hackUserChoice['d1'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1

    def d2(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.d2n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=175, height=25, width=25)
            self.hackUserChoice['d2'] = ('ON')
            self.licznikKlikow += 1
    def d2n(self):
        Button(self.phoneScreen, command=self.d2z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=175, height=25, width=25)
        self.hackUserChoice['d2'] = ('OFF')
        self.liczFF += 1
    def d2z(self):
        Button(self.phoneScreen, command=self.d2, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=175, height=25, width=25)
        self.hackUserChoice['d2'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1

    def d3(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.d3n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=205, height=25, width=25)
            self.hackUserChoice['d3'] = ('ON')
            self.licznikKlikow += 1
    def d3n(self):
        Button(self.phoneScreen, command=self.d3z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=205, height=25, width=25)
        self.hackUserChoice['d3'] = ('OFF')
        self.liczFF += 1
    def d3z(self):
        Button(self.phoneScreen, command=self.d3, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=205, height=25, width=25)
        self.hackUserChoice['d3'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1

    def d4(self):
        if self.licznikKlikow < 5:
            Button(self.phoneScreen, command=self.d4n, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=235, height=25, width=25)
            self.hackUserChoice['d4'] = ('ON')
            self.licznikKlikow += 1
    def d4n(self):
        Button(self.phoneScreen, command=self.d4z, text="FF", fg="black", bg="white", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=235, height=25, width=25)
        self.hackUserChoice['d4'] = ('OFF')
        self.liczFF += 1
    def d4z(self):
        Button(self.phoneScreen, command=self.d4, text="??", fg="#b4fffa", bg="gray", bd=0, justify="left", font=("Arial", 9)).place(x=125, y=235, height=25, width=25)
        self.hackUserChoice['d4'] = ('NONE')
        self.licznikKlikow -= 1
        self.liczFF -= 1

    def licznikKlikowPrint(self):
        choice = self.my_listBox.get(ANCHOR)
        if choice != "":
            zoba = userAlive.usersFirewall(choice)
            if zoba == None:
                wynikAtaku = 'User ' + ' < '  + str(choice)+ ' > nie posiada zapory'
                Label(self.phoneScreen, text=str(wynikAtaku), fg="green", bg="#9d9d9d", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=430, width=260)
                Button(
                    self.phoneScreen,
                    command=self.getControl,
                    text="</> PRZEJMIJ MASZYNĘ", 
                    fg="#b4fffa", 
                    bg="black", 
                    bd=0, 
                    justify="left",
                    font=("Arial", 10)
                    ).place(x=35, y=465, height=60, width=250)

            else:
                wynikAtaku = ''
                wynikSuccess = 0
                if self.licznikKlikow == 5:
                    if self.liczFF != 0:
                        if self.hackUserChoice['vpnTurn'] == zoba[0] :                         
                            if self.hackUserChoice['a1'] == 'NONE':
                                pass
                            else:
                                if self.hackUserChoice['a1'] == zoba[1]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'

                            if self.hackUserChoice['a2'] == 'NONE':
                                pass
                            else:
                                if self.hackUserChoice['a2'] == zoba[2]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'
                            
                            if self.hackUserChoice['a3'] == 'NONE':
                                pass
                            else:
                                if self.hackUserChoice['a3'] == zoba[3]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'
                            
                            if self.hackUserChoice['a4'] == 'NONE':
                                pass
                            else:
                                if self.hackUserChoice['a4'] == zoba[4]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'
                            if self.hackUserChoice['b1'] == 'NONE':
                                pass
                            else:
                                if self.hackUserChoice['b1'] == zoba[5]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'
                            if self.hackUserChoice['b2'] == 'NONE':
                                pass
                            else:
                                if self.hackUserChoice['b2'] == zoba[6]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'
                            if self.hackUserChoice['b3'] == 'NONE':
                                pass
                            else:
                                if self.hackUserChoice['b3'] == zoba[7]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'
                            if self.hackUserChoice['b4'] == 'NONE':
                                pass
                            else:
                                if self.hackUserChoice['b4'] == zoba[8]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'
                            if self.hackUserChoice['c1'] == 'NONE':
                                pass
                            else:
                                if self.hackUserChoice['c1'] == zoba[9]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'                            
                            if self.hackUserChoice['c2'] == 'NONE':
                                pass
                            else:
                                if self.hackUserChoice['c2'] == zoba[10]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'
                            if self.hackUserChoice['c3'] == 'NONE':
                                pass
                            else:
                                if self.hackUserChoice['c3'] == zoba[11]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'
                            if self.hackUserChoice['c4'] == 'NONE':
                                pass
                            else:
                                if self.hackUserChoice['c4'] == zoba[12]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'
                            if self.hackUserChoice['d1'] == 'NONE':
                                pass                        
                            else:
                                if self.hackUserChoice['d1'] == zoba[13]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'
                            if self.hackUserChoice['d2'] == 'NONE':
                                pass
                            else:
                                if self.hackUserChoice['d2'] == zoba[14]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'
                            if self.hackUserChoice['d3'] == 'NONE':
                                pass
                            else:
                                if self.hackUserChoice['d3'] == zoba[15]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'
                            if self.hackUserChoice['d4'] == 'NONE':
                                pass                                
                            else:
                                if self.hackUserChoice['d4'] == zoba[16]:
                                    wynikSuccess += 1
                                else:
                                    wynikAtaku ='Ustawienia firewall nieprawidłowe'                           
                        else:
                            wynikAtaku ='Ustawienia firewall nieprawidłowe'
                    else:
                        wynikAtaku ='Przynajmniej jeden bit musi mieć wartość FF'
                else:
                    wynikAtaku = 'Musisz zaznaczyć 5 bitów'            
                Label(self.phoneScreen, text=str(wynikAtaku), fg="red", bg="#9d9d9d", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=430, width=260)
                if wynikSuccess != 0:
                    if wynikSuccess == 5:
                        Label(self.phoneScreen, text='Przełamałeś zabezpieczenia firewall', fg="green", bg="#9d9d9d", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=430, width=260)
                        wynikAtaku = 'User ' + ' < '  + str(choice)+ ' > nie posiada zapory'
                        Label(self.phoneScreen, text=str(wynikAtaku), fg="green", bg="#9d9d9d", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=430, width=260)
                        Button(
                            self.phoneScreen,
                            command=self.getControl,
                            text="</> PRZEJMIJ MASZYNĘ", 
                            fg="#b4fffa", 
                            bg="black", 
                            bd=0, 
                            justify="left",
                            font=("Arial", 10)
                            ).place(x=35, y=465, height=60, width=250)
                    else:
                        Label(self.phoneScreen, text='Ustawienia firewall nieprawidłowe', fg="red", bg="#9d9d9d", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=430, width=260)               
                        
                self.shots = userAlive.autoOfensive(self.txt_user)                
                if self.shots != None:
                    a1 = self.shots[1]
                    a2 = self.shots[2]
                    a3 = self.shots[3]
                    a4 = self.shots[4]

                    b1 = self.shots[5]
                    b2 = self.shots[6]
                    b3 = self.shots[7]
                    b4 = self.shots[8]

                    c1 = self.shots[9]
                    c2 = self.shots[10]
                    c3 = self.shots[11]
                    c4 = self.shots[12]

                    d1 = self.shots[13]
                    d2 = self.shots[14]
                    d3 = self.shots[15]
                    d4 = self.shots[16]

                    akcja = int(self.shots[17])                    
                    Label(self.phoneScreen, text='Hack values key: ' + str(int(wynikSuccess * akcja ** (0.5))), fg="black", bg="#9d9d9d", bd=0, justify="left", font=("Arial", 9)).place(x=35, y=410, width=260)                     
                    if a1 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=145, height=25, width=25)
                    elif a1 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=145, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=145, height=25, width=25)

                    if a2 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=175, height=25, width=25)
                    elif a2 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=175, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=175, height=25, width=25)

                    if a3 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=205, height=25, width=25)
                    elif a3 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=205, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=205, height=25, width=25)

                    if a4 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=235, height=25, width=25)
                    elif a4 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=235, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=170, y=235, height=25, width=25)

                    if b1 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=145, height=25, width=25)
                    elif b1 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=145, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=145, height=25, width=25)

                    if b2 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=175, height=25, width=25)
                    if b2 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=175, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=175, height=25, width=25)

                    if b3 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=205, height=25, width=25)
                    elif b3 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=205, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=205, height=25, width=25)

                    if b4 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=235, height=25, width=25)
                    elif b4 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=235, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=200, y=235, height=25, width=25)

                    if c1 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=145, height=25, width=25)
                    elif c1 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=145, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=145, height=25, width=25)

                    if c2 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=175, height=25, width=25)
                    elif c2 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=175, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=175, height=25, width=25)

                    if c3 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=205, height=25, width=25)
                    elif c3 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=205, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=205, height=25, width=25)

                    if c4 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=235, height=25, width=25)
                    elif c4 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=235, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=230, y=235, height=25, width=25)

                    if d1 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=145, height=25, width=25)
                    elif d1 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=145, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=145, height=25, width=25)

                    if d2 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=175, height=25, width=25)
                    elif d2 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=175, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=175, height=25, width=25)

                    if d3 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=205, height=25, width=25)
                    elif d3 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=205, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=205, height=25, width=25)

                    if d4 == 'ON':
                        Label(self.phoneScreen, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=235, height=25, width=25)
                    elif d4 == 'SHOT':
                        Label(self.phoneScreen, text="XX", fg="#b4fffa", bg="red", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=235, height=25, width=25)
                    else:
                        Label(self.phoneScreen, text="FF", fg="#b4fffa", bg="green", bd=0, justify="left", font=("Arial", 9)).place(x=260, y=235, height=25, width=25)
                    
                    losAkcja = userAlive.mixer(4,6)
                    if self.shots[17] == losAkcja:
                        Label(self.phoneScreen, text="!! Security Allarm !!", fg="white", bg="red", bd=0, justify="left", font=("Arial", 10, 'bold')).place(x=35, y=380, height=30, width=250)
                        uwaga = 'UWAGA !! \nZostałeś wykryty i straciłeś \nznaczik telefonu < ' + choice + ' > \n( JESTEŚ WIDOCZY )'
                        Label(self.phoneScreen, text=str(uwaga), fg="#005c6d", bg="white", bd=0, justify="center", font=("Arial", 8, 'bold')).place(x=35, y=410, height=70, width=250)
                        Button(
                            self.phoneScreen,
                            command=self.uwagaAdd,
                            text="Maskuj swoją aktywność!", 
                            fg="#deff00", 
                            bg="#005c6d", 
                            bd=0, 
                            justify="left",
                            font=("Impact", 12)
                            ).place(x=35, y=490, height=45, width=250)

                        Label(self.phoneScreen, text="", fg="#005c6d", bg="#8d8b8b", bd=0, justify="center", font=("Arial", 8, 'bold')).place(x=35, y=535, height=40, width=250)

                        userAlive.dataUserDELETE('selected_targets', str(self.txt_user), 'kolumna1', str(choice))

    def deleteTarget(self):
        choice = self.my_listBox.get(ANCHOR)
        Label(self.phoneScreen, text='Target ' + str(choice) + ' został usunięty.', fg="#005c6d", bg="white", bd=0, justify="center", font=("Arial", 8, 'bold')).place(x=35, y=410, height=70, width=250)
        userAlive.dataUserDELETE('selected_targets', str(self.txt_user), 'kolumna1', str(choice))
        userAlive.goTodo('bluetoothdetector600Vgui.py')
        userAlive.exitSys()

    def airCrank(self):
        userAlive.goTodo('aircrack.py')
        userAlive.exitSys()


    def uwagaAdd(self):
        choice = self.my_listBox.get(ANCHOR)
        if choice != "":

            userAlive.writeSS(self.txt_user)
            userAlive.sendUser(self.txt_user)
            
            userid = userAlive.dataUserSELECT('users_main', '', 'user', str(choice), 'identyfikator')
            useridforchanged = userid[0]                        
            attack_failds = userAlive.dataUserProfil(self.txt_user, 'attack_failds')

            try:
                attack_failds = int(attack_failds)                           
            except:
                attack_failds = 0

            attack_failds += 1                                               

            userAlive.dataUserUPDATE('users_main', '', 'attack_failds', str(attack_failds), str(useridforchanged))
            losWoz = userAlive.mixer(0, 121)
            if losWoz > 30:
                userAlive.sysColorconsole('9', '6')
                userAlive.dataUserCREATE6("selected_targets", choice)
                userAlive.dataUserINSERT6('selected_targets', str(choice), str(self.txt_user), 'Bluetooth Detector 600V', 'Re Hacked FireWall', "", "", "")
                userAlive.checking_bar('Maskowanie aktywności zakończone [niepowodzeniem] ' + self.txt_user, 100, 0.01)
                userAlive.goTodo('bluetoothdetector600Vgui.py')
                userAlive.exitSys()
            else:
                userAlive.sysColorconsole('9', '0')
                userAlive.checking_bar('Maskowanie aktywności zakończone [sukcesem] ' + self.txt_user, 100, 0.01)
                userAlive.goTodo('bluetoothdetector600Vgui.py')
                userAlive.exitSys()

            

    def getControl(self):
        choice = self.my_listBox.get(ANCHOR)
        if choice != "":
            userAlive.writeSS(txt_user)
            userAlive.sendUser(txt_user)
            userAlive.sysColorconsole('0', 'B')

            userid = userAlive.dataUserSELECT('users_main', '', 'user', txt_user, 'identyfikator')
            useridforchanged = userid[0]
            poziom = userAlive.dataUserProfil(txt_user, 'aktualny_poziom')
            pktDos = userAlive.dataUserProfil(txt_user, 'punkty_doswiadczenia')
            vcoins = userAlive.dataUserProfil(txt_user, 'aktualne_vcoin')
            attack_failds = userAlive.dataUserProfil(txt_user, 'attack_failds')
            attack_success = userAlive.dataUserProfil(txt_user, 'attack_success')        

            try:
                attack_failds = int(attack_failds)
                attack_success = int(attack_success)
            except:
                attack_failds = 0
                attack_success = 0
            poziom = int(poziom)

            vcoins = float(vcoins)

            pktDos = int(pktDos)

            mnoznik = userAlive.mixer(5, 50)
            zysk = mnoznik
            dos = (zysk + mnoznik) * 100
            
            print("Uruchamianie Bluetooth Detector 600V")
            print()
            print('Zdobyłeś kolejny trzy poziomy')
            print("To hackowanie dało Ci zarobić: V$" + str(zysk))
            print("Twoje doświadczenie zwiększa się o " + str(dos))
            userAlive.checking_bar('Zapisywanie wyniku ' + choice, 100, 0.1)

            attack_failds += 1
            attack_success += 1
            przychod = zysk + vcoins
            dosUp = dos + pktDos
            poziomUp = poziom + 3

            userAlive.dataUserUPDATE('users_main', '', 'attack_success', str(attack_success), str(useridforchanged))
            userAlive.dataUserUPDATE('users_main', '', 'aktualne_vcoin', str(przychod), str(useridforchanged))
            userAlive.dataUserUPDATE('users_main', '', 'punkty_doswiadczenia', str(dosUp), str(useridforchanged))
            userAlive.dataUserUPDATE('users_main', '', 'aktualny_poziom', str(poziomUp), str(useridforchanged))

            userAlive.dataUserCREATE6('victims_hacked', str(self.txt_user))
            userAlive.dataUserINSERT6('victims_hacked', str(self.txt_user), str(choice), 'Bluetooth Detector 600V', '', '', '', '')
            
            userAlive.dataUserDELETE('selected_targets', str(self.txt_user), 'kolumna1', str(choice))

            userAlive.goTodo('bluetoothdetector600Vgui.py')            
            userAlive.goTodo('aircrack.py')
            userAlive.exitSys()


    def vpnOff(self):
        Label(self.phoneScreen, text="", fg="black", bg="#242424", bd=0, justify="left", font=("Arial", 9)).place(x=45, y=295, height=60, width=225)
        Button(self.phoneScreen, command=self.vpnOff, text="OFF", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 13)).place(x=55, y=300, height=50, width=100)
        Button(self.phoneScreen, command=self.vpnOn, text="ON", fg="#b4fffa", bg="#8d8b8b", bd=0, justify="left", font=("Arial", 13)).place(x=165, y=300, height=50, width=100)
        Label(self.phoneScreen, text="Hack VPN is off line ", fg="red", bg="#9d9d9d", bd=0, justify="left", font=("Arial", 9)).place(x=100, y=355)
        self.hackUserChoice['vpnTurn'] = ('OFF')

    def vpnOn(self):
        Label(self.phoneScreen, text="", fg="black", bg="#242424", bd=0, justify="left", font=("Arial", 9)).place(x=45, y=295, height=60, width=225)
        Button(self.phoneScreen, command=self.vpnOff, text="OFF", fg="#b4fffa", bg="#8d8b8b", bd=0, justify="left", font=("Arial", 13)).place(x=55, y=300, height=50, width=100)
        Button(self.phoneScreen, command=self.vpnOn, text="ON", fg="#b4fffa", bg="black", bd=0, justify="left", font=("Arial", 13)).place(x=165, y=300, height=50, width=100)
        Label(self.phoneScreen, text="Hack VPN is on line ", fg="green", bg="#9d9d9d", bd=0, justify="left", font=("Arial", 9)).place(x=100, y=355)
        self.hackUserChoice['vpnTurn'] = ('ON')

root = tkinter.Tk()
area = Obszar_Roboczy(root, txt_user, session)

root.mainloop()