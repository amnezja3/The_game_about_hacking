import userAlive
import time
import argparse

parser = argparse.ArgumentParser(description="Hacker GRA cRPG v1")
parser.add_argument("-b", "--bluetoothNick", type=str, help="Wpowadź nick  dla lokacji w lini polecen, jeżeli są spacje użej cudzyslowów")
args = parser.parse_args()
hackCrackBluetooth = args.bluetoothNick

giveuser = userAlive.giveUser()
userAlive.clearConsole()
userAlive.sysColorconsole('0', 'B')

if hackCrackBluetooth == None:
    print('Wprowadź nick ofiary w celu zainstalowania znacznika, na zlokalizowanym telefonie.')
    print('[hack blue] - Otwórz Gui Panel dla Bluetooth Detector 600V')
    victimNick = input(' >>>')   
    if victimNick == 'hack blue' or victimNick == 'hack gui' or victimNick == 'open gui' or victimNick == 'skip it now':
        userAlive.goTodo('bluetoothdetector600Vgui.py')
        userAlive.exitSys() 
else:    
    victimNick = str(hackCrackBluetooth)



try:
    victimuses = userAlive.detectOterHacker(giveuser)
    if victimNick in victimuses.keys():
        print('Inicjalizowanie operacji')
    else:
        print('Hacker ' + victimNick + ' nie został wykryty w tej lokalizacji')
        userAlive.checking_bar('Operacja zakończona', 100, 0.01)
        userAlive.exitSys()


except:
    victimuses = {}
    if victimuses == {} or victimNick == "":
        print('Coś poszło nie źle, nie wykryto podatności')
        userAlive.checking_bar('Operacja zakończona', 100, 0.01)
        userAlive.exitSys()



while True:    
    userAlive.sysColorconsole('0', 'B')
    los = userAlive.mixer(0, 51)
    userAlive.clearConsole()
    userAlive.checking_bar('Nawiązywanie połączenia bluetooth z ' + victimNick + '. Praca w tle.', 100, 0.01)
    if los == 0 or los == 1: 
        userAlive.clearConsole()
        userAlive.sysColorconsole('0', 'A')
        userAlive.checking_bar('Instalowanie znacznika dla telefonu ' + victimNick, 100, 0.1)

        userAlive.writeSS(giveuser)
        userAlive.sendUser(giveuser)
        
        userid = userAlive.dataUserSELECT('users_main', '', 'user', giveuser, 'identyfikator')
        useridforchanged = userid[0]
        poziom = userAlive.dataUserProfil(giveuser, 'aktualny_poziom')
        pktDos = userAlive.dataUserProfil(giveuser, 'punkty_doswiadczenia')
        vcoins = userAlive.dataUserProfil(giveuser, 'aktualne_vcoin')
        attack_failds = userAlive.dataUserProfil(giveuser, 'attack_failds')
        attack_success = userAlive.dataUserProfil(giveuser, 'attack_success')

        userAlive.dataUserCREATE6("selected_targets", giveuser)

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
        dos = (zysk + mnoznik) * 1
        
        print("Uruchamianie Bluetooth Detector 600V")
        print()
        print('Zdobyłeś kolejny poziom')
        print("Na namierzenie telefonu zarobiłeś :V$" + str(zysk))
        print("Twoje doświadczenie zwiększa się o " + str(dos))
        userAlive.checking_bar('Zapisywanie wyniku ' + victimNick, 100, 0.1)

        attack_failds += 1
        attack_success += 1
        przychod = zysk + vcoins
        dosUp = dos + pktDos
        poziomUp = poziom + 1

        userAlive.dataUserUPDATE('users_main', '', 'attack_success', str(attack_success), str(useridforchanged))
        userAlive.dataUserUPDATE('users_main', '', 'aktualne_vcoin', str(przychod), str(useridforchanged))
        userAlive.dataUserUPDATE('users_main', '', 'punkty_doswiadczenia', str(dosUp), str(useridforchanged))
        userAlive.dataUserUPDATE('users_main', '', 'aktualny_poziom', str(poziomUp), str(useridforchanged))

        userAlive.dataUserINSERT6('selected_targets', str(giveuser), str(victimNick), 'Bluetooth Detector 600V', 'NULL', "NULL", "NULL", "NULL")
        print("Target "+ victimNick + " oznaczony!")


        userAlive.goTodo('bluetoothdetector600Vgui.py')


        break
