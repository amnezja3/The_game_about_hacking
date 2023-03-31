import userAlive
from getpass import getpass
from time import sleep
import argparse

#####################################        ARGUMETOWANIE SKRYPTU     #####################################
parser = argparse.ArgumentParser(description="Hacker GRA cRPG v1")
parser.add_argument("-l", "--login", type=str, help="Wpowadź login w lini polecen, jeżeli są spacje użej cudzyslowów")
parser.add_argument("-p", "--password", type=str, help="Wpowadź haslo w lini polecen, jeżeli są spacje użej cudzyslowów")
args = parser.parse_args()
hackCrackUSER = args.login
hackCrackPASSWORD = args.password
##################################### ARGUMETOWANIE SKRYPTU ZAKONCZONE #####################################

userAlive.clearConsole()
userAlive.sysColorconsole("0", "8")
try: 
    userAlive.banner("Logowanie", "Rozpoznawanie użytkownika")
except:
    userAlive.czytajTo('Nie jesteś zalogowany', 0.5)
userAlive.literujTo('Nie jesteś zalogowany \n', 0.002)
userAlive.literujTo("Podaj login: \n", 0.01)
userAlive.mowTo("WELCOME")
if hackCrackUSER == None:
    inputNickName = input(">> ")
else:
    inputNickName = hackCrackUSER
giveNickName = inputNickName
userAlive.checking_bar(userAlive.literujTo("SPRAWDZANIE UŻYTKOWNIKA WEBblack", 0.01), 10, 0.003)
login = giveNickName
para = userAlive.dataUserLogin(login)
real_login = str(para[0])
v_login = str(para[1])

userAlive.sysColorconsole("0", "E")
if str(real_login) == str(v_login):    
    userAlive.literujTo("Użytjonik zweryfikowany poprawnie\nWprowadź hasło dla: \n", 0.002)
    userAlive.mowTo("Username correct ..")
    
    if hackCrackPASSWORD == None:
        inputNickpass = getpass(">> " + giveNickName + " >> ")
    else:
        inputNickpass = hackCrackPASSWORD
    givePass = inputNickpass        
    userAlive.checking_bar("WERYFIKACJA HASŁA", 30, 0.003)
    userAlive.sysColorconsole("0", "E")     
    dataPasswords = userAlive.dataPassLogin(giveNickName, givePass)
    standardOne = dataPasswords[0]
    std_pass = dataPasswords[1]
    if str(standardOne) == str(std_pass):              
        userAlive.clearConsole()
        userAlive.banner("Użytkownik rozpoznany", "Zalogowano jako: " + giveNickName)   
        userAlive.sendUser(giveNickName)
        pre_user_login = " <" + giveNickName + "> "
        user_login = pre_user_login
        userAlive.literujTo("Twoje konto zostało poprawnie zalogowane \n", 0.002)
        userAlive.literujTo("[cmd] - otwiera interfejs hackerski \n", 0.001)
        userAlive.literujTo("[cmd --help] - cmd tricks \n", 0.001)
        userAlive.literujTo("[tools] - otwiera interfejs graficzny narzędzi hackerskich \n", 0.001)
        userAlive.literujTo("[panel] - otwiera interfejs graficzny panelu użytkownika \n", 0.001)
        userAlive.literujTo("[lista] - pokaż dostępne opcje \n", 0.001)
        userAlive.literujTo("[exit] - wyloguj się \n", 0.001)
        userAlive.mowTo("Welcome " + giveNickName)
        while True: # root/ 
            print()           
            rootCommand = input("Hack Clonsole @ "+ user_login +"/:>> ")
            if rootCommand == "exit" or rootCommand == "quit" or rootCommand == "0" or rootCommand == "koniec":
                userAlive.mowTo("See You later .. " + giveNickName)
                userAlive.exitSys()

            if rootCommand == "panel":                              
                userAlive.sendUser(giveNickName)
                userAlive.writeSS(giveNickName)
                userAlive.goTodo("panel.py") # najpierw pygame Window
                userAlive.goTodo("profil.py")
                userAlive.goTodo("profesja.py")
                userAlive.goTodo("okolica.py")
                userAlive.goTodo("news.py")                
                userAlive.clearConsole()
                userAlive.banner("Użytkonik", giveNickName )
                userAlive.czytajTo("Utworzono instancję Panelu dla użytkonika " + giveNickName, 0.001)
                userAlive.mowTo("Creating an instance of the User Panel ")
                userAlive.checking_bar("Tworzenie stancji dla " + rootCommand, 30, 0.003)

            if rootCommand == "lista" or rootCommand == "list" or rootCommand == "-l":
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName )
                userAlive.checking_bar("\nTworzenie stancji dla " + rootCommand, 30, 0.003)
                userAlive.czytajTo("\nUtworzono instancję opcji dla użytkonika " + giveNickName + ' \n', 0.001)
                userAlive.mowTo("I'll show you some options ")
                userAlive.listCommand() 
            
            if rootCommand == "info" or rootCommand == "wiadomosci" or rootCommand == "mess":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "dodaj":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "atakuj":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "telefon" or rootCommand == "phone" or rootCommand == "tel" or rootCommand == "mobile":
                userAlive.sendUser(giveNickName)
                userAlive.writeSS(giveNickName)        
                userAlive.clearConsole()    
                userAlive.banner("Użytkonik", giveNickName)            
                userAlive.goTodo("telefon.py")
                userAlive.mowTo("Creating an instance for mobile")
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("running phone ..")
                
            if rootCommand == "darknet":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "traps":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "szukaj" or rootCommand == "scan":
                userAlive.sendUser(giveNickName)
                userAlive.writeSS(giveNickName)        
                userAlive.clearConsole()    
                userAlive.banner("Użytkonik", giveNickName)            
                userAlive.goTodo("szukaj.py")
                userAlive.mowTo("Creating an instance for area scanner")
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Scanning areas ..")
                
            if rootCommand == "publikuj":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "profil":
                userAlive.sendUser(giveNickName)
                userAlive.writeSS(giveNickName)
                userAlive.goTodo("profil.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Utworzono instancję widgetu ", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Creating an instance for player profil")                
                
            if rootCommand == "profesja":
                userAlive.sendUser(giveNickName)
                userAlive.goTodo("profesja.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")            
                
            if rootCommand == "spacer":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "news":
                userAlive.sendUser(giveNickName)
                userAlive.writeSS(giveNickName)
                userAlive.goTodo("news.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Utworzono instancję widgetu ", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Creating an instance for news")
                
            if rootCommand == "uzyj":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "wez":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "plecak":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")                
                
            if rootCommand == "gotowka":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "znajomi":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "wyslij":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "robota":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "zlec":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "handel wirtualny":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "handel fizyczny":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "oferty wirtualne":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "oferty fizyczny":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "okolica" or rootCommand == "idz" or rootCommand == "idź" or rootCommand == "spaceruj" or rootCommand == "go":
                userAlive.sendUser(giveNickName)
                userAlive.writeSS(giveNickName)
                userAlive.goTodo("okolica.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Utworzono instancję dla " + rootCommand, 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Near you ..")
                
            if rootCommand == "mapa":
                userAlive.sendUser(giveNickName)
                userAlive.goTodo("mapa.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("The map is opening right now ..")
                
            if rootCommand == "zapisz":
                # userAlive.sendUser(giveNickName)
                # userAlive.goTodo("cel.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Nie utworzono instancji dla tej opcji", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Invite soon ..")
                
            if rootCommand == "miejsca":
                userAlive.sendUser(giveNickName)
                userAlive.writeSS(giveNickName)
                userAlive.goTodo("miejsca.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Utworzono instancję widgetu ", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Creating an instance for places")
               
                            
            if rootCommand == "dom" or rootCommand == "home" or rootCommand == "baza" or rootCommand == "centrum dowodzenia":
                userAlive.sendUser(giveNickName)
                userAlive.writeSS(giveNickName)
                lokalizacja_dom_y = userAlive.dataUserProfil(giveNickName, 'lokalizacja_dom_y')
                lokalizacja_dom_x = userAlive.dataUserProfil(giveNickName, 'lokalizacja_dom_x')
                aktualna_lokalizacja_y  = userAlive.dataUserProfil(giveNickName, 'aktualna_lokalizacja_y')
                aktualna_lokalizacja_x  = userAlive.dataUserProfil(giveNickName, 'aktualna_lokalizacja_x')
                lokalizacja_terenu_a_y = userAlive.dataUserProfil(giveNickName, 'lokalizacja_terenu_a_y')
                lokalizacja_terenu_a_x = userAlive.dataUserProfil(giveNickName, 'lokalizacja_terenu_a_x')
                lokalizacja_terenu_b_y = userAlive.dataUserProfil(giveNickName, 'lokalizacja_terenu_b_y')
                lokalizacja_terenu_b_x = userAlive.dataUserProfil(giveNickName, 'lokalizacja_terenu_b_x')
                lokalizacja_terenu_c_y = userAlive.dataUserProfil(giveNickName, 'lokalizacja_terenu_c_y')
                lokalizacja_terenu_c_x = userAlive.dataUserProfil(giveNickName, 'lokalizacja_terenu_c_x')
                lokalizacja_terenu_d_y = userAlive.dataUserProfil(giveNickName, 'lokalizacja_terenu_d_y')
                lokalizacja_terenu_d_x = userAlive.dataUserProfil(giveNickName, 'lokalizacja_terenu_d_x')
                userid = userAlive.dataUserSELECT('users_main', '', 'user', giveNickName, 'identyfikator')
                useridforchanged = userid[0]
                # pobierz loc > aktualna, A, B, C
                aktlokY = aktualna_lokalizacja_y
                aktlokX = aktualna_lokalizacja_x                
                # ustaw aktualną ustaw C na D
                userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_y', str(lokalizacja_terenu_c_y), useridforchanged)
                userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_d_x', str(lokalizacja_terenu_c_x), useridforchanged)
                # ustaw aktualną ustaw B na C
                userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_y', str(lokalizacja_terenu_b_y), useridforchanged)
                userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_c_x', str(lokalizacja_terenu_c_x), useridforchanged)
                # ustaw aktualną ustaw A na B
                userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_y', str(lokalizacja_terenu_a_y), useridforchanged)
                userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_b_x', str(lokalizacja_terenu_a_x), useridforchanged)
                # ustaw aktualną ustaw aktualna na A
                userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_y', str(aktlokY), useridforchanged)
                userAlive.dataUserUPDATE('users_main', '', 'lokalizacja_terenu_a_x', str(aktlokX), useridforchanged)
                userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_y', str(lokalizacja_dom_y), useridforchanged)
                userAlive.dataUserUPDATE('users_main', '', 'aktualna_lokalizacja_x', str(lokalizacja_dom_x), useridforchanged)  
                userAlive.goTodo('okolica.py')                
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Utworzono instancję dla " + rootCommand, 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("You are at home .." + giveNickName)
                
            if rootCommand == "tools":
                userAlive.sendUser(giveNickName)
                userAlive.writeSS(giveNickName)
                userAlive.goTodo("tools.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Utworzono instancję widgetu ", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Creating an instance for tools")
            
            if rootCommand == "cmd" or rootCommand == "console" or rootCommand == "hack line" or rootCommand == "command" or rootCommand == "konsola" or rootCommand == "linia" or rootCommand == "terminal" or rootCommand == "poprostu terminal":
                userAlive.sendUser(giveNickName)
                userAlive.writeSS(giveNickName)
                userAlive.goTodo("hackConsole.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Utworzono instancję hackerConsole ", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Creating an instance for hacker Console")
            
            if rootCommand == "cmd --help" or rootCommand == "cmd tricks" or rootCommand == "hack tricks" or rootCommand == "command triks" or rootCommand == "konsola triki" or rootCommand == "linia triki" or rootCommand == "terminal triki":
                userAlive.sendUser(giveNickName)
                userAlive.writeSS(giveNickName)
                userAlive.goTodo("hackconsoletricks.py")
                userAlive.clearConsole()                
                userAlive.banner("Użytkonik", giveNickName)
                userAlive.czytajTo("Utworzono instancję hackerConsole ", 0.001)                
                userAlive.checking_bar("Tworzenie instancji dla " + rootCommand, 30, 0.003)
                userAlive.mowTo("Creating an instance for hacker Console Tricks")
            

    else:
        userAlive.clearConsole()
        userAlive.sysColorconsole("0", "6", "WERYFIKACJA HASŁA NIE POWIODŁA SIĘ")
        userAlive.banner("Użytkownik nie rozpoznany!!", "Niezalogowano: " + giveNickName)
        print("Złe haslo")
        while True:
            userAlive.clearConsole()
            userAlive.banner("Użytkownik nie rozpoznany!!", "Niezalogowano: " + giveNickName)
            print("Dostepne HackTools")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("[Victimus-777V13] - Accounts Cracker!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")        
            hacktools_Y_or_N = input("Czy chcesz użyć Victimus-777V13? [ Yes or No ]\n#:/>>> ")    
            if hacktools_Y_or_N == "y" or hacktools_Y_or_N == "Yes" or hacktools_Y_or_N == "yes" or hacktools_Y_or_N == "YEs" or hacktools_Y_or_N == "YES" or hacktools_Y_or_N == "YeS" or hacktools_Y_or_N == "yES":                
                userAlive.clearConsole()
                userAlive.sysColorconsole("0", "E", "HackTools")
                userAlive.banner("Użytkownik nie rozpoznany!!", "Niezalogowano: " + giveNickName)
                zw_mixer_hac = userAlive.mixer(0, 75)
                userAlive.checking_bar("Ładowanie słowników VictimusDICT", 500, 0.01)
                userAlive.checking_bar("Przygotowanie środowiska VictimusSystem", 100, 0.003)
                userAlive.checking_bar("Weryfikacja środowiska VictimusSystem", 100, 0.003)
                userAlive.checking_bar("Integracja środowiska VictimusSystem", 100, 0.003)
                userAlive.checking_bar("Generowanie skryptów VictimusScr", 3200, 0.003)
                userAlive.checking_bar("Cracking Users by Accounts Cracker!", userAlive.mixer(5000, 75000), 0.003)                        
                while True:
                    if zw_mixer_hac == 0:
                        userAlive.sysColorconsole("0", "A", "HackTools")                   
                        victimus = userAlive.victimusTool()
                        victimUser = victimus[0]
                        victimpass = victimus[1]                    
                        pausa = input("HackTools: Victimus-777 (Accounts Cracker! v13)\nZłamano hasło użytkownikowi " + victimUser + ".\nPress ENTER loguj jako " + victimUser + "\n[exit] - porzuć sesje\n#:/>>> ")
                        if pausa == "exit":
                            userAlive.restartGame()
                        else:
                            userAlive.goTodo("hacker.py -l "+str(victimUser)+" -p "+str(victimpass))
                            break
                    else:   
                        userAlive.sysColorconsole("0", "4", "HackTools")                 
                        pausa = input("HackTools: Victimus-777 (Accounts Cracker! v13)\nOperacja zakończona niepowodzeniem.\nPress ENTER - porzuć sesje")                        
                        break            
            elif hacktools_Y_or_N == "n" or hacktools_Y_or_N == "No" or hacktools_Y_or_N == "no" or hacktools_Y_or_N == "NO" or hacktools_Y_or_N == "nO" or hacktools_Y_or_N == "N0" or hacktools_Y_or_N == "n0":
                userAlive.restartGame()
            else:
                userAlive.restartGame()
else:
    login_wlasciwy = "nie"
    userAlive.clearConsole()
    userAlive.banner("Użytkownik nie rozpoznany!!", "Niezalogowano: " + giveNickName)
    userAlive.czytajTo("Nie ma jeszcze użytkownika o takim nicku. \n", 0.02)
    userAlive.literujTo("Czy chesz zarejestowan się pod nickiem " + giveNickName + "\n", 0.002)
    userAlive.mowTo("Wanna you add " + giveNickName + " as new user?")
    rejestruj_Y_or_N = input("Yes or No ?\n#:/>>> ")
    
    if rejestruj_Y_or_N == "y" or rejestruj_Y_or_N == "Yes" or rejestruj_Y_or_N == "yes" or rejestruj_Y_or_N == "YEs" or rejestruj_Y_or_N == "YES" or rejestruj_Y_or_N == "YeS" or rejestruj_Y_or_N == "yES":
        nowy_user_login = giveNickName
        userAlive.clearConsole()
        userAlive.banner("Użytkownik nie rozpoznany!!", "Niezalogowano: " + giveNickName)
        newUserPassone = getpass("Wprowadź haslo dla loginu " + giveNickName + ": ")
        newUserPasstwo = getpass("Powtórz haslo dla loginu " + giveNickName + ": ")
        if newUserPassone == newUserPasstwo:
            userAlive.clearConsole()
            userAlive.banner("Użytkownik nie rozpoznany!!", "Niezalogowano: " + giveNickName)
            userAlive.literujTo("Pdane hasla są zgodne.\n", 0.003)
            newUserPass = newUserPasstwo
        if newUserPassone != newUserPasstwo:
            userAlive.clearConsole()
            userAlive.sysColorconsole("0", "4", "Pdane hasla NIE są zgodne. Spróbuj jeszcze raz")
            userAlive.banner("Użytkownik nie rozpoznany!!", "Niezalogowano: " + giveNickName)
            userAlive.literujTo("Pdane hasla NIE są zgodne. Spróbuj jeszcze raz\n", 0.003)
            newUserPassone1 = getpass("Wprowadź haslo dla loginu " + giveNickName + ": ")
            newUserPasstwo1 = getpass("Powtórz haslo dla loginu " + giveNickName + ": ")
            if newUserPassone1 == newUserPasstwo1:
                userAlive.clearConsole()
                userAlive.banner("Użytkownik nie rozpoznany!!", "Niezalogowano: " + giveNickName)
                userAlive.literujTo("Pdane hasla są zgodne. \n", 0.003)
                newUserPass = newUserPasstwo1
            if newUserPassone1 != newUserPasstwo1:
                sleep(0.1)
                userAlive.restartGame()
        new_user = str(v_login)        
        newUserPass = newUserPassone
        if new_user == "set()":
            userAlive.dataUserAdd(giveNickName, newUserPass)
            userAlive.clearConsole()
            userAlive.banner("Rejestracja nowego uzytkownika", "Przyszły login to: " + giveNickName)
            print("Konto dla loginu " + giveNickName + " zostalo utworzone.")     
            sleep(3)
            userAlive.restartGame()

    if rejestruj_Y_or_N == "n" or rejestruj_Y_or_N == "No" or rejestruj_Y_or_N == "no" or rejestruj_Y_or_N == "NO" or rejestruj_Y_or_N == "nO" or rejestruj_Y_or_N == "N0" or rejestruj_Y_or_N == "n0":    
        while True:
            userAlive.clearConsole()
            userAlive.banner("Użytkownik nie rozpoznany!!", "Niezalogowano: " + giveNickName)
            print("Dostepne HackTools")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("[Victimus-777V13] - Accounts Cracker!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")        
            hacktools_Y_or_N = input("Czy chcesz użyć Victimus-777V13? [ Yes or No ]\n#:/>>> ")    
            if hacktools_Y_or_N == "y" or hacktools_Y_or_N == "Yes" or hacktools_Y_or_N == "yes" or hacktools_Y_or_N == "YEs" or hacktools_Y_or_N == "YES" or hacktools_Y_or_N == "YeS" or hacktools_Y_or_N == "yES":                
                userAlive.clearConsole()    
                userAlive.banner("Użytkownik nie rozpoznany!!", "Niezalogowano: " + giveNickName)
                zw_mixer_hac = userAlive.mixer(0, 15)
                userAlive.checking_bar("Ładowanie słowników VictimusDICT", 500, 0.01)
                userAlive.checking_bar("Przygotowanie środowiska VictimusSystem", 100, 0.003)
                userAlive.checking_bar("Weryfikacja środowiska VictimusSystem", 100, 0.003)
                userAlive.checking_bar("Integracja środowiska VictimusSystem", 100, 0.003)
                userAlive.checking_bar("Generowanie skryptów VictimusScr", 3200, 0.003)
                userAlive.checking_bar("Cracking Users by Accounts Cracker!", userAlive.mixer(5000, 75000), 0.003)                                   
                while True:
                    if zw_mixer_hac == 0:
                        userAlive.sysColorconsole("0", "A", "HackTools")          
                        victimus = userAlive.victimusTool()
                        victimUser = victimus[0]
                        victimpass = victimus[1]                    
                        pausa = input("HackTools: Victimus-777 (Accounts Cracker! v13)\nZłamano hasło użytkownikowi " + victimUser + ".\nPress ENTER loguj jako " + victimUser + "\n[exit] - porzuć sesje\n#:/>>> ")
                        if pausa == "exit":
                            userAlive.restartGame()
                        else:
                            userAlive.goTodo("hacker.py -l "+str(victimUser)+" -p "+str(victimpass))
                            break
                    else:                    
                        userAlive.sysColorconsole("0", "4", "HackTools")
                        pausa = input("HackTools: Victimus-777 (Accounts Cracker! v13)\nOperacja zakończona niepowodzeniem.\nPress ENTER - porzuć sesje\n#:/>>> ")                        
                        break                   
            elif hacktools_Y_or_N == "hack" or hacktools_Y_or_N == "crack" or hacktools_Y_or_N == "broke" or hacktools_Y_or_N == "force" or hacktools_Y_or_N == "takeall" or hacktools_Y_or_N == "fuck" or hacktools_Y_or_N == "hacking":                
                userAlive.clearConsole()    
                userAlive.banner("Użytkownik nie rozpoznany!!", "Niezalogowano: " + giveNickName)
                zw_mixer_hac = userAlive.mixer(0, 3)
                userAlive.checking_bar("Ładowanie słowników VictimusDICT", 500, 0.01)
                userAlive.checking_bar("Przygotowanie środowiska VictimusSystem", 100, 0.003)
                userAlive.checking_bar("Weryfikacja środowiska VictimusSystem", 100, 0.003)
                userAlive.checking_bar("Integracja środowiska VictimusSystem", 100, 0.003)
                userAlive.checking_bar("Generowanie skryptów VictimusScr", 300, 0.003)
                userAlive.checking_bar("Cracking Users by Accounts Cracker!", userAlive.mixer(50, 7500), 0.003)                                   
                while True:
                    if zw_mixer_hac == 0:
                        userAlive.sysColorconsole("0", "A", "HackTools")          
                        victimus = userAlive.victimusTool()
                        victimUser = victimus[0]
                        victimpass = victimus[1]                    
                        pausa = input("HackTools: Victimus-777 (Accounts Cracker! v13)\nZłamano hasło użytkownikowi " + victimUser + ".\nPress ENTER loguj jako " + victimUser + "\n[exit] - porzuć sesje\n#:/>>> ")
                        if pausa == "exit":
                            userAlive.restartGame()
                        else:
                            userAlive.goTodo("hacker.py -l "+str(victimUser)+" -p "+str(victimpass))
                            break
                    else:                    
                        userAlive.sysColorconsole("0", "4", "HackTools")
                        pausa = input("HackTools: Victimus-777 (Accounts Cracker! v13)\nOperacja zakończona niepowodzeniem.\nPress ENTER - porzuć sesje\n#:/>>> ")                        
                        break    
            elif hacktools_Y_or_N == "n" or hacktools_Y_or_N == "No" or hacktools_Y_or_N == "no" or hacktools_Y_or_N == "NO" or hacktools_Y_or_N == "nO" or hacktools_Y_or_N == "N0" or hacktools_Y_or_N == "n0":
                userAlive.restartGame()
            else:
                userAlive.restartGame()
    userAlive.restartGame()

    

