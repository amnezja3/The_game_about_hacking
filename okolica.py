import tkinter
from tkinter import Label, Frame, Button, Entry, Text
from tkinter import messagebox
from PIL import Image, ImageTk

from time import sleep

from tkhtmlview import HTMLLabel
import folium
from folium import plugins
import userAlive

txt_user = userAlive.giveUser()
session = userAlive.giveSS()

def checkSessions():
    if txt_user != session:
        userAlive.exitSys()

userAlive.banner(session, "Uruchomiona instancja")
userAlive.sysColorconsole("0", "4", "Uruchomiona instancja")

userAlive.dataUserCREATE6('fav_places', str(txt_user))
userAlive.dataUserCREATE6("terra_scan", str(txt_user))
userAlive.dataUserDELETE('terra_scan', str(txt_user), 'kolumna6', 'del')

class Obszar_Roboczy:
    def __init__(self, root, txt_user, session):
        self.root = root
        self.root.title("Street HacKer v 1.001")
        self.root.geometry("480x320+620+20")
        self.root.resizable(False, False)   
        self.root.overrideredirect(True)  
        # self.root.attributes('-alpha', 0.9)
        self.txt_user = txt_user
        self.bg=ImageTk.PhotoImage(file="img/main_logoff.png")
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        def move_app(e):                   
            root.geometry(f'+{e.x_root-260}+{e.y_root-300}')

        self.txt_user = txt_user
        self.session = session       
                

        sca1 = userAlive.scanningTerra('bankomat', 250, userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_y' ), userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_x' ))
        sca2 = userAlive.scanningTerra('poczta', 250, userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_y' ), userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_x' ))
        sca3 = userAlive.scanningTerra('urząd', 250, userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_y' ), userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_x' ))
        sca4 = userAlive.scanningTerra('hotel', 250, userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_y' ), userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_x' ))
        sca5 = userAlive.scanningTerra('restauracja', 250, userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_y' ), userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_x'))
        sca6 = userAlive.scanningTerra('firma', 250, userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_y' ), userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_x' ))
        sca7 = userAlive.scanningTerra('usługi', 250, userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_y' ), userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_x' ))
        sca8 = userAlive.scanningTerra('sklep', 250, userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_y' ), userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_x' ))
        sca9 = userAlive.scanningTerra('policja', 250, userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_y' ), userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_x' ))

        self.otherPlayers = userAlive.detectOterHacker(str(self.txt_user))
        
        self.bankomat = len(sca1)
        self.poczta = len(sca2)
        self.urzad = len(sca3)
        self.hotel = len(sca4)
        self.restauracja = len(sca5)
        self.firma = len(sca6)
        self.uslugi = len(sca7)
        self.sklep = len(sca8)
        self.policja = len(sca9)
        

        empty = {0:'empty'}
        
        if sca1 == empty and sca2 == empty and sca3 == empty and sca4 == empty and sca5 == empty and sca6 == empty and sca7 == empty and sca8 == empty and sca9 == empty:
            self.bankomat = 0
            self.poczta = 0
            self.urzad = 0
            self.hotel = 0
            self.restauracja = 0
            self.firma = 0
            self.uslugi = 0
            self.sklep = 0
            self.policja = 0
        else:            
            a = 0
            if sca1 != empty:
                for i in range(self.bankomat):
                        dane = sca1[i]
                        y = userAlive.dotLocation(str(dane[a]))
                        x = userAlive.dotLocation(str(dane[a+1]))
                        userAlive.dataUserINSERT6('terra_scan', str(self.txt_user), str(dane[int(a+2)]), str(y), str(x), 'bankomat', '', 'del')
                        i += 1
            if sca2 != empty:
                for i in range(self.poczta):
                        dane = sca2[i]                
                        y = userAlive.dotLocation(str(dane[a]))
                        x = userAlive.dotLocation(str(dane[a+1]))
                        userAlive.dataUserINSERT6('terra_scan', str(self.txt_user), str(dane[a+2]), str(y), str(x), 'poczta', '', 'del')                
                        i += 1
            if sca3 != empty:
                for i in range(self.urzad):
                        dane = sca3[i]                
                        y = userAlive.dotLocation(str(dane[a]))
                        x = userAlive.dotLocation(str(dane[a+1]))
                        userAlive.dataUserINSERT6('terra_scan', str(self.txt_user), str(dane[a+2]), str(y), str(x), 'urzad', '', 'del')
                        i += 1
            if sca4 != empty:
                for i in range(self.hotel):
                        dane = sca4[i]                
                        y = userAlive.dotLocation(str(dane[a]))
                        x = userAlive.dotLocation(str(dane[a+1]))
                        userAlive.dataUserINSERT6('terra_scan', str(self.txt_user), str(dane[a+2]), str(y), str(x), 'hotel', '', 'del')
                        i += 1
            if sca5 != empty:
                for i in range(self.restauracja):
                        dane = sca5[i]                
                        y = userAlive.dotLocation(str(dane[a]))
                        x = userAlive.dotLocation(str(dane[a+1]))
                        userAlive.dataUserINSERT6('terra_scan', str(self.txt_user), str(dane[a+2]), str(y), str(x), 'restauracja', '', 'del')
                        i += 1
            if sca6 != empty:
                for i in range(self.firma):
                        dane = sca6[i]                
                        y = userAlive.dotLocation(str(dane[a]))
                        x = userAlive.dotLocation(str(dane[a+1]))
                        userAlive.dataUserINSERT6('terra_scan', str(self.txt_user), str(dane[a+2]), str(y), str(x), 'firma', '', 'del')
                        i += 1
            if sca7 != empty:
                for i in range(self.uslugi):
                        dane = sca7[i]                
                        y = userAlive.dotLocation(str(dane[a]))
                        x = userAlive.dotLocation(str(dane[a+1]))
                        userAlive.dataUserINSERT6('terra_scan', str(self.txt_user), str(dane[a+2]), str(y), str(x), 'uslugi', '', 'del')
                        i += 1
            if sca8 != empty:
                for i in range(self.sklep):
                        dane = sca8[i]                
                        y = userAlive.dotLocation(str(dane[a]))
                        x = userAlive.dotLocation(str(dane[a+1]))
                        userAlive.dataUserINSERT6('terra_scan', str(self.txt_user), str(dane[a+2]), str(y), str(x), 'sklep', '', 'del')
                        i += 1
            if sca9 != empty:
                for i in range(self.policja):
                        dane = sca9[i]                
                        y = userAlive.dotLocation(str(dane[a]))
                        x = userAlive.dotLocation(str(dane[a+1]))
                        userAlive.dataUserINSERT6('terra_scan', str(self.txt_user), str(dane[a+2]), str(y), str(x), 'policja', '', 'del')
                        i += 1
        
        #######################################
        #
        # linki do obrazkow
        #
        #######################################
        self.widget_screen_main = ImageTk.PhotoImage(file='img/area_main_logoff.png')
        self.widget_screen_main_okolica = ImageTk.PhotoImage(file='img/area_main_okolica0.png')
        self.widget_screen_main_dom = ImageTk.PhotoImage(file='img/area_main_dom0.png')
        self.widget_screen_main_adept = ImageTk.PhotoImage(file='img/area_main_login_adept.png')
        self.widget_screen_main_idz_do_lokacji = ImageTk.PhotoImage(file='img/area_main_idz_do_lokacji.png')

        #######################################
        # Root/ - LOKACJE
        #######################################
        # 
        # USTAWIENIA MAPY   
        # AB     
        self.punkt_AB_Y = userAlive.dataUserProfil(str(self.txt_user), 'lokalizacja_terenu_a_y')
        self.punkt_AB_X = userAlive.dataUserProfil(str(self.txt_user), 'lokalizacja_terenu_a_x')
        self.punktAB = [self.punkt_AB_Y, self.punkt_AB_X]
        # DA
        self.punkt_DA_Y = userAlive.dataUserProfil(str(self.txt_user), 'lokalizacja_terenu_b_y')
        self.punkt_DA_X = userAlive.dataUserProfil(str(self.txt_user), 'lokalizacja_terenu_b_x')
        self.punktDA = [self.punkt_DA_Y, self.punkt_DA_X]
        # CB
        self.punkt_CB_Y = userAlive.dataUserProfil(str(self.txt_user), 'lokalizacja_terenu_c_y')
        self.punkt_CB_X = userAlive.dataUserProfil(str(self.txt_user), 'lokalizacja_terenu_c_x')
        self.punktCB = [self.punkt_CB_Y, self.punkt_CB_X]
        # DC
        self.punkt_DC_Y = userAlive.dataUserProfil(str(self.txt_user), 'lokalizacja_terenu_d_y')
        self.punkt_DC_X = userAlive.dataUserProfil(str(self.txt_user), 'lokalizacja_terenu_d_x')
        self.punktDC = [self.punkt_DC_Y, self.punkt_DC_X]

        self.lista_Y = [self.punkt_AB_Y, self.punkt_DA_Y, self.punkt_CB_Y, self.punkt_DC_Y]
        self.lista_X = [self.punkt_AB_X, self.punkt_DA_X, self.punkt_CB_X, self.punkt_DC_X]

        # USTAWIENIA ZAPISANYCH MIEJSC
        # TARGET
                

        self.zapisaneY = userAlive.dataGeneral('fav_places'+ str(self.txt_user), "kolumna2")
        self.zapisaneX = userAlive.dataGeneral('fav_places'+ str(self.txt_user), "kolumna3")      
        

        

        # aktualna lokacja
        akl_y = userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_y')
        akl_x = userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_x')

        self.list_obecna_loc = [akl_y, akl_x]   

        # lokacja DOM
        akd_y = userAlive.dataUserProfil(self.txt_user, 'lokalizacja_dom_y')
        akd_x = userAlive.dataUserProfil(str(self.txt_user), 'lokalizacja_dom_x')

        self.lokalizacja_dom = [akd_y, akd_x]


       
        #######################################
        # Root/Okolica - Ramka Area
        ####################################### 
        area_ramka=Frame(self.root, bg="white")
        area_ramka.place(x=10, y=10, height=285, width=460)
        
        

        # w domu
        if self.list_obecna_loc[0] == self.lokalizacja_dom[0] and self.list_obecna_loc[1] == self.lokalizacja_dom[1]:
            Label(area_ramka, image=self.widget_screen_main_dom).place(x=0, y=0, relwidth=1, relheight=1)
            Label(
                area_ramka, 
                text="Dom  ", 
                font=("Impact", 45, "normal"),
                fg="white", 
                bg="black"
                ).place(x=5, y=5) 
            Label(
                area_ramka, 
                text="Witaj w domu "+str(self.txt_user), 
                font=("Corbel", 14, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=5, y=80)
            
        # poza domem                           
        else:
            Label(area_ramka, image=self.widget_screen_main_okolica).place(x=0, y=0, relwidth=1, relheight=1)
            Label(
                        area_ramka, 
                        text=" ",
                        font=("Corbel", 10, "normal"),
                        fg="white", 
                        bg="black",                 
                        justify="left"
                        ).place(x=5, y=8, height=125, width=325)

            Label(
                    area_ramka, 
                    text="Okolica ", 
                    font=("Impact", 45, "normal"),
                    fg="white", 
                    bg="black"
                    ).place(x=5, y=5) 
            Label(
                    area_ramka, 
                    text="Uważaj na siebie "+str(self.txt_user)+" bo jesteś poza domem.", 
                    font=("Corbel", 8, "normal"),
                    fg="#b4ff1a", 
                    bg="black", 
                    justify="left"
                    ).place(x=5, y=80)   
            

            Label(
                    area_ramka, 
                    text="Teren zeskanowany", 
                    font=("Corbel", 9, "bold"),
                    fg="#8aef06", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=5)

            Label(
                    area_ramka, 
                    text="Bankomaty:  ( "+str(self.bankomat)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#9aee2c", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=20) 

            Label(
                    area_ramka, 
                    text="Poczt: ( "+str(self.poczta)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#a5ef43", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=35) 
            Label(
                    area_ramka, 
                    text="Urzędów: ( "+str(self.urzad)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#adee58", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=50) 
            Label(
                    area_ramka, 
                    text="Hoteli: ( "+str(self.hotel)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#b4ff1a", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=65) 
            Label(
                    area_ramka, 
                    text="Restauracji: ( "+str(self.restauracja)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#b5ef68", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=80) 
            Label(
                    area_ramka, 
                    text="Firm: ( "+str(self.firma)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#beef7e", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=95) 

            Label(
                    area_ramka, 
                    text="Dostawców usług: ( "+str(self.uslugi)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#c5f18c", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=95)
            Label(
                    area_ramka, 
                    text="Sklepów: ( "+str(self.sklep)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#d1f5a1", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=110)

            Label(
                    area_ramka, 
                    text="( "+str(self.policja)+" )   komisariatów Policji w tej okolicy.", 
                    font=("Corbel", 8, "normal"),
                    fg="orange", 
                    bg="black", 
                    justify="left"
                    ).place(x=5, y=95)
            if len(self.otherPlayers) > 0:
                Label(
                        area_ramka, 
                        text="( "+str(len(self.otherPlayers))+" )   aktywności hackerów.", 
                        font=("Corbel", 8, "normal"),
                        fg="green", 
                        bg="black", 
                        justify="left"
                        ).place(x=5, y=110)
            else:
                Label(
                        area_ramka, 
                        text="( "+str(len(self.otherPlayers))+" )   aktywności hackerów.", 
                        font=("Corbel", 8, "normal"),
                        fg="red", 
                        bg="black", 
                        justify="left"
                        ).place(x=5, y=110)

            Button(
                area_ramka,
                command=self.backHome,
                text="</>WRÓĆ DO DOMU ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=310, y=215, height=15)        

            Button(
                area_ramka,
                command=self.setHome,
                text="</>USTAW TU DOM ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=10, y=235, height=15)


        Label(
                area_ramka, 
                text=" ",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black",                 
                justify="left"
                ).place(x=338, y=8, height=112, width=115)

        Label(
                area_ramka, 
                text="Historia ruchów",
                font=("Corbel", 10, "normal"),
                fg="gray", 
                bg="black",                 
                justify="left"
                ).place(x=340, y=8) 

        Button(area_ramka, 
                command = self.hista,
                text=" "+ str(self.punkt_AB_Y) + " / " + " "+ str(self.punkt_AB_X), 
                font=("Corbel", 8, "normal"),                
                fg="#aaa9aa", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=30)
        
        Button(area_ramka, 
                command = self.histb,
                text=" "+ str(self.punkt_DA_Y) + " / " + " "+ str(self.punkt_DA_X), 
                font=("Corbel", 8, "normal"),                
                fg="#646364", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=53)

        Button(area_ramka, 
                command = self.histc,
                text=" "+ str(self.punkt_CB_Y) + " / " + " "+ str(self.punkt_CB_X), 
                font=("Corbel", 8, "normal"),                
                fg="#4a494a", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=76)

        Button(area_ramka, 
                command = self.histd,
                text=" "+ str(self.punkt_DC_Y) + " / " + " "+ str(self.punkt_DC_X), 
                font=("Corbel", 8, "normal"),                
                fg="#222222", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=99)


        Label(
                area_ramka, 
                text="Twoja obecna lokalizacja ",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black",                 
                justify="left"
                ).place(x=5, y=135)  
        loc_pozycja = 165
        for kolejna_loc in self.list_obecna_loc:
            Label(
                area_ramka, 
                text=str(kolejna_loc),
                font=("Corbel", 11, "normal"),
                fg="#03ff21", 
                bg="black", 
                justify="left"
                ).place(x=10, y=loc_pozycja)
            loc_pozycja += 20        
        Button(
                area_ramka,
                command=self.link_mapa,
                text="</>MAPA ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=110, y=165, height=15)
        Button(
                area_ramka,
                command=self.idzDoLokacji,
                text="</>IDŹ ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=110, y=185, height=15)
        Button(
                area_ramka,
                command=self.savePlace,
                text="</>ZAPISZ TO MIEJSCE ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=10, y=215, height=15)
             

        Label(
                area_ramka, 
                text="Lokalizacja domu",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=305, y=135)
        dom_pozycja = 165
        for xy_dom in self.lokalizacja_dom:
            Label(
                    area_ramka, 
                    text=str(xy_dom),
                    font=("Corbel", 11, "normal"),
                    fg="#03ff21", 
                    bg="black", 
                    justify="left"
                    ).place(x=310, y=dom_pozycja)
            dom_pozycja += 20
        
        
        

        #######################################
        #
        # Root/Profill - Ramka MAIN MENU
        #
        #######################################
        checkSessions()
        menu_main=Frame(self.root, bg="black")
        menu_main.place(x=6, y=273, height=37, width=468)
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
                text="Okolica", 
                fg="#79ffff", 
                bg="black", 
                bd=0, 
                font=("Arial", 10)
                ).place(x=60, y=9, width=45, height=20)
        
        Button(
                menu_main,
                command=self.exit,
                text="</> Console", 
                fg="gray", 
                bg="black", 
                bd=0, 
                font=("Arial", 10, "bold")
                ).place(x=375, y=9, width=85, height=20)













    def link_mapa(self):        
        ######################################
        #Root/Okolica - Ramka Area
        ###################################### 
        area_ramka=Frame(self.root, bg="white")
        area_ramka.place(x=10, y=10, height=285, width=460)
        # w domu
        if self.list_obecna_loc[0] == self.lokalizacja_dom[0] and self.list_obecna_loc[1] == self.lokalizacja_dom[1]:
            Label(area_ramka, image=self.widget_screen_main_dom).place(x=0, y=0, relwidth=1, relheight=1)
            Label(
                area_ramka, 
                text="Dom  ", 
                font=("Impact", 45, "normal"),
                fg="white", 
                bg="black"
                ).place(x=5, y=5) 
            Label(
                area_ramka, 
                text="Witaj w domu "+str(self.txt_user), 
                font=("Corbel", 14, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=5, y=80)
           
            
        # poza domem                           
        else:
            Label(area_ramka, image=self.widget_screen_main_okolica).place(x=0, y=0, relwidth=1, relheight=1)
            Label(
                        area_ramka, 
                        text=" ",
                        font=("Corbel", 10, "normal"),
                        fg="white", 
                        bg="black",                 
                        justify="left"
                        ).place(x=5, y=8, height=125, width=325)

            Label(
                    area_ramka, 
                    text="Okolica ", 
                    font=("Impact", 45, "normal"),
                    fg="white", 
                    bg="black"
                    ).place(x=5, y=5) 
            Label(
                    area_ramka, 
                    text="Uważaj na siebie "+str(self.txt_user)+" bo jesteś poza domem.", 
                    font=("Corbel", 8, "normal"),
                    fg="#b4ff1a", 
                    bg="black", 
                    justify="left"
                    ).place(x=5, y=80)   
            

            Label(
                    area_ramka, 
                    text="Teren zeskanowany", 
                    font=("Corbel", 9, "bold"),
                    fg="#8aef06", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=5)

            Label(
                    area_ramka, 
                    text="Bankomaty:  ( "+str(self.bankomat)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#9aee2c", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=20) 

            Label(
                    area_ramka, 
                    text="Poczt: ( "+str(self.poczta)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#a5ef43", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=35) 
            Label(
                    area_ramka, 
                    text="Urzędów: ( "+str(self.urzad)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#adee58", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=50) 
            Label(
                    area_ramka, 
                    text="Hoteli: ( "+str(self.hotel)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#b4ff1a", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=65) 
            Label(
                    area_ramka, 
                    text="Restauracji: ( "+str(self.restauracja)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#b5ef68", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=80) 
            Label(
                    area_ramka, 
                    text="Firm: ( "+str(self.firma)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#beef7e", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=95) 

            Label(
                    area_ramka, 
                    text="Dostawców usług: ( "+str(self.uslugi)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#c5f18c", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=95)
            Label(
                    area_ramka, 
                    text="Sklepów: ( "+str(self.sklep)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#d1f5a1", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=110)

            Label(
                    area_ramka, 
                    text="( "+str(self.policja)+" )   komisariatów Policji w tej okolicy.", 
                    font=("Corbel", 8, "normal"),
                    fg="orange", 
                    bg="black", 
                    justify="left"
                    ).place(x=5, y=95)
            if len(self.otherPlayers) > 0:
                Label(
                        area_ramka, 
                        text="( "+str(len(self.otherPlayers))+" )   aktywności hackerów.", 
                        font=("Corbel", 8, "normal"),
                        fg="green", 
                        bg="black", 
                        justify="left"
                        ).place(x=5, y=110)
            else:
                Label(
                        area_ramka, 
                        text="( "+str(len(self.otherPlayers))+" )   aktywności hackerów.", 
                        font=("Corbel", 8, "normal"),
                        fg="red", 
                        bg="black", 
                        justify="left"
                        ).place(x=5, y=110)

            Button(
                area_ramka,
                command=self.backHome,
                text="</>WRÓĆ DO DOMU ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=310, y=215, height=15)        

            Button(
                area_ramka,
                command=self.setHome,
                text="</>USTAW TU DOM ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=10, y=235, height=15)

        Label(
                area_ramka, 
                text=" ",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black",                 
                justify="left"
                ).place(x=338, y=8, height=112, width=115)

        Label(
                area_ramka, 
                text="Historia ruchów",
                font=("Corbel", 10, "normal"),
                fg="gray", 
                bg="black",                 
                justify="left"
                ).place(x=340, y=8) 

        Button(area_ramka, 
                command = self.hista,
                text=" "+ str(self.punkt_AB_Y) + " / " + " "+ str(self.punkt_AB_X), 
                font=("Corbel", 8, "normal"),                
                fg="#aaa9aa", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=30)
        
        Button(area_ramka, 
                command = self.histb,
                text=" "+ str(self.punkt_DA_Y) + " / " + " "+ str(self.punkt_DA_X), 
                font=("Corbel", 8, "normal"),                
                fg="#646364", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=53)

        Button(area_ramka, 
                command = self.histc,
                text=" "+ str(self.punkt_CB_Y) + " / " + " "+ str(self.punkt_CB_X), 
                font=("Corbel", 8, "normal"),                
                fg="#4a494a", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=76)

        Button(area_ramka, 
                command = self.histd,
                text=" "+ str(self.punkt_DC_Y) + " / " + " "+ str(self.punkt_DC_X), 
                font=("Corbel", 8, "normal"),                
                fg="#222222", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=99)



        Label(
                area_ramka, 
                text="Twoja obecna lokalizacja ",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=5, y=135)  
        loc_pozycja = 165
        for kolejna_loc in self.list_obecna_loc:
            Label(
                area_ramka, 
                text=str(kolejna_loc),
                font=("Corbel", 11, "normal"),
                fg="#03ff21", 
                bg="black", 
                justify="left"
                ).place(x=10, y=loc_pozycja)
            loc_pozycja += 20        
        Button(
                area_ramka,
                command=self.link_mapa,
                text="</>MAPA ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=110, y=165, height=15)
        
        Button(
                area_ramka,
                command=self.goMap,
                text="</>HACKER MAP ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=160, y=165, height=15)

        Button(
                area_ramka,
                command=self.goGooDron,
                text="</>GOOGLE DRON ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=160, y=185, height=15)
        

        Button(
                area_ramka,
                command=self.idzDoLokacji,
                text="</>IDŹ ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=110, y=185, height=15)
        Button(
                area_ramka,
                command=self.savePlace,
                text="</>ZAPISZ TO MIEJSCE ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=10, y=215, height=15)

        Label(
                area_ramka, 
                text="Lokalizacja domu",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=305, y=135)
        dom_pozycja = 165
        for xy_dom in self.lokalizacja_dom:
            Label(
                    area_ramka, 
                    text=str(xy_dom),
                    font=("Corbel", 11, "normal"),
                    fg="#03ff21", 
                    bg="black", 
                    justify="left"
                    ).place(x=310, y=dom_pozycja)
            dom_pozycja += 20        

        #######################################
        #
        # Root/Profill - Ramka MAIN MENU
        #
        #######################################
        def move_app(e):                   
            root.geometry(f'+{e.x_root-260}+{e.y_root-300}')
        checkSessions()
        menu_main=Frame(self.root, bg="black")
        menu_main.place(x=6, y=273, height=37, width=468)
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
                text="Okolica", 
                fg="#79ffff", 
                bg="black", 
                bd=0, 
                font=("Arial", 10)
                ).place(x=60, y=9, width=45, height=20)
        
        Button(
                menu_main,
                command=self.exit,
                text="</> Console", 
                fg="gray", 
                bg="black", 
                bd=0, 
                font=("Arial", 10, "bold")
                ).place(x=375, y=9, width=85, height=20)      
        
        zapisaneY = self.zapisaneY
        zapisaneX = self.zapisaneX

        check = userAlive.dataGeneral('fav_places' + str(self.txt_user), 'kolumna1')
        if check != None:
            yourLocation = userAlive.dataGeneral('fav_places' + str(self.txt_user), 'kolumna1')
        else:
            yourLocation = "DOM"
        yourLocation1 = "Poprzednia lokalizacja"
        yourLocation2 = "Najwcześniejsze położenie"
        yourLocation3 = "Wcześniejsze połozenie"
        yourLocation4 = "Ostatnie połozenie"
        yourLocation5 = "OBECNA LOKALIZACJA"
        yourLocation6 = "DOM"
        if zapisaneY != None and zapisaneX != None:
            lat = zapisaneY
            lng = zapisaneX
        else:
            lat = self.lokalizacja_dom[0]
            lng = self.lokalizacja_dom[1]

        lat1 = self.punkt_AB_Y
        lng1 = self.punkt_AB_X

        lat2 = self.punkt_DA_Y
        lng2 = self.punkt_DA_X

        lat3 = self.punkt_CB_Y
        lng3 = self.punkt_CB_X

        lat4 = self.punkt_DC_Y
        lng4 = self.punkt_DC_X

        lat5 = self.list_obecna_loc[0]
        lng5 = self.list_obecna_loc[1]

        lat6 = self.lokalizacja_dom[0]
        lng6 = self.lokalizacja_dom[1]

        myMap = folium.Map(location = [lat5, lng5], zoom_start = 16, titles='CartoDB Dark_Matter')

        level = userAlive.dataUserProfil(str(txt_user),'aktualny_poziom')
        level = int(level)
        try:
            for i in range(len(lat)):
                folium.CircleMarker([lat[i], lng[i]], popup=str(yourLocation[i]), color='#a300ac', fill_color='#a300ac').add_to((myMap))
        except:
            pass
        folium.CircleMarker([lat1, lng1], popup=yourLocation1, color='#30302f', fill_color='#30302f').add_to((myMap))
        folium.CircleMarker([lat2, lng2], popup=yourLocation2, color='#525252', fill_color='#525252').add_to((myMap))
        folium.CircleMarker([lat3, lng3], popup=yourLocation3, color='#7c7c7c', fill_color='#7c7c7c').add_to((myMap))
        folium.CircleMarker([lat4, lng4], popup=yourLocation4, color='#9c9f9f', fill_color='#9c9f9f').add_to((myMap))
        folium.Marker([lat5, lng5], popup=yourLocation5, color='#000000', fill_color='#111111').add_to((myMap))
        folium.CircleMarker([lat6, lng6], popup=yourLocation6, color='#24ff00', fill_color='#24ff00').add_to((myMap))

        
        folium.Circle(radius = level * 15, location=[lat5, lng5], color='green').add_to(myMap)
        
        folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(myMap)
        # folium.raster_layers.TileLayer('Stamen Terrain').add_to(myMap)
        # folium.raster_layers.TileLayer('Open Street Map').add_to(myMap)
        # folium.LayerControl().add_to(myMap)

        
        myMap.add_child(folium.LatLngPopup())



        # save map
        myMap.save("map_"+ self.txt_user +".html")
        
    def goMap(self):
        
        prepareHackerMap= "file:///map_" + str(self.txt_user) + ".html"

        userAlive.goTodo('StreetHackerBrowser.py -a ' + prepareHackerMap)
        

    def goGooDron(self):
        
        lat5 = self.list_obecna_loc[0]
        lng5 = self.list_obecna_loc[1]

        googlePart1 = """https://earth.google.com/web/@"""
        googlePart2 = str(lat5)
        googlePart3 = ","
        googlePart4 = str(lng5)
        googlePart5 = """,80.88106533a,3324.79213989d,1y,0h,0t,0r"""

        prepareLinkGoogleE = googlePart1 + googlePart2 + googlePart3 + googlePart4 + googlePart5

        userAlive.goTodo('StreetHackerBrowser.py -a ' + prepareLinkGoogleE)
        userAlive.goTodo('detector3dgoogledron.py')



       
        






    def idzDoLokacji(self):
        ######################################
        #Root/Okolica - Ramka Area
        ###################################### 
        area_ramka=Frame(self.root, bg="white")
        area_ramka.place(x=10, y=10, height=285, width=460)
        # w domu
        if self.list_obecna_loc[0] == self.lokalizacja_dom[0] and self.list_obecna_loc[1] == self.lokalizacja_dom[1]:
            Label(area_ramka, image=self.widget_screen_main_dom).place(x=0, y=0, relwidth=1, relheight=1)
            Label(
                area_ramka, 
                text="Dom  ", 
                font=("Impact", 45, "normal"),
                fg="white", 
                bg="black"
                ).place(x=5, y=5) 
            Label(
                area_ramka, 
                text="Witaj w domu "+str(self.txt_user), 
                font=("Corbel", 14, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=5, y=80)
           
            
        # poza domem                           
        else:
            Label(area_ramka, image=self.widget_screen_main_okolica).place(x=0, y=0, relwidth=1, relheight=1)
            Label(
                        area_ramka, 
                        text=" ",
                        font=("Corbel", 10, "normal"),
                        fg="white", 
                        bg="black",                 
                        justify="left"
                        ).place(x=5, y=8, height=125, width=325)

            Label(
                    area_ramka, 
                    text="Okolica ", 
                    font=("Impact", 45, "normal"),
                    fg="white", 
                    bg="black"
                    ).place(x=5, y=5) 
            Label(
                    area_ramka, 
                    text="Uważaj na siebie "+str(self.txt_user)+" bo jesteś poza domem.", 
                    font=("Corbel", 8, "normal"),
                    fg="#b4ff1a", 
                    bg="black", 
                    justify="left"
                    ).place(x=5, y=80)   
            

            Label(
                    area_ramka, 
                    text="Teren zeskanowany", 
                    font=("Corbel", 9, "bold"),
                    fg="#8aef06", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=5)

            Label(
                    area_ramka, 
                    text="Bankomaty:  ( "+str(self.bankomat)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#9aee2c", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=20) 

            Label(
                    area_ramka, 
                    text="Poczt: ( "+str(self.poczta)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#a5ef43", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=35) 
            Label(
                    area_ramka, 
                    text="Urzędów: ( "+str(self.urzad)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#adee58", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=50) 
            Label(
                    area_ramka, 
                    text="Hoteli: ( "+str(self.hotel)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#b4ff1a", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=65) 
            Label(
                    area_ramka, 
                    text="Restauracji: ( "+str(self.restauracja)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#b5ef68", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=80) 
            Label(
                    area_ramka, 
                    text="Firm: ( "+str(self.firma)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#beef7e", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=95) 

            Label(
                    area_ramka, 
                    text="Dostawców usług: ( "+str(self.uslugi)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#c5f18c", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=95)
            Label(
                    area_ramka, 
                    text="Sklepów: ( "+str(self.sklep)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#d1f5a1", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=110)

            Label(
                    area_ramka, 
                    text="( "+str(self.policja)+" )   komisariatów Policji w tej okolicy.", 
                    font=("Corbel", 8, "normal"),
                    fg="orange", 
                    bg="black", 
                    justify="left"
                    ).place(x=5, y=95)

            if len(self.otherPlayers) > 0:
                Label(
                        area_ramka, 
                        text="( "+str(len(self.otherPlayers))+" )   aktywności hackerów.", 
                        font=("Corbel", 8, "normal"),
                        fg="green", 
                        bg="black", 
                        justify="left"
                        ).place(x=5, y=110)
            else:
                Label(
                        area_ramka, 
                        text="( "+str(len(self.otherPlayers))+" )   aktywności hackerów.", 
                        font=("Corbel", 8, "normal"),
                        fg="red", 
                        bg="black", 
                        justify="left"
                        ).place(x=5, y=110)

            Button(
                area_ramka,
                command=self.backHome,
                text="</>WRÓĆ DO DOMU ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=310, y=215, height=15)        

            Button(
                area_ramka,
                command=self.setHome,
                text="</>USTAW TU DOM ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=10, y=235, height=15)

        Label(
                area_ramka, 
                text=" ",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black",                 
                justify="left"
                ).place(x=338, y=8, height=112, width=115)

        Label(
                area_ramka, 
                text="Historia ruchów",
                font=("Corbel", 10, "normal"),
                fg="gray", 
                bg="black",                 
                justify="left"
                ).place(x=340, y=8) 

        Button(area_ramka, 
                command = self.hista,
                text=" "+ str(self.punkt_AB_Y) + " / " + " "+ str(self.punkt_AB_X), 
                font=("Corbel", 8, "normal"),                
                fg="#aaa9aa", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=30)
        
        Button(area_ramka, 
                command = self.histb,
                text=" "+ str(self.punkt_DA_Y) + " / " + " "+ str(self.punkt_DA_X), 
                font=("Corbel", 8, "normal"),                
                fg="#646364", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=53)

        Button(area_ramka, 
                command = self.histc,
                text=" "+ str(self.punkt_CB_Y) + " / " + " "+ str(self.punkt_CB_X), 
                font=("Corbel", 8, "normal"),                
                fg="#4a494a", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=76)

        Button(area_ramka, 
                command = self.histd,
                text=" "+ str(self.punkt_DC_Y) + " / " + " "+ str(self.punkt_DC_X), 
                font=("Corbel", 8, "normal"),                
                fg="#222222", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=99)

        Label(
                area_ramka, 
                text="Twoja obecna lokalizacja ",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=5, y=135)  
        loc_pozycja = 165
        for kolejna_loc in self.list_obecna_loc:
            Label(
                area_ramka, 
                text=str(kolejna_loc),
                font=("Corbel", 11, "normal"),
                fg="#03ff21", 
                bg="black", 
                justify="left"
                ).place(x=10, y=loc_pozycja)
            loc_pozycja += 20        
        Button(
                area_ramka,
                command=self.link_mapa,
                text="</>MAPA ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=110, y=165, height=15)
        Button(
                area_ramka,
                command=self.idzDoLokacji,
                text="</>IDŹ ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=110, y=185, height=15)
        Button(
                area_ramka,
                command=self.savePlace,
                text="</>ZAPISZ TO MIEJSCE ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=10, y=215, height=15)

        Label(
                area_ramka, 
                text="Lokalizacja domu",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=305, y=135)
        dom_pozycja = 165
        for xy_dom in self.lokalizacja_dom:
            Label(
                    area_ramka, 
                    text=str(xy_dom),
                    font=("Corbel", 11, "normal"),
                    fg="#03ff21", 
                    bg="black", 
                    justify="left"
                    ).place(x=310, y=dom_pozycja)
            dom_pozycja += 20
       
        ###############################
        # lokacje

        Label(
                area_ramka, 
                text="Wprowadź współrzedne   \n\n\n\n\n\n\n",
                font=("Corbel", 8, "normal"),
                fg="orange", 
                bg="black", 
                justify="left"
                ).place(x=170, y=135)

        Label(
                area_ramka, 
                text="W/E",
                font=("Corbel", 6, "normal"),
                fg="#1eff00", 
                bg="black", 
                justify="left"
                ).place(x=180, y=169)   
        
        Label(
                area_ramka, 
                text="N/S",
                font=("Corbel", 6, "normal"),
                fg="#1eff00", 
                bg="black", 
                justify="left"
                ).place(x=180, y=154)

        Label(
                area_ramka, 
                text=" . ",
                font=("Corbel", 18, "normal"),
                fg="#1eff00", 
                bg="black", 
                justify="left"
                ).place(x=222, y=158)

        Label(
                area_ramka, 
                text=" . ",
                font=("Corbel", 18, "normal"),
                fg="#1eff00", 
                bg="black", 
                justify="left"
                ).place(x=222, y=140)

        Label(
                area_ramka, 
                text="Wprowadź współrzedne   ",
                font=("Corbel", 8, "normal"),
                fg="orange", 
                bg="black", 
                justify="left"
                ).place(x=170, y=135)
        
        # ##############################
        # # podaj lokacje

        self.wspC_Y = Entry(
                area_ramka,                 
                font=("Arial", 7, "normal"), 
                fg="#1eff00", bg="black"
                )
        self.wspC_Y.place(x=205, y=155, width=20, height=12)

        self.wspD_Y = Entry(
                area_ramka,                 
                font=("Arial", 7, "normal"), 
                fg="#1eff00", bg="black"
                )
        self.wspD_Y.place(x=242, y=155, width=35, height=12)

        self.wspC_X = Entry(
                area_ramka,                 
                font=("Arial", 7, "normal"), 
                fg="#1eff00", bg="black"
                )
        self.wspC_X.place(x=205, y=170, width=20, height=12)

        self.wspD_X = Entry(
                area_ramka,                 
                font=("Arial", 7, "normal"), 
                fg="#1eff00", bg="black"
                )
        self.wspD_X.place(x=242, y=170, width=35, height=12)

        Button(
                area_ramka,
                command=self.getLocation,
                text=" GET FROM MAP ", 
                fg="#b4fffa", 
                bg="#121212", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=174, y=187, height=15, width=115)

        Button(
                area_ramka,
                command=self.sprawdzLokacje,
                text=" CHECK ", 
                fg="#b4fffa", 
                bg="#121212",
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=173, y=207, height=15, width=55)

        Button(
                area_ramka,
                command=self.teleportTo,
                text=" GO ", 
                fg="#b4fffa", 
                bg="#121212", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=233, y=207, height=15, width=55)
        
        Button(
                area_ramka,
                command=self.openPlace,
                text=" OPEN SAVED ", 
                fg="#b4fffa", 
                bg="#121212", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=174, y=227, height=15, width=115)
        #######################################
        #
        # Root/Profill - Ramka MAIN MENU
        #
        #######################################
        def move_app(e):                   
            root.geometry(f'+{e.x_root-260}+{e.y_root-300}')
        checkSessions()
        menu_main=Frame(self.root, bg="black")
        menu_main.place(x=6, y=273, height=37, width=468)
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
                text="Okolica", 
                fg="#79ffff", 
                bg="black", 
                bd=0, 
                font=("Arial", 10)
                ).place(x=60, y=9, width=45, height=20)
        
        Button(
                menu_main,
                command=self.exit,
                text="</> Console", 
                fg="gray", 
                bg="black", 
                bd=0, 
                font=("Arial", 10, "bold")
                ).place(x=375, y=9, width=85, height=20) 
        






    def sprawdzLokacje(self):        
        cy = self.wspC_Y.get()
        dy = self.wspD_Y.get()
        cx =self.wspC_X.get()
        dx = self.wspD_X.get()

        wspxy = [len(cy), len(dy), len(cx), len(dx)] 
        
        try:
            int(cy)
            int(dy)
            int(cx)
            int(dx)
            cyfry = True
        except:
            userAlive.mowTo("hey Sily, be focus on the moment! Did You put Wrong data. ")
            cyfry = False
        if cyfry == True:
            if int(wspxy[0]) < 5 and int(wspxy[2]) < 5 and int(wspxy[1]) > 5 and int(wspxy[3]) > 5: # 
                if int(cy) < 90 and int(cx) < 180 and int(cy) > -90 and int(cx) > -180:
                        miny = dy[0:6]
                        minx = dx[0:6]
                        
                        poblocY = str(cy) + "." + str(miny)
                        poblocX = str(cx) + "." + str(minx)
                        
                        googlePart1 = """https://earth.google.com/web/@"""
                        googlePart2 = str(poblocY)
                        googlePart3 = ","
                        googlePart4 = str(poblocX)
                        googlePart5 = """,80.88106533a,3324.79213989d,1y,0h,0t,0r" """
                        prepareLinkGoogleE = googlePart1 + googlePart2 + googlePart3 + googlePart4 + googlePart5
                        userAlive.goTodo('StreetHackerBrowser.py -a ' + prepareLinkGoogleE)
                        userAlive.goTodo('detector3dgoogledron.py')
                else:
                    userAlive.czytajTo("Podane dane są nieprawidłowe. Nie ma takich współrzednych geograficznych.")
                    userAlive.mowTo("hey Sily, be focus on the moment! Did You put Wrong data. ")
            else:
                userAlive.czytajTo("Podane dane są niekompletne")
                userAlive.mowTo("hey Sily, be focus on the moment! Did You put Wrong data. ")
        else: 
            userAlive.czytajTo("GeoError! ")
            userAlive.mowTo("Idiot ")






    def openPlace(self):
        userAlive.goTodo('miejsca.py')
        root.quit()






    def savePlace(self):
        #######################################
        # Root/Okolica - Ramka Area
        ####################################### 
        area_ramka=Frame(self.root, bg="white")
        area_ramka.place(x=10, y=10, height=285, width=460)
        # w domu
        if self.list_obecna_loc[0] == self.lokalizacja_dom[0] and self.list_obecna_loc[1] == self.lokalizacja_dom[1]:
            Label(area_ramka, image=self.widget_screen_main_dom).place(x=0, y=0, relwidth=1, relheight=1)
            Label(
                area_ramka, 
                text="Dom  ", 
                font=("Impact", 45, "normal"),
                fg="white", 
                bg="black"
                ).place(x=5, y=5) 
            Label(
                area_ramka, 
                text="Witaj w domu "+str(self.txt_user), 
                font=("Corbel", 14, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=5, y=80)         
           
            
        # poza domem                           
        else:
            Label(area_ramka, image=self.widget_screen_main_okolica).place(x=0, y=0, relwidth=1, relheight=1)
            Label(
                        area_ramka, 
                        text=" ",
                        font=("Corbel", 10, "normal"),
                        fg="white", 
                        bg="black",                 
                        justify="left"
                        ).place(x=5, y=8, height=125, width=325)

            Label(
                    area_ramka, 
                    text="Okolica ", 
                    font=("Impact", 45, "normal"),
                    fg="white", 
                    bg="black"
                    ).place(x=5, y=5) 
            Label(
                    area_ramka, 
                    text="Uważaj na siebie "+str(self.txt_user)+" bo jesteś poza domem.", 
                    font=("Corbel", 8, "normal"),
                    fg="#b4ff1a", 
                    bg="black", 
                    justify="left"
                    ).place(x=5, y=80)   
            

            Label(
                    area_ramka, 
                    text="Teren zeskanowany", 
                    font=("Corbel", 9, "bold"),
                    fg="#8aef06", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=5)

            Label(
                    area_ramka, 
                    text="Bankomaty:  ( "+str(self.bankomat)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#9aee2c", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=20) 

            Label(
                    area_ramka, 
                    text="Poczt: ( "+str(self.poczta)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#a5ef43", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=35) 
            Label(
                    area_ramka, 
                    text="Urzędów: ( "+str(self.urzad)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#adee58", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=50) 
            Label(
                    area_ramka, 
                    text="Hoteli: ( "+str(self.hotel)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#b4ff1a", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=65) 
            Label(
                    area_ramka, 
                    text="Restauracji: ( "+str(self.restauracja)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#b5ef68", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=80) 
            Label(
                    area_ramka, 
                    text="Firm: ( "+str(self.firma)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#beef7e", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=95) 

            Label(
                    area_ramka, 
                    text="Dostawców usług: ( "+str(self.uslugi)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#c5f18c", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=95)
            Label(
                    area_ramka, 
                    text="Sklepów: ( "+str(self.sklep)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#d1f5a1", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=110)

            Label(
                    area_ramka, 
                    text="( "+str(self.policja)+" )   komisariatów Policji w tej okolicy.", 
                    font=("Corbel", 8, "normal"),
                    fg="orange", 
                    bg="black", 
                    justify="left"
                    ).place(x=5, y=95)

            if len(self.otherPlayers) > 0:
                Label(
                        area_ramka, 
                        text="( "+str(len(self.otherPlayers))+" )   aktywności hackerów.", 
                        font=("Corbel", 8, "normal"),
                        fg="green", 
                        bg="black", 
                        justify="left"
                        ).place(x=5, y=110)
            else:
                Label(
                        area_ramka, 
                        text="( "+str(len(self.otherPlayers))+" )   aktywności hackerów.", 
                        font=("Corbel", 8, "normal"),
                        fg="red", 
                        bg="black", 
                        justify="left"
                        ).place(x=5, y=110)

            Button(
                area_ramka,
                command=self.backHome,
                text="</>WRÓĆ DO DOMU ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=310, y=215, height=15)  

        Label(
                area_ramka, 
                text=" ",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black",                 
                justify="left"
                ).place(x=338, y=8, height=112, width=115)

        Label(
                area_ramka, 
                text="Historia ruchów",
                font=("Corbel", 10, "normal"),
                fg="gray", 
                bg="black",                 
                justify="left"
                ).place(x=340, y=8) 

        Button(area_ramka, 
                command = self.hista,
                text=" "+ str(self.punkt_AB_Y) + " / " + " "+ str(self.punkt_AB_X), 
                font=("Corbel", 8, "normal"),                
                fg="#aaa9aa", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=30)
        
        Button(area_ramka, 
                command = self.histb,
                text=" "+ str(self.punkt_DA_Y) + " / " + " "+ str(self.punkt_DA_X), 
                font=("Corbel", 8, "normal"),                
                fg="#646364", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=53)

        Button(area_ramka, 
                command = self.histc,
                text=" "+ str(self.punkt_CB_Y) + " / " + " "+ str(self.punkt_CB_X), 
                font=("Corbel", 8, "normal"),                
                fg="#4a494a", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=76)

        Button(area_ramka, 
                command = self.histd,
                text=" "+ str(self.punkt_DC_Y) + " / " + " "+ str(self.punkt_DC_X), 
                font=("Corbel", 8, "normal"),                
                fg="#222222", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=99)

        Label(
                area_ramka, 
                text="Twoja obecna lokalizacja ",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=5, y=135)  
        loc_pozycja = 165
        for kolejna_loc in self.list_obecna_loc:
            Label(
                area_ramka, 
                text=str(kolejna_loc),
                font=("Corbel", 11, "normal"),
                fg="#03ff21", 
                bg="black", 
                justify="left"
                ).place(x=10, y=loc_pozycja)
            loc_pozycja += 20        
        Button(
                area_ramka,
                command=self.link_mapa,
                text="</>MAPA ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=110, y=165, height=15)
        Button(
                area_ramka,
                command=self.idzDoLokacji,
                text="</>IDŹ ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=110, y=185, height=15)
        
        Label(
                area_ramka, 
                text="Wprowadź nazwę dla tego miejsca ",
                font=("Corbel", 8, "normal"),
                fg="orange", 
                bg="black", 
                justify="left"
                ).place(x=10, y=211)
        
        self.saveName = Entry(
                area_ramka,                 
                font=("Arial", 10, "normal"), 
                fg="#1eff00", bg="black"
                )
        self.saveName.place(x=10, y=231, width=160, height=15)
        
        Button(
                area_ramka,
                command=self.addUlubione,
                text="<!>ZATWIERDŹ NAZWĘ ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 6)
                ).place(x=75, y=248, height=15)
       
        Label(
                area_ramka, 
                text="Lokalizacja domu",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=305, y=135)
        dom_pozycja = 165
        for xy_dom in self.lokalizacja_dom:
            Label(
                    area_ramka, 
                    text=str(xy_dom),
                    font=("Corbel", 11, "normal"),
                    fg="#03ff21", 
                    bg="black", 
                    justify="left"
                    ).place(x=310, y=dom_pozycja)
            dom_pozycja += 20
        
        
        #######################################
        #
        # Root/Profill - Ramka MAIN MENU
        #
        #######################################
        def move_app(e):                   
            root.geometry(f'+{e.x_root-260}+{e.y_root-300}')
        checkSessions()
        menu_main=Frame(self.root, bg="black")
        menu_main.place(x=6, y=273, height=37, width=468)
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
                text="Okolica", 
                fg="#79ffff", 
                bg="black", 
                bd=0, 
                font=("Arial", 10)
                ).place(x=60, y=9, width=45, height=20)
        
        Button(
                menu_main,
                command=self.exit,
                text="</> Console", 
                fg="gray", 
                bg="black", 
                bd=0, 
                font=("Arial", 10, "bold")
                ).place(x=375, y=9, width=85, height=20) 





    def addUlubione(self):
        userAlive.dataUserCREATE6('fav_places', str(self.txt_user))
        
        placesname = userAlive.dataGeneral('fav_places' + str(self.txt_user), 'kolumna1')
        placesY = userAlive.dataGeneral('fav_places' + str(self.txt_user), 'kolumna2')
        placesX = userAlive.dataGeneral('fav_places' + str(self.txt_user), 'kolumna3')
        aktualna_lokalizacja_y = userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_y')
        aktualna_lokalizacja_x = userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_x')        
        alreadyEgsit = []
        for i in range(len(placesname)):
                if  aktualna_lokalizacja_y == placesY[i] and aktualna_lokalizacja_x == placesX[i]:                        
                        alreadyEgsit.append(placesname[i])
                i += 1        
        lending = len(alreadyEgsit)
        if lending > 0:
                userAlive.czytajTo('Masz już zapisane to miejsce pod nazą: ' + alreadyEgsit[0])
                userAlive.goTodo('okolica.py')
                root.quit()
        else:
                userAlive.dataUserINSERT6('fav_places', str(self.txt_user), str(self.saveName.get()), str(aktualna_lokalizacja_y), str(aktualna_lokalizacja_x), "", "", "")
                print("Miejsce zostało zapisane")
                userAlive.goTodo('okolica.py')
                root.quit()
  





    def setHome(self):
            aktualna_lokalizacja_y = userAlive.dotLocation(userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_y'))
            aktualna_lokalizacja_x = userAlive.dotLocation(userAlive.dataUserProfil(str(self.txt_user), 'aktualna_lokalizacja_x'))
        
            lokalizacja_dom_y = userAlive.dotLocation(userAlive.dataUserProfil(str(self.txt_user), 'lokalizacja_dom_y'))
            lokalizacja_dom_x = userAlive.dotLocation(userAlive.dataUserProfil(str(self.txt_user), 'lokalizacja_dom_x'))

            saldoUser = userAlive.dataUserProfil(str(self.txt_user), 'aktualne_vcoin')
            saldoUser = float(saldoUser)

            roznicaY = aktualna_lokalizacja_y - lokalizacja_dom_y
            roznicaX = aktualna_lokalizacja_x - lokalizacja_dom_x
            if roznicaY < 0:
                    roznicaY = roznicaY * -1
            if roznicaX < 0:
                    roznicaX = roznicaX * -1
            mnoznik = (roznicaY + roznicaX) * 10_000 / 2

            mnoznik = int(mnoznik)
            if saldoUser > mnoznik:
                userAlive.sysColorconsole('0','2')
                userAlive.mowTo("Hey richman, you rulez! Just put ENTER on the keyboard.")
                pot = input("Potwierdż ENTER że chcesz zapłacić VC$ " + str(mnoznik) + "\n[STOP] - Przerwij\n >>> " )
                if pot == "STOP" or pot == "stop":
                        print('Przeprowadzka odwołana')
                        userAlive.goTodo('okolica.py')
                        userAlive.sysColorconsole('0','4')
                        root.quit()
                else:
                        print("Zmiana miejsca zamieszkania kosztowała cię: " + str(mnoznik) + " VS$")
                        print("Przeprowadzka zakończona powodzeniem")
                        print(aktualna_lokalizacja_y, aktualna_lokalizacja_x)

                        userid = userAlive.dataUserSELECT('users_main', '', 'user', str(txt_user), 'identyfikator')
                        useridforchanged = userid[0]
                        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_dom_y', str(aktualna_lokalizacja_y), useridforchanged)
                        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_dom_x', str(aktualna_lokalizacja_x), useridforchanged)

                        prize = int(saldoUser - mnoznik) * 0.01 * 100
                        userAlive.dataUserUPDATE('users_main', '', 'aktualne_vcoin', str(prize), useridforchanged)
                        userAlive.checking_bar("Zmiena miejsca zamieszkania trwa", int(userAlive.mixer(100, (100 + mnoznik) * 2)), 0.01)

                        userAlive.goTodo('okolica.py')
                        userAlive.sysColorconsole('0','4')
                        root.quit()
            else:
                print('Masz zamało pieniędzy. Idź zarabiać gdzieś bliżej.')




            
        
    def teleportTo(self):        
        cy = self.wspC_Y.get()
        dy = self.wspD_Y.get()
        cx =self.wspC_X.get()
        dx = self.wspD_X.get()

        wspxy = [len(cy), len(dy), len(cx), len(dx)]                

        try:
            int(cy)
            int(dy)
            int(cx)
            int(dx)
            cyfry = True
        except:
            userAlive.mowTo("hey Sily, be focus on the moment! Did You put Wrong data. ")
            cyfry = False
        if cyfry == True: #  or (self.gotlat == True and self.gotlng == True)
            if int(wspxy[0]) < 5 and int(wspxy[2]) < 5 and int(wspxy[1]) > 5 and int(wspxy[3]) > 5:
                if int(cy) < 90 and int(cx) < 180 and int(cy) > -90 and int(cx) > -180:
                        miny = dy[0:6]
                        minx = dx[0:6]
                        if int(minx[5]) == 0:                                
                                minx = str(minx[:5]) + str("1")
                        if int(miny[5]) == 0:                                
                                miny = str(miny[:5]) + str("1")
                        
                        poblocY = str(cy) + "." + str(miny)
                        poblocX = str(cx) + "." + str(minx)
                        
                        googlePart1 = """https://earth.google.com/web/@"""
                        googlePart2 = str(poblocY)
                        googlePart3 = ","
                        googlePart4 = str(poblocX)
                        googlePart5 = """,80.88106533a,3324.79213989d,1y,0h,0t,0r" """
                        prepareLinkGoogleE = googlePart1 + googlePart2 + googlePart3 + googlePart4 + googlePart5
                        userAlive.goTodo('StreetHackerBrowser.py -a ' + prepareLinkGoogleE)
                        userAlive.goTodo('detector3dgoogledron.py')
                        userid = userAlive.dataUserSELECT('users_main', '', 'user', txt_user, 'identyfikator')
                        useridforchanged = userid[0]

                        # pobierz loc > aktualna, A, B, C
                        aktlokY = self.list_obecna_loc[0]
                        aktlokX = self.list_obecna_loc[1]

                        # ustaw aktualną ustaw C na D
                        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_y', str(self.punkt_CB_Y), useridforchanged)
                        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_x', str(self.punkt_CB_X), useridforchanged)

                        # ustaw aktualną ustaw B na C
                        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_y', str(self.punkt_DA_Y), useridforchanged)
                        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_x',str(self.punkt_DA_X), useridforchanged)

                        # ustaw aktualną ustaw A na B
                        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_y', str(self.punkt_AB_Y), useridforchanged)
                        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_x', str(self.punkt_AB_X), useridforchanged)

                        # ustaw aktualną ustaw aktualna na A
                        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_y', str(aktlokY), useridforchanged)
                        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_x', str(aktlokX), useridforchanged)


                        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_y', str(poblocY), useridforchanged)
                        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_x', str(poblocX), useridforchanged)

                        userAlive.goTodo('okolica.py')
                        root.quit()
                    
                else:
                    userAlive.czytajTo("Podane dane są nieprawidłowe. Nie ma takich współrzednych geograficznych.")
                    userAlive.mowTo("hey Sily, be focus on the moment! Did You put Wrong data. ")
            else:
                userAlive.czytajTo("Podane dane są niekompletne")
                userAlive.mowTo("hey Sily, be focus on the moment! Did You put Wrong data. ")
        else: 
            userAlive.mowTo("GeoError! ")







    def getLocation(self):        
        

        ######################################
        #Root/Okolica - Ramka Area
        ###################################### 
        area_ramka=Frame(self.root, bg="white")
        area_ramka.place(x=10, y=10, height=285, width=460)
        # w domu
        if self.list_obecna_loc[0] == self.lokalizacja_dom[0] and self.list_obecna_loc[1] == self.lokalizacja_dom[1]:
            Label(area_ramka, image=self.widget_screen_main_dom).place(x=0, y=0, relwidth=1, relheight=1)
            Label(
                area_ramka, 
                text="Dom  ", 
                font=("Impact", 45, "normal"),
                fg="white", 
                bg="black"
                ).place(x=5, y=5) 
            Label(
                area_ramka, 
                text="Witaj w domu "+str(self.txt_user), 
                font=("Corbel", 14, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=5, y=80)
           
            
        # poza domem                           
        else:
            Label(area_ramka, image=self.widget_screen_main_okolica).place(x=0, y=0, relwidth=1, relheight=1)
            Label(
                        area_ramka, 
                        text=" ",
                        font=("Corbel", 10, "normal"),
                        fg="white", 
                        bg="black",                 
                        justify="left"
                        ).place(x=5, y=8, height=125, width=325)

            Label(
                    area_ramka, 
                    text="Okolica ", 
                    font=("Impact", 45, "normal"),
                    fg="white", 
                    bg="black"
                    ).place(x=5, y=5) 
            Label(
                    area_ramka, 
                    text="Uważaj na siebie "+str(self.txt_user)+" bo jesteś poza domem.", 
                    font=("Corbel", 8, "normal"),
                    fg="#b4ff1a", 
                    bg="black", 
                    justify="left"
                    ).place(x=5, y=80)   
            

            Label(
                    area_ramka, 
                    text="Teren zeskanowany", 
                    font=("Corbel", 9, "bold"),
                    fg="#8aef06", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=5)

            Label(
                    area_ramka, 
                    text="Bankomaty:  ( "+str(self.bankomat)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#9aee2c", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=20) 

            Label(
                    area_ramka, 
                    text="Poczt: ( "+str(self.poczta)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#a5ef43", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=35) 
            Label(
                    area_ramka, 
                    text="Urzędów: ( "+str(self.urzad)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#adee58", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=50) 
            Label(
                    area_ramka, 
                    text="Hoteli: ( "+str(self.hotel)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#b4ff1a", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=65) 
            Label(
                    area_ramka, 
                    text="Restauracji: ( "+str(self.restauracja)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#b5ef68", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=80) 
            Label(
                    area_ramka, 
                    text="Firm: ( "+str(self.firma)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#beef7e", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=95) 

            Label(
                    area_ramka, 
                    text="Dostawców usług: ( "+str(self.uslugi)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#c5f18c", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=95)
            Label(
                    area_ramka, 
                    text="Sklepów: ( "+str(self.sklep)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#d1f5a1", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=110)

            Label(
                    area_ramka, 
                    text="( "+str(self.policja)+" )   komisariatów Policji w tej okolicy.", 
                    font=("Corbel", 8, "normal"),
                    fg="orange", 
                    bg="black", 
                    justify="left"
                    ).place(x=5, y=95)

            if len(self.otherPlayers) > 0:
                Label(
                        area_ramka, 
                        text="( "+str(len(self.otherPlayers))+" )   aktywności hackerów.", 
                        font=("Corbel", 8, "normal"),
                        fg="green", 
                        bg="black", 
                        justify="left"
                        ).place(x=5, y=110)
            else:
                Label(
                        area_ramka, 
                        text="( "+str(len(self.otherPlayers))+" )   aktywności hackerów.", 
                        font=("Corbel", 8, "normal"),
                        fg="red", 
                        bg="black", 
                        justify="left"
                        ).place(x=5, y=110)

            Button(
                area_ramka,
                command=self.backHome,
                text="</>WRÓĆ DO DOMU ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=310, y=215, height=15)        

            Button(
                area_ramka,
                command=self.setHome,
                text="</>USTAW TU DOM ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=10, y=235, height=15)

        Label(
                area_ramka, 
                text=" ",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black",                 
                justify="left"
                ).place(x=338, y=8, height=112, width=115)

        Label(
                area_ramka, 
                text="Historia ruchów",
                font=("Corbel", 10, "normal"),
                fg="gray", 
                bg="black",                 
                justify="left"
                ).place(x=340, y=8) 

        Button(area_ramka, 
                command = self.hista,
                text=" "+ str(self.punkt_AB_Y) + " / " + " "+ str(self.punkt_AB_X), 
                font=("Corbel", 8, "normal"),                
                fg="#aaa9aa", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=30)
        
        Button(area_ramka, 
                command = self.histb,
                text=" "+ str(self.punkt_DA_Y) + " / " + " "+ str(self.punkt_DA_X), 
                font=("Corbel", 8, "normal"),                
                fg="#646364", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=53)

        Button(area_ramka, 
                command = self.histc,
                text=" "+ str(self.punkt_CB_Y) + " / " + " "+ str(self.punkt_CB_X), 
                font=("Corbel", 8, "normal"),                
                fg="#4a494a", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=76)

        Button(area_ramka, 
                command = self.histd,
                text=" "+ str(self.punkt_DC_Y) + " / " + " "+ str(self.punkt_DC_X), 
                font=("Corbel", 8, "normal"),                
                fg="#222222", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=99)

        Label(
                area_ramka, 
                text="Twoja obecna lokalizacja ",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=5, y=135)  
        loc_pozycja = 165
        for kolejna_loc in self.list_obecna_loc:
            Label(
                area_ramka, 
                text=str(kolejna_loc),
                font=("Corbel", 11, "normal"),
                fg="#03ff21", 
                bg="black", 
                justify="left"
                ).place(x=10, y=loc_pozycja)
            loc_pozycja += 20        
        Button(
                area_ramka,
                command=self.link_mapa,
                text="</>MAPA ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=110, y=165, height=15)
        Button(
                area_ramka,
                command=self.idzDoLokacji,
                text="</>IDŹ ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=110, y=185, height=15)
        Button(
                area_ramka,
                command=self.savePlace,
                text="</>ZAPISZ TO MIEJSCE ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=10, y=215, height=15)

        Label(
                area_ramka, 
                text="Lokalizacja domu",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=305, y=135)
        dom_pozycja = 165
        for xy_dom in self.lokalizacja_dom:
            Label(
                    area_ramka, 
                    text=str(xy_dom),
                    font=("Corbel", 11, "normal"),
                    fg="#03ff21", 
                    bg="black", 
                    justify="left"
                    ).place(x=310, y=dom_pozycja)
            dom_pozycja += 20
       
        ###############################
        # lokacje

        Label(
                area_ramka, 
                text="Wprowadź współrzedne   \n\n\n\n\n\n\n",
                font=("Corbel", 8, "normal"),
                fg="orange", 
                bg="black", 
                justify="left"
                ).place(x=170, y=135)

        Label(
                area_ramka, 
                text="W/E",
                font=("Corbel", 6, "normal"),
                fg="#1eff00", 
                bg="black", 
                justify="left"
                ).place(x=180, y=169)   
        
        Label(
                area_ramka, 
                text="N/S",
                font=("Corbel", 6, "normal"),
                fg="#1eff00", 
                bg="black", 
                justify="left"
                ).place(x=180, y=154)

        # Label(
        #         area_ramka, 
        #         text=" . ",
        #         font=("Corbel", 18, "normal"),
        #         fg="#1eff00", 
        #         bg="black", 
        #         justify="left"
        #         ).place(x=222, y=158)

        # Label(
        #         area_ramka, 
        #         text=" . ",
        #         font=("Corbel", 18, "normal"),
        #         fg="#1eff00", 
        #         bg="black", 
        #         justify="left"
        #         ).place(x=222, y=140)

        Label(
                area_ramka, 
                text="Wprowadź współrzedne   ",
                font=("Corbel", 8, "normal"),
                fg="orange", 
                bg="black", 
                justify="left"
                ).place(x=170, y=135)
        
        # ##############################
        # # podaj lokacje

        # self.wspC_Y = Entry(
        #         area_ramka,                 
        #         font=("Arial", 7, "normal"), 
        #         fg="#1eff00", bg="black"
        #         )
        # self.wspC_Y.place(x=205, y=155, width=20, height=12)

        self.getDataMap = Entry(
                area_ramka,                 
                font=("Arial", 5, "normal"), 
                fg="#1eff00", bg="black"
                )
        self.getDataMap.place(x=202, y=155, width=75, height=29)

        # self.wspC_X = Entry(
        #         area_ramka,                 
        #         font=("Arial", 7, "normal"), 
        #         fg="#1eff00", bg="black"
        #         )
        # self.wspC_X.place(x=205, y=170, width=20, height=12)

        # self.wspD_X = Entry(
        #         area_ramka,                 
        #         font=("Arial", 7, "normal"), 
        #         fg="#1eff00", bg="black"
        #         )
        # self.wspD_X.place(x=242, y=170, width=35, height=12)

        Button(
                area_ramka,
                command=self.autogetLocation,
                text="AUTO CONVERTER", 
                fg="#b4fffa", 
                bg="#121212", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=175, y=189, height=50, width=110)

        # Button(
        #         area_ramka,
        #         command=self.sprawdzLokacje,
        #         text=" CHECK ", 
        #         fg="#b4fffa", 
        #         bg="#121212",
        #         bd=0, 
        #         justify="left",
        #         font=("Arial", 7)
        #         ).place(x=173, y=207, height=15, width=55)

        # Button(
        #         area_ramka,
        #         command=self.teleportTo,
        #         text=" GO ", 
        #         fg="#b4fffa", 
        #         bg="#121212", 
        #         bd=0, 
        #         justify="left",
        #         font=("Arial", 7)
        #         ).place(x=233, y=207, height=15, width=55)
        
        # Button(
        #         area_ramka,
        #         command=self.openPlace,
        #         text=" OPEN SAVED ", 
        #         fg="#b4fffa", 
        #         bg="#121212", 
        #         bd=0, 
        #         justify="left",
        #         font=("Arial", 7)
        #         ).place(x=174, y=227, height=15, width=115)
        #######################################
        #
        # Root/Profill - Ramka MAIN MENU
        #
        #######################################
        def move_app(e):                   
            root.geometry(f'+{e.x_root-260}+{e.y_root-300}')
        checkSessions()
        menu_main=Frame(self.root, bg="black")
        menu_main.place(x=6, y=273, height=37, width=468)
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
                text="Okolica", 
                fg="#79ffff", 
                bg="black", 
                bd=0, 
                font=("Arial", 10)
                ).place(x=60, y=9, width=45, height=20)
        
        Button(
                menu_main,
                command=self.exit,
                text="</> Console", 
                fg="gray", 
                bg="black", 
                bd=0, 
                font=("Arial", 10, "bold")
                ).place(x=375, y=9, width=85, height=20) 
        Label(self.root, text="UWAGA!! AUTOMATYCZNE POBIERANIE!", font=('Arial', 6, 'bold'), bg="black", fg='yellow').place(x=20, y=225)
        Label(self.root, text="Nie poruszaj kursorem myszy podczas", font=('Arial', 6, 'bold'), bg="black", fg='yellow').place(x=20, y=240)
        Label(self.root, text="kopiowana do boksu. Pozostaw okno z mapą widoczne.", font=('Arial', 6, 'bold'), bg="black", fg='yellow').place(x=20, y=255)



        userAlive.checking_bar("Operacja rozpocznie się za kilka sekund", 10, 0.001)
        userAlive.goTodo('locfromstreethackermap.py')


    def autogetLocation(self):
        gotLocation = self.getDataMap.get()
        self.gotlat = str(userAlive.gotLocation(gotLocation)[0]) + str("01")
        self.gotlng = str(userAlive.gotLocation(gotLocation)[1]) + str("01")

        ######################################
        #Root/Okolica - Ramka Area
        ###################################### 
        area_ramka=Frame(self.root, bg="white")
        area_ramka.place(x=10, y=10, height=285, width=460)
        # w domu
        if self.list_obecna_loc[0] == self.lokalizacja_dom[0] and self.list_obecna_loc[1] == self.lokalizacja_dom[1]:
            Label(area_ramka, image=self.widget_screen_main_dom).place(x=0, y=0, relwidth=1, relheight=1)
            Label(
                area_ramka, 
                text="Dom  ", 
                font=("Impact", 45, "normal"),
                fg="white", 
                bg="black"
                ).place(x=5, y=5) 
            Label(
                area_ramka, 
                text="Witaj w domu "+str(self.txt_user), 
                font=("Corbel", 14, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=5, y=80)
           
            
        # poza domem                           
        else:
            Label(area_ramka, image=self.widget_screen_main_okolica).place(x=0, y=0, relwidth=1, relheight=1)
            Label(
                        area_ramka, 
                        text=" ",
                        font=("Corbel", 10, "normal"),
                        fg="white", 
                        bg="black",                 
                        justify="left"
                        ).place(x=5, y=8, height=125, width=325)

            Label(
                    area_ramka, 
                    text="Okolica ", 
                    font=("Impact", 45, "normal"),
                    fg="white", 
                    bg="black"
                    ).place(x=5, y=5) 
            Label(
                    area_ramka, 
                    text="Uważaj na siebie "+str(self.txt_user)+" bo jesteś poza domem.", 
                    font=("Corbel", 8, "normal"),
                    fg="#b4ff1a", 
                    bg="black", 
                    justify="left"
                    ).place(x=5, y=80)   
            

            Label(
                    area_ramka, 
                    text="Teren zeskanowany", 
                    font=("Corbel", 9, "bold"),
                    fg="#8aef06", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=5)

            Label(
                    area_ramka, 
                    text="Bankomaty:  ( "+str(self.bankomat)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#9aee2c", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=20) 

            Label(
                    area_ramka, 
                    text="Poczt: ( "+str(self.poczta)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#a5ef43", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=35) 
            Label(
                    area_ramka, 
                    text="Urzędów: ( "+str(self.urzad)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#adee58", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=50) 
            Label(
                    area_ramka, 
                    text="Hoteli: ( "+str(self.hotel)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#b4ff1a", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=65) 
            Label(
                    area_ramka, 
                    text="Restauracji: ( "+str(self.restauracja)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#b5ef68", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=80) 
            Label(
                    area_ramka, 
                    text="Firm: ( "+str(self.firma)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#beef7e", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=95) 

            Label(
                    area_ramka, 
                    text="Dostawców usług: ( "+str(self.uslugi)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#c5f18c", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=95)
            Label(
                    area_ramka, 
                    text="Sklepów: ( "+str(self.sklep)+" )", 
                    font=("Corbel", 8, "normal"),
                    fg="#d1f5a1", 
                    bg="black", 
                    justify="left"
                    ).place(x=220, y=110)

            Label(
                    area_ramka, 
                    text="( "+str(self.policja)+" )   komisariatów Policji w tej okolicy.", 
                    font=("Corbel", 8, "normal"),
                    fg="orange", 
                    bg="black", 
                    justify="left"
                    ).place(x=5, y=95)

            if len(self.otherPlayers) > 0:
                Label(
                        area_ramka, 
                        text="( "+str(len(self.otherPlayers))+" )   aktywności hackerów.", 
                        font=("Corbel", 8, "normal"),
                        fg="green", 
                        bg="black", 
                        justify="left"
                        ).place(x=5, y=110)
            else:
                Label(
                        area_ramka, 
                        text="( "+str(len(self.otherPlayers))+" )   aktywności hackerów.", 
                        font=("Corbel", 8, "normal"),
                        fg="red", 
                        bg="black", 
                        justify="left"
                        ).place(x=5, y=110)

            Button(
                area_ramka,
                command=self.backHome,
                text="</>WRÓĆ DO DOMU ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=310, y=215, height=15)        

            Button(
                area_ramka,
                command=self.setHome,
                text="</>USTAW TU DOM ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=10, y=235, height=15)

        Label(
                area_ramka, 
                text=" ",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black",                 
                justify="left"
                ).place(x=338, y=8, height=112, width=115)

        Label(
                area_ramka, 
                text="Historia ruchów",
                font=("Corbel", 10, "normal"),
                fg="gray", 
                bg="black",                 
                justify="left"
                ).place(x=340, y=8) 

        Button(area_ramka, 
                command = self.hista,
                text=" "+ str(self.punkt_AB_Y) + " / " + " "+ str(self.punkt_AB_X), 
                font=("Corbel", 8, "normal"),                
                fg="#aaa9aa", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=30)
        
        Button(area_ramka, 
                command = self.histb,
                text=" "+ str(self.punkt_DA_Y) + " / " + " "+ str(self.punkt_DA_X), 
                font=("Corbel", 8, "normal"),                
                fg="#646364", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=53)

        Button(area_ramka, 
                command = self.histc,
                text=" "+ str(self.punkt_CB_Y) + " / " + " "+ str(self.punkt_CB_X), 
                font=("Corbel", 8, "normal"),                
                fg="#4a494a", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=76)

        Button(area_ramka, 
                command = self.histd,
                text=" "+ str(self.punkt_DC_Y) + " / " + " "+ str(self.punkt_DC_X), 
                font=("Corbel", 8, "normal"),                
                fg="#222222", 
                bg="black", 
                bd=0, 
                justify="left"
                ).place(x=340, y=99)

        Label(
                area_ramka, 
                text="Twoja obecna lokalizacja ",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=5, y=135)  
        loc_pozycja = 165
        for kolejna_loc in self.list_obecna_loc:
            Label(
                area_ramka, 
                text=str(kolejna_loc),
                font=("Corbel", 11, "normal"),
                fg="#03ff21", 
                bg="black", 
                justify="left"
                ).place(x=10, y=loc_pozycja)
            loc_pozycja += 20        
        Button(
                area_ramka,
                command=self.link_mapa,
                text="</>MAPA ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=110, y=165, height=15)
        Button(
                area_ramka,
                command=self.idzDoLokacji,
                text="</>IDŹ ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=110, y=185, height=15)
        Button(
                area_ramka,
                command=self.savePlace,
                text="</>ZAPISZ TO MIEJSCE ", 
                fg="#b4fffa", 
                bg="black", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=10, y=215, height=15)

        Label(
                area_ramka, 
                text="Lokalizacja domu",
                font=("Corbel", 10, "normal"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=305, y=135)
        dom_pozycja = 165
        for xy_dom in self.lokalizacja_dom:
            Label(
                    area_ramka, 
                    text=str(xy_dom),
                    font=("Corbel", 11, "normal"),
                    fg="#03ff21", 
                    bg="black", 
                    justify="left"
                    ).place(x=310, y=dom_pozycja)
            dom_pozycja += 20
       
        ###############################
        # lokacje

        Label(
                area_ramka, 
                text="",
                font=("Corbel", 8, "normal"),
                fg="orange", 
                bg="black", 
                justify="left"
                ).place(x=170, y=135, width=125, height=70)

        Label(
                area_ramka, 
                text="W/E",
                font=("Corbel", 6, "normal"),
                fg="#1eff00", 
                bg="black", 
                justify="left"
                ).place(x=180, y=169)   
        
        Label(
                area_ramka, 
                text="N/S",
                font=("Corbel", 6, "normal"),
                fg="#1eff00", 
                bg="black", 
                justify="left"
                ).place(x=180, y=154)

        # Label(
        #         area_ramka, 
        #         text=" . ",
        #         font=("Corbel", 18, "normal"),
        #         fg="#1eff00", 
        #         bg="black", 
        #         justify="left"
        #         ).place(x=222, y=158)

        # Label(
        #         area_ramka, 
        #         text=" . ",
        #         font=("Corbel", 18, "normal"),
        #         fg="#1eff00", 
        #         bg="black", 
        #         justify="left"
        #         ).place(x=222, y=140)

        Label(
                area_ramka, 
                text="Pobrane współrzedne   ",
                font=("Corbel", 8, "normal"),
                fg="orange", 
                bg="black", 
                justify="left"
                ).place(x=172, y=135)
        
        # ##############################
        # # podaj lokacje

        Label(
                area_ramka,  
                text=self.gotlat,                   
                font=("Arial", 7, "normal"), 
                fg="#1eff00", bg="black"
                ).place(x=215, y=156, height=12)
        
        # self.wspC_Y        
        # self.wspD_Y


        Label(
                area_ramka,
                text=self.gotlng,               
                font=("Arial", 7, "normal"), 
                fg="#1eff00", bg="black"
                ).place(x=215, y=171,  height=12)

        # self.wspC_X        
        # self.wspD_X

        # Button(
        #         area_ramka,
        #         command=self.getLocation,
        #         text=" GET FROM MAP ", 
        #         fg="#b4fffa", 
        #         bg="#121212", 
        #         bd=0, 
        #         justify="left",
        #         font=("Arial", 7)
        #         ).place(x=174, y=187, height=15, width=115)

        # Button(
        #         area_ramka,
        #         command=self.sprawdzLokacje,
        #         text=" CHECK ", 
        #         fg="#b4fffa", 
        #         bg="#121212",
        #         bd=0, 
        #         justify="left",
        #         font=("Arial", 7)
        #         ).place(x=173, y=207, height=15, width=55)

        Button(
                area_ramka,
                command=self.teleportTogetmap,
                text=" GO ", 
                fg="#b4fffa", 
                bg="#121212", 
                bd=0, 
                justify="left",
                font=("Arial", 7)
                ).place(x=174, y=187, height=15, width=115)
        
        # Button(
        #         area_ramka,
        #         command=self.openPlace,
        #         text=" OPEN SAVED ", 
        #         fg="#b4fffa", 
        #         bg="#121212", 
        #         bd=0, 
        #         justify="left",
        #         font=("Arial", 7)
        #         ).place(x=174, y=227, height=15, width=115)
        #######################################
        #
        # Root/Profill - Ramka MAIN MENU
        #
        #######################################
        def move_app(e):                   
            root.geometry(f'+{e.x_root-260}+{e.y_root-300}')
        checkSessions()
        menu_main=Frame(self.root, bg="black")
        menu_main.place(x=6, y=273, height=37, width=468)
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
                text="Okolica", 
                fg="#79ffff", 
                bg="black", 
                bd=0, 
                font=("Arial", 10)
                ).place(x=60, y=9, width=45, height=20)
        
        Button(
                menu_main,
                command=self.exit,
                text="</> Console", 
                fg="gray", 
                bg="black", 
                bd=0, 
                font=("Arial", 10, "bold")
                ).place(x=375, y=9, width=85, height=20) 


    def teleportTogetmap(self):
        googlePart1 = """https://earth.google.com/web/@"""
        googlePart2 = str(self.gotlat)
        googlePart3 = ","
        googlePart4 = str(self.gotlng)
        googlePart5 = """,80.88106533a,3324.79213989d,1y,0h,0t,0r" """
        prepareLinkGoogleE = googlePart1 + googlePart2 + googlePart3 + googlePart4 + googlePart5
        userAlive.goTodo('StreetHackerBrowser.py -a ' + prepareLinkGoogleE)
        userAlive.goTodo('detector3dgoogledron.py')
        userid = userAlive.dataUserSELECT('users_main', '', 'user', str(self.txt_user), 'identyfikator')
        useridforchanged = userid[0]
        
        print(userid[0])
        print(userid)
        print(type(userid))

        # pobierz loc > aktualna, A, B, C
        aktlokY = self.list_obecna_loc[0]
        aktlokX = self.list_obecna_loc[1]

        # ustaw aktualną ustaw C na D
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_y', str(self.punkt_CB_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_x', str(self.punkt_CB_X), useridforchanged)

        # ustaw aktualną ustaw B na C
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_y', str(self.punkt_DA_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_x', str(self.punkt_DA_X), useridforchanged)

        # ustaw aktualną ustaw A na B
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_y', str(self.punkt_AB_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_x', str(self.punkt_AB_X), useridforchanged)

        # ustaw aktualną ustaw aktualna na A
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_y', str(aktlokY), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_x', str(aktlokX), useridforchanged)


        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_y', str(self.gotlat), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_x', str(self.gotlng), useridforchanged)

        userAlive.goTodo('okolica.py')
        root.quit()



    def backHome(self):
        lokalizacja_dom_y = userAlive.dotLocation(userAlive.dataUserProfil(str(self.txt_user), 'lokalizacja_dom_y'))
        lokalizacja_dom_x = userAlive.dotLocation(userAlive.dataUserProfil(str(self.txt_user), 'lokalizacja_dom_x'))

        userid = userAlive.dataUserSELECT('users_main', '', 'user', str(txt_user), 'identyfikator')
        useridforchanged = userid[0]

        # pobierz loc > aktualna, A, B, C
        aktlokY = self.list_obecna_loc[0]
        aktlokX = self.list_obecna_loc[1]
        
        # ustaw aktualną ustaw C na D
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_y', str(self.punkt_CB_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_x', str(self.punkt_CB_X), useridforchanged)

        # ustaw aktualną ustaw B na C
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_y', str(self.punkt_DA_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_x', str(self.punkt_DA_X), useridforchanged)

        # ustaw aktualną ustaw A na B
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_y', str(self.punkt_AB_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_x', str(self.punkt_AB_X), useridforchanged)

        # ustaw aktualną ustaw aktualna na A
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_y', str(aktlokY), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_x', str(aktlokX), useridforchanged)


        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_y', str(lokalizacja_dom_y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_x', str(lokalizacja_dom_x), useridforchanged)  

        userAlive.goTodo('okolica.py')
        userAlive.sysColorconsole('0','4')
        root.quit()






    def hista(self):
        userid = userAlive.dataUserSELECT('users_main', '', 'user', str(txt_user), 'identyfikator')
        useridforchanged = userid[0]

        # pobierz loc > aktualna, A, B, C
        aktlokY = self.list_obecna_loc[0]
        aktlokX = self.list_obecna_loc[1]
        
        # ustaw aktualną ustaw C na D
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_y', str(self.punkt_CB_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_x', str(self.punkt_CB_X), useridforchanged)

        # ustaw aktualną ustaw B na C
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_y', str(self.punkt_DA_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_x', str(self.punkt_DA_X), useridforchanged)

        # ustaw aktualną ustaw A na B
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_y', str(self.punkt_AB_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_x', str(self.punkt_AB_X), useridforchanged)

        # ustaw aktualną ustaw aktualna na A
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_y', str(aktlokY), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_x', str(aktlokX), useridforchanged)

        # ustaw A jako aktuala
        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_y', str(self.punkt_AB_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_x', str(self.punkt_AB_X), useridforchanged)
        userAlive.goTodo('okolica.py')
        root.quit()



    def histb(self):
        userid = userAlive.dataUserSELECT('users_main', '', 'user', str(txt_user), 'identyfikator')
        useridforchanged = userid[0]

        # pobierz loc > aktualna, A, B, C
        aktlokY = self.list_obecna_loc[0]
        aktlokX = self.list_obecna_loc[1]
        
        # ustaw aktualną ustaw C na D
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_y', str(self.punkt_CB_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_x', str(self.punkt_CB_X), useridforchanged)

        # ustaw aktualną ustaw B na C
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_y', str(self.punkt_DA_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_x', str(self.punkt_DA_X), useridforchanged)

        # ustaw aktualną ustaw A na B
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_y', str(self.punkt_AB_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_x', str(self.punkt_AB_X), useridforchanged)

        # ustaw aktualną ustaw aktualna na A
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_y', str(aktlokY), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_x', str(aktlokX), useridforchanged)

        # ustaw A jako aktuala
        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_y', str(self.punkt_DA_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_x', str(self.punkt_DA_X), useridforchanged)
        userAlive.goTodo('okolica.py')
        root.quit()





    def histc(self):
        userid = userAlive.dataUserSELECT('users_main', '', 'user', str(txt_user), 'identyfikator')
        useridforchanged = userid[0]

        # pobierz loc > aktualna, A, B, C
        aktlokY = self.list_obecna_loc[0]
        aktlokX = self.list_obecna_loc[1]
        
        # ustaw aktualną ustaw C na D
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_y', str(self.punkt_CB_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_x', str(self.punkt_CB_X), useridforchanged)

        # ustaw aktualną ustaw B na C
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_y', str(self.punkt_DA_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_x', str(self.punkt_DA_X), useridforchanged)

        # ustaw aktualną ustaw A na B
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_y', str(self.punkt_AB_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_x', str(self.punkt_AB_X), useridforchanged)

        # ustaw aktualną ustaw aktualna na A
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_y', str(aktlokY), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_x', str(aktlokX), useridforchanged)

        # ustaw A jako aktuala
        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_y', str(self.punkt_CB_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_x', str(self.punkt_CB_X), useridforchanged)
        userAlive.goTodo('okolica.py')
        root.quit()





    def histd(self):
        userid = userAlive.dataUserSELECT('users_main', '', 'user', str(txt_user), 'identyfikator')
        useridforchanged = userid[0]

        # pobierz loc > aktualna, A, B, C
        aktlokY = self.list_obecna_loc[0]
        aktlokX = self.list_obecna_loc[1]
        
        # ustaw aktualną ustaw C na D
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_y', str(self.punkt_CB_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_x', str(self.punkt_CB_X), useridforchanged)

        # ustaw aktualną ustaw B na C
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_y', str(self.punkt_DA_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_x', str(self.punkt_DA_X), useridforchanged)

        # ustaw aktualną ustaw A na B
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_y', str(self.punkt_AB_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_x', str(self.punkt_AB_X), useridforchanged)

        # ustaw aktualną ustaw aktualna na A
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_y', str(aktlokY), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_x', str(aktlokX), useridforchanged)

        # ustaw A jako aktuala
        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_y', str(self.punkt_DC_Y), useridforchanged)
        userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_x', str(self.punkt_DC_X), useridforchanged)
        userAlive.goTodo('okolica.py')
        root.quit()




    def exit(self):
        userAlive.exitSys()

# userAlive.checking_bar("Aktywne okno nawigacji ... " + txt_user, 100, 0.02)
root = tkinter.Tk()
area = Obszar_Roboczy(root, txt_user, session)

root.mainloop()