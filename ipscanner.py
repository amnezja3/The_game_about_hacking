import userAlive as uA
import time

giveuser = uA.giveUser()
uA.clearConsole()
uA.sysColorconsole('0', 'E')
uA.checking_bar('Ładowanie IP Scanner', 100, 0.0025)
print()
startIPScaner = input('Czy chcesz rozpocząć scan internetu? [ Tak / Nie ]')
uA.clearConsole()
while True:
    while True:
        if startIPScaner == 'Tak' or startIPScaner == 'tak'or startIPScaner == 't' or startIPScaner == 'y' or startIPScaner == 'yes':
            uA.clearConsole()
            uA.checking_bar('IP Scanner przeszukuje internet w poszukiwaniu podatności', 100, 0.025)
            los = uA.mixer(0, 21)
            if los == 1:
                uA.clearConsole()
                uA.sysColorconsole('0', 'A')
                getTargetIP = uA.dataGeneral('targets', 'ip_url')
                getTargetCat = uA.dataGeneral('targets', 'category')
                lendingIPs = len(getTargetIP)
                losIP = uA.mixer(0, lendingIPs)
                getIP = getTargetIP[losIP]
                getCategoryIP = getTargetCat[losIP]
                uA.checking_bar('Pobieranie znacznika', 100, 0.1)
                uA.czytajTo('Wykryto podatność IP - możliwy zdalny dostęp do ' + getCategoryIP, 0.06)        
                choice = input("Czy chcesz zaatakować IP:"+ getIP +" narzędziem Q-type finder? [TAK / NIE] \n>>>")    
                if choice == 'Tak' or choice == 'tak'or choice == 't' or choice == 'y' or choice == 'yes':
                    uA.writeSS(giveuser)
                    uA.sendUser(giveuser)
                    userTool = uA.verifityTools('dostepne_tools', giveuser, 'kolumna1', 'Q-type finder', 'kolumna4')
                    if userTool != None:
                        print(userTool)
                        uA.goTodo('qtypefinder.py -ip "' + str(getIP)+'"')
                        uA.exitSys()
                    else:                
                        uA.goTodo('download.py --tool ' + '"Q-type finder"')
                        print('W procesie scanowania wykryto podatność IP:' + str(getIP) + "\n Q-type finder shout be downloading.. Wait")
                        choice = input("[ ENTER ] Kontynuj manualnie po zainstalowaniu narzędzia Q-type finder\n >>>")
                else:
                    restartIPScaner = input('[ ENTER ] ponowny scan internetu?')
                    break
        else:
            uA.exitSys()
