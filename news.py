import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from time import sleep
from tkhtmlview import HTMLLabel
import userAlive

txt_user = userAlive.giveUser()
session = userAlive.giveSS()


userAlive.banner(session, "Uruchomiona instancja")
userAlive.sysColorconsole("0", "4", "Uruchomiona instancja")

userAlive.dataUserCREATE6("today_news", str(txt_user))
userAlive.dataUserDELETE('today_news', str(txt_user), 'kolumna6', 'del')

listNewsTitle = userAlive.dataGeneral("news", "title")
listNewsContent = userAlive.dataGeneral("news", "content")
listNewsData = userAlive.dataGeneral("news", "data")

listRoundRange = userAlive.mixer(4, 9)
listRoundStart = userAlive.mixer(0, 11)

print(listRoundRange, listRoundStart)

for news in range(listRoundRange):
    listNewsDownload = userAlive.mixer(0, 6)
    if listNewsDownload == 1:
        download = 'download'
    else:
        download = 'empty'
    
    userAlive.dataUserINSERT6('today_news', str(txt_user), str(listNewsTitle[news]), str(listNewsData[news]), str(listNewsContent[news]), str(download), 'NULL', 'del')
    news += listRoundStart


class Obszar_Roboczy:
    def __init__(self, root, txt_user, session):
        self.root = root
        self.root.title("Street HacKer v 1.001")
        self.root.geometry("480x420+720+160")
        self.root.resizable(False, False)   
        self.root.overrideredirect(True)  
        self.root.attributes('-alpha', 0.9)
        self.txt_user = txt_user
        self.bg=ImageTk.PhotoImage(file="img/main_logoff.png")
        self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        def move_app(e):                   
            root.geometry(f'+{e.x_root-260}+{e.y_root-380}')

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
        arearea_ramka.place(x=10, y=10, height=385, width=460)
        Label(arearea_ramka, image=self.widget_screen_main_adept).place(x=0, y=0, relwidth=1, relheight=1)
        Label(
                        arearea_ramka, 
                        text="Street Hacker News!", 
                        font=("Impact", 36),
                        fg="white", 
                        bg="black"
                        ).place(x=5, y=5)             
        

        
        self.list_oznaczone_general_tools = userAlive.dataGeneral('tools', "tool_name") 
        


        self.list_oznaczone_news = []
        self.list_oznaczone_news_index = []
        self.list_oznaczone_news_tytul = userAlive.dataGeneral('today_news' + str(self.txt_user), "kolumna1")
        self.list_oznaczone_news_data = userAlive.dataGeneral('today_news' + str(self.txt_user), "kolumna2")
        self.list_oznaczone_news_opis = userAlive.dataGeneral('today_news' + str(self.txt_user), "kolumna3")
        self.list_oznaczone_news_download = userAlive.dataGeneral('today_news' + str(self.txt_user), "kolumna4")
        
        
        
        idexes_list = len(self.list_oznaczone_news_tytul)
        
        for post in range(int(idexes_list)):
            insPos = "     [  " + self.list_oznaczone_news_data[post] + "  ]  | "+ self.list_oznaczone_news_tytul[post]
            self.list_oznaczone_news_index.append(post)
            self.list_oznaczone_news.append(insPos)
            post += 1

        Label(
                        arearea_ramka, 
                        text="Najświeższe Newsy",
                        font=("Corbel", 15, "bold"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        ).place(x=33, y=75)


        self.my_listBox = Listbox(                            
                        arearea_ramka,                         
                        borderwidth=0, 
                        highlightthickness=0,
                        font=("Corbel", 12, "normal"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        )
        self.my_listBox.place(x=33, y=109, width=388, height=219)


        for item in self.list_oznaczone_news:
            self.my_listBox.insert(END, item)
        
        Button(
                arearea_ramka, 
                text="CZYTAJ",
                command=self.program_news,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Impact", 18, "bold"),
                fg="orange", 
                bg="black", 
                justify="left" 
                ).place(x=33, y=334, width=388, height=30)


        Button(
                        arearea_ramka, 
                        text="</> WALK",
                        font=("Corbel", 8, "normal"),
                        # command = self.cel_samochodowy,
                        fg="#b4fffa", 
                        bg="#011c24", 
                        justify="left",
                        bd=0
                            ).place(x=315, y=85, height=15)
        
        Button(
                        arearea_ramka, 
                        text="</>TOOLS",
                        font=("Corbel", 8, "normal"),
                        command = self.tools,
                        fg="#b4fffa", 
                        bg="#011c24", 
                        justify="left",
                        bd=0
                            ).place(x=375, y=85, height=15)
        ################################################################

        # MENU BOTTOM PAGE

        ################################################################

        checkSessions()
        menu_main=Frame(self.root, bg="black")
        menu_main.place(x=6, y=373, height=37, width=468)
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
                text="News", 
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
                ).place(x=375, y=9, width=85, height=20)

    def exit(self):
        userAlive.exitSys()

    def program_news(self):
        try:
            choice = self.my_listBox.get(ANCHOR)        
            indexChoice = self.list_oznaczone_news.index(choice)
            newsTitle = self.list_oznaczone_news_tytul[indexChoice]
            newsContent = self.list_oznaczone_news_opis[indexChoice]
            newsData = self.list_oznaczone_news_data[indexChoice]
        except:
            newsTitle = 'Hack News!'            
            newsContent = 'Wyberz news do wyświetlenia'
            newsData = 'The best news data'
            indexChoice = 0

        area_ramka=Frame(self.root, bg="white")
        area_ramka.place(x=10, y=10, height=365, width=460)
        Label(area_ramka, image=self.widget_screen_main_adept2).place(x=0, y=0, relwidth=1, relheight=1)
        Label(
                area_ramka, 
                text=newsTitle, 
                font=("Impact", 36),
                fg="white", 
                bg="black"
                ).place(x=5, y=5)
        
        Label(
                area_ramka, 
                text=newsData,
                font=("Corbel", 15, "bold"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=33, y=75)
        Label(
                area_ramka, 
                text=newsContent,
                wraplength=350,
                font=("Corbel", 11, "bold"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=33, y=108, height=225, width=388)

        
        if self.list_oznaczone_news_download[indexChoice] != "download":
                Button(
                area_ramka, 
                text="Zaknij news'a",
                command=self.closeNews,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Impact", 18, "bold"),
                fg="orange", 
                bg="black", 
                justify="left" 
                ).place(x=33, y=334, width=388, height=30)
        else:                   

                Button(
                        area_ramka, 
                        text="DOWNLOAD </> TOOLS",
                        font=("Corbel", 8, "normal"),
                        command = self.download,                    
                        fg="red", 
                        bg="#011c24", 
                        justify="left",
                        bd=0
                        ).place(x=300, y=85, height=15)    
                
                Button(
                        area_ramka, 
                        text="Zaknij news'a",
                        command=self.closeNews,
                        highlightbackground = "black", 
                        highlightthickness = 2,
                        bd=0,                        
                        font=("Impact", 18, "bold"),
                        fg="orange", 
                        bg="black", 
                        justify="left" 
                        ).place(x=33, y=334, width=388, height=30)

    def download(self):       
        choice = self.my_listBox.get(ANCHOR)        
        indexChoice = self.list_oznaczone_news.index(choice)
        newsDownload = self.list_oznaczone_news_download[indexChoice]

        
        idTool = len(self.list_oznaczone_general_tools)
        getTools = self.list_oznaczone_general_tools
        
        pickedTool = userAlive.mixer(0, idTool)
        theTool = getTools[pickedTool]

        userAlive.sendUser(self.txt_user)
        userAlive.writeSS(self.txt_user)
        
        userAlive.goTodo('download.py -t "' + theTool+'"')
        self.list_oznaczone_news_download[indexChoice] = ''

        arearea_ramka=Frame(self.root, bg="white")
        arearea_ramka.place(x=10, y=10, height=385, width=460)
        Label(arearea_ramka, image=self.widget_screen_main_adept).place(x=0, y=0, relwidth=1, relheight=1)
        Label(
                arearea_ramka, 
                text="Street Hacker News!", 
                font=("Impact", 36),
                fg="white", 
                bg="black"
                ).place(x=5, y=5)
        
        def move_app(e):                   
            root.geometry(f'+{e.x_root-260}+{e.y_root-380}')      
        Label(
                arearea_ramka, 
                text="Najświeższe Newsy",
                font=("Corbel", 15, "bold"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=33, y=75)
        self.my_listBox = Listbox(                            
                        arearea_ramka,                         
                        borderwidth=0, 
                        highlightthickness=0,
                        font=("Corbel", 12, "normal"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        )
        self.my_listBox.place(x=33, y=109, width=388, height=219)
        for item in self.list_oznaczone_news:
            self.my_listBox.insert(END, item)
        Button(
                arearea_ramka, 
                text="CZYTAJ",
                command=self.program_news,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Impact", 18, "bold"),
                fg="orange", 
                bg="black", 
                justify="left" 
                ).place(x=33, y=334, width=388, height=30)
        Button(
                arearea_ramka, 
                text="</> WALK",
                font=("Corbel", 8, "normal"),
                # command = self.cel_samochodowy,
                fg="#b4fffa", 
                bg="#011c24", 
                justify="left",
                bd=0
                ).place(x= 315, y=85, height=15)        
        Button(
                arearea_ramka, 
                text="</>TOOLS",
                font=("Corbel", 8, "normal"),
                command = self.tools,
                fg="#b4fffa", 
                bg="#011c24", 
                justify="left",
                bd=0
                ).place(x=375, y=85, height=15)

        ################################################################

        # MENU BOTTOM PAGE

        ################################################################
        menu_main=Frame(self.root, bg="black")
        menu_main.place(x=6, y=373, height=37, width=468)
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
                text="News", 
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
                ).place(x=375, y=9, width=85, height=20)
       
        
        
       

    def closeNews(self):
        arearea_ramka=Frame(self.root, bg="white")
        arearea_ramka.place(x=10, y=10, height=385, width=460)
        Label(arearea_ramka, image=self.widget_screen_main_adept).place(x=0, y=0, relwidth=1, relheight=1)
        Label(
                arearea_ramka, 
                text="Street Hacker News!", 
                font=("Impact", 36),
                fg="white", 
                bg="black"
                ).place(x=5, y=5)
        
        def move_app(e):                   
            root.geometry(f'+{e.x_root-260}+{e.y_root-380}')      
        Label(
                arearea_ramka, 
                text="Najświeższe Newsy",
                font=("Corbel", 15, "bold"),
                fg="white", 
                bg="black", 
                justify="left"
                ).place(x=33, y=75)
        self.my_listBox = Listbox(                            
                        arearea_ramka,                         
                        borderwidth=0, 
                        highlightthickness=0,
                        font=("Corbel", 12, "normal"),
                        fg="white", 
                        bg="black", 
                        justify="left"
                        )
        self.my_listBox.place(x=33, y=109, width=388, height=219)
        for item in self.list_oznaczone_news:
            self.my_listBox.insert(END, item)
        Button(
                arearea_ramka, 
                text="CZYTAJ",
                command=self.program_news,
                highlightbackground = "black", 
                highlightthickness = 2,
                bd=0,                        
                font=("Impact", 18, "bold"),
                fg="orange", 
                bg="black", 
                justify="left" 
                ).place(x=33, y=334, width=388, height=30)
        Button(
                arearea_ramka, 
                text="</> WALK",
                font=("Corbel", 8, "normal"),
                # command = self.cel_samochodowy,
                fg="#b4fffa", 
                bg="#011c24", 
                justify="left",
                bd=0
                ).place(x= 315, y=85, height=15)        
        Button(
                arearea_ramka, 
                text="</>TOOLS",
                font=("Corbel", 8, "normal"),
                command = self.tools,
                fg="#b4fffa", 
                bg="#011c24", 
                justify="left",
                bd=0
                ).place(x=375, y=85, height=15)

        ################################################################

        # MENU BOTTOM PAGE

        ################################################################
        menu_main=Frame(self.root, bg="black")
        menu_main.place(x=6, y=373, height=37, width=468)
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
                text="News", 
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
                ).place(x=375, y=9, width=85, height=20)

    def tools(self):
        userAlive.writeSS(session)
        userAlive.sendUser(txt_user)
        userAlive.goTodo('tools.py')

userAlive.checking_bar("News, przeglądaj w poszukiwaniu narzędzi ... " + txt_user, 100, 0.01)
root = tkinter.Tk()
area = Obszar_Roboczy(root, txt_user, session)

root.mainloop()