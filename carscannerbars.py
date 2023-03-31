import userAlive
import time
import random
from time import sleep

giveNickName = userAlive.giveUser()
session = userAlive.giveSS()

userAlive.clearConsole()
userAlive.sysColorconsole("0", "2", "Uruchomiona instancja")

userAlive.checking_bar("[ Przetwarzanie zebranych informacji ]", 100, 0.2)
userAlive.checking_bar("[ Wykrywanie błedów zabezpieczeń ]", 300, 0.01)
userAlive.checking_bar("[ Generowanie raportu ze scanowania ]", 300, 0.01)

userAlive.clearConsole()
userAlive.checking_bar("Generowanie Raportu", 20, 0.05)
userAlive.clearConsole()
# userAlive.banner("Raport ze skanowania pozjazdu", "Autoryzacja: " + giveNickName)                                                        
raport_czas = time.ctime(time.time())                                                        
print("RAPORT")
print("----------------------------------------------------------")
print("DATA: " + str(raport_czas))
print("----------------------------------------------------------")
raport_losowy_pasmo = random.randrange(200) 
print("Wykryto " + str(raport_losowy_pasmo) + " pasma radiowe bez babezpiezeń.")                                                        
raport_losowy_immo = random.randrange(80) 
print("Wykryto " + str(raport_losowy_immo) + " luk w systemie immobilaizera.")                                                        
raport_losowy_ultra = random.randrange(3) 
print("Jest " + str(raport_losowy_ultra) + " możliwości przejęcia zdalnej kontroli nad pojazdem.")                                                        
raport_losowy_sys = random.randrange(400) 
print("System posiada " + str(raport_losowy_sys) + " nieaktualnych modułów i sterowników.")
print("----------------------------------------------------------")
print("KONIEC RAPORTU")
print("----------------------------------------------------------")
print("\n")
print("Czy chcesz rozpocząć hackowanie [Tak / Nie] ")
usch = input(">>> ")
userAlive.clearConsole()
userid = userAlive.dataUserSELECT('users_main', '', 'user', giveNickName, 'identyfikator')
useridforchanged = userid[0]
poziom = userAlive.dataUserProfil(giveNickName, 'aktualny_poziom')
pktDos = userAlive.dataUserProfil(giveNickName, 'punkty_doswiadczenia')
vcoins = userAlive.dataUserProfil(giveNickName, 'aktualne_vcoin')
attack_failds = userAlive.dataUserProfil(giveNickName, 'attack_failds')
attack_success = userAlive.dataUserProfil(giveNickName, 'attack_success')
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
zysk = mnoznik * poziom
dos = (zysk + mnoznik) * 3
attack_failds += 1
attack_success += 1
if usch == "tak" or usch == "Tak" or usch == "TAK" or usch == "ta" or usch == "t" or usch == "y" or usch == "yes":    
    userAlive.checking_bar("Próba wejścia przy użyciu pasma radiowego.", 100, 0.05)
    take = userAlive.sukces()
    if raport_losowy_pasmo > 0 and take == "Ukończono z powodzeniem":
        take = userAlive.sukces()
        zobaczyl = ['przejeżdzający radiowów', 'staruszkę', 'społeczniaka', 'właściciela']
        kto = zobaczyl[userAlive.mixer(0,4)]
        if take == "Ukończono z powodzeniem":
            print("Próba wejścia przy użyciu pasma radiowego zakończona powodzeniem.")
            print("GRATULACJE! POJAZD ZOSTAŁ ZHAKOWANY")
            print()
            print('Zdobyłeś kolejny poziom')
            print("Na zhackowaniu tego pojazdu zarobiłeś :V$" + str(zysk))
            print("Twoje doświadczenie zwiększa się o " + str(dos))
            przychod = zysk + vcoins
            dosUp = dos + pktDos
            poziomUp = poziom + 1
            userAlive.dataUserUPDATE('users_main', '', 'attack_success', str(attack_success), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'aktualne_vcoin', str(przychod), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'punkty_doswiadczenia', str(dosUp), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'aktualny_poziom', str(poziomUp), useridforchanged)
            sleep(10)
            userAlive.exitSys()
        else:
            print("WYŁAPAŁEŚ PRZYPAŁ! Zostałeś zauważony przez " + kto + '.')
            print("Interweniowała policja i zostałeś aresztowny. \nMusiałeś zapłacić adwokatowi V$" + str(int(zysk * 2)))
            koszty = vcoins - (zysk * 2)
            if koszty <= 0:
                koszty = 0
            userAlive.dataUserUPDATE('users_main', '', 'aktualne_vcoin', str(koszty), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'attack_failds', str(attack_failds), useridforchanged)            
            sleep(10)
            userAlive.exitSys()

    userAlive.checking_bar("Próba wejścia przy użyciu luk w systemie immobilaizera.", 100, 0.05)
    take = userAlive.sukces()
    if raport_losowy_immo > 0 and take == "Ukończono z powodzeniem":
        take = userAlive.sukces()
        zobaczyl = ['przejeżdzający radiowów', 'staruszkę', 'społeczniaka', 'właściciela']
        kto = zobaczyl[userAlive.mixer(0,4)]
        if take == "Ukończono z powodzeniem":
            print("Próba wejścia przy użyciu luk w systemie immobilaizera zakończona powodzeniem.")
            print("GRATULACJE! POJAZD ZOSTAŁ ZHAKOWANY")
            print()
            print('Zdobyłeś kolejny poziom')
            print("Na shackowaniu tego pojazdu zarobiłeś :V$" + str(zysk))
            print("Twoje doświadczenie zwiększa się o " + str(dos))
            przychod = zysk + vcoins
            dosUp = dos + pktDos
            poziomUp = poziom + 1
            userAlive.dataUserUPDATE('users_main', '', 'attack_success', str(attack_success), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'aktualne_vcoin', str(przychod), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'punkty_doswiadczenia', str(dosUp), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'aktualny_poziom', str(poziomUp), useridforchanged)
            sleep(10)
            userAlive.exitSys()
        else:
            print("WYŁAPAŁEŚ PRZYPAŁ! Zostałeś zauważony przez " + kto + '.')
            print("Interweniowała policja i zostałeś aresztowny. \nMusiałeś zapłacić adwokatowi V$" + str(int(zysk * 2)))
            koszty = vcoins - (zysk * 2)
            if koszty <= 0:
                koszty = 0
            userAlive.dataUserUPDATE('users_main', '', 'aktualne_vcoin', str(koszty), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'attack_failds', str(attack_failds), useridforchanged)            
            sleep(10)
            userAlive.exitSys()
    
    userAlive.checking_bar("Próba przejęcia zdalnej kontroli nad pojazdem.", 100, 0.05)
    take = userAlive.sukces()
    if raport_losowy_immo > 0 and take == "Ukończono z powodzeniem":
        take = userAlive.sukces()
        zobaczyl = ['przejeżdzający radiowów', 'staruszkę', 'społeczniaka', 'właściciela']
        kto = zobaczyl[userAlive.mixer(0,4)]
        if take == "Ukończono z powodzeniem":
            print("Próba wejścia przy użyciu luk w systemie immobilaizera zakończona powodzeniem.")
            print("GRATULACJE! POJAZD ZOSTAŁ ZHAKOWANY")
            print()
            print('Zdobyłeś kolejny poziom')
            print("Na shackowaniu tego pojazdu zarobiłeś :V$" + str(zysk))
            print("Twoje doświadczenie zwiększa się o " + str(dos))
            przychod = zysk + vcoins
            dosUp = dos + pktDos
            poziomUp = poziom + 1
            userAlive.dataUserUPDATE('users_main', '', 'attack_success', str(attack_success), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'aktualne_vcoin', str(przychod), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'punkty_doswiadczenia', str(dosUp), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'aktualny_poziom', str(poziomUp), useridforchanged)
            sleep(10)
            userAlive.exitSys()
        else:
            print("WYŁAPAŁEŚ PRZYPAŁ! Zostałeś zauważony przez " + kto + '.')
            print("Interweniowała policja i zostałeś aresztowny. \nMusiałeś zapłacić adwokatowi V$" + str(int(zysk * 2)))
            koszty = vcoins - (zysk * 2)
            if koszty <= 0:
                koszty = 0
            userAlive.dataUserUPDATE('users_main', '', 'aktualne_vcoin', str(koszty), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'attack_failds', str(attack_failds), useridforchanged)            
            sleep(10)
            userAlive.exitSys()
        
    userAlive.checking_bar("Próba wejścia za pomocą nieaktualnych modułów i sterowników.", 100, 0.05)
    take = userAlive.sukces()
    if raport_losowy_immo > 0 and take == "Ukończono z powodzeniem":
        take = userAlive.sukces()
        zobaczyl = ['przejeżdzający radiowów', 'staruszkę', 'społeczniaka', 'właściciela']
        kto = zobaczyl[userAlive.mixer(0,4)]
        if take == "Ukończono z powodzeniem":
            print("Próba wejścia za pomocą nieaktualnych modułów i sterowników zakończona powodzeniem.")
            print("GRATULACJE! POJAZD ZOSTAŁ ZHAKOWANY")
            print()
            print('Zdobyłeś kolejny poziom')
            print("Na shackowaniu tego pojazdu zarobiłeś :V$" + str(zysk))
            print("Twoje doświadczenie zwiększa się o " + str(dos))
            przychod = zysk + vcoins
            dosUp = dos + pktDos
            poziomUp = poziom + 1
            userAlive.dataUserUPDATE('users_main', '', 'attack_success', str(attack_success), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'aktualne_vcoin', str(przychod), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'punkty_doswiadczenia', str(dosUp), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'aktualny_poziom', str(poziomUp), useridforchanged)
            sleep(10)
            userAlive.exitSys()
        else:
            print("WYŁAPAŁEŚ PRZYPAŁ! Zostałeś zauważony przez " + kto + '.')
            print("Interweniowała policja i zostałeś aresztowny. \nMusiałeś zapłacić adwokatowi V$" + str(int(zysk * 2)))
            koszty = vcoins - (zysk * 2)
            if koszty <= 0:
                koszty = 0
            userAlive.dataUserUPDATE('users_main', '', 'aktualne_vcoin', str(koszty), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'attack_failds', str(attack_failds), useridforchanged)            
            sleep(10)
            userAlive.exitSys()        

    else:
        take = userAlive.sukces()
        zobaczyl = ['przejeżdzający radiowów', 'staruszkę', 'społeczniaka', 'właściciela']
        kto = zobaczyl[userAlive.mixer(0,4)]
        if take == "Ukończono z powodzeniem":
            print("POJAZD NIE ZOSTAŁ ZHAKOWANY!")
            userAlive.dataUserUPDATE('users_main', '', 'attack_failds', str(attack_failds), useridforchanged)
            sleep(10)
            userAlive.exitSys()
        else:
            print("WYŁAPAŁEŚ PRZYPAŁ! Zostałeś zauważony przez " + kto + '.')
            print("Interweniowała policja i zostałeś aresztowny. \nMusiałeś zapłacić adwokatowi V$" + str(int(zysk * 2)))
            koszty = vcoins - (zysk * 2)
            if koszty <= 0:
                koszty = 0
            userAlive.dataUserUPDATE('users_main', '', 'aktualne_vcoin', str(koszty), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'attack_failds', str(attack_failds), useridforchanged)            
            sleep(10)
            userAlive.exitSys()
else:
    userAlive.exitSys()