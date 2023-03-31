import userAlive
import argparse
import os

parser = argparse.ArgumentParser(description="Hacker GRA cRPG v1")
parser.add_argument("-ip", "--internetProtocol", type=str, help="Wpowadź login w lini polecen, jeżeli są spacje użej cudzyslowów")
args = parser.parse_args()
hackCrackIP = args.internetProtocol

giveuser = userAlive.giveUser()
userAlive.clearConsole()



if hackCrackIP == None:
    print('Wprowadź IP do sforsowania')
    victimIP = input(' >>>')
    ipGood = userAlive.checkIpNumber(victimIP)
    try:
        if ipGood[0] == True and ipGood[1] == True and ipGood[2] == True and ipGood[3] == True:
            victimIP = victimIP
            os.system('start ping ' + victimIP)
        else:
            print('Podany adres nie jest IP, sprawdź adres i spróbuj ponownie!')
            userAlive.exitSys()
    except:
        print('Podany adres nie jest IP, sprawdź adres i spróbuj ponownie!')
        userAlive.exitSys()
else:
    victimIP = str(hackCrackIP)
    print('IP '+ hackCrackIP +' do sforsowania')
    os.system('start ping ' + victimIP)



victimuses = userAlive.verifityTarget('targets', victimIP)
while True:
    if victimuses == True:
        userAlive.clearConsole()
        userAlive.sysColorconsole('0', 'D')
        los = userAlive.mixer(0, 4)
        if los == 1:
            userAlive.sysColorconsole('0', 'A')
            print('Aktywny attack na IP')
            userAlive.checking_bar('Budowanie środowiska QtpF dla ' + victimIP, 100, 0.1)
            userAlive.checking_bar('Wyszukiwanie Backdoors dla ' + victimIP, 100, 0.1)
            userAlive.checking_bar('Wyszukiwanie dostępnych exploits dla ' + victimIP, 100, 0.1)

            userid = userAlive.dataUserSELECT('users_main', '', 'user', giveuser, 'identyfikator')
            useridforchanged = userid[0]
            poziom = userAlive.dataUserProfil(giveuser, 'aktualny_poziom')
            pktDos = userAlive.dataUserProfil(giveuser, 'punkty_doswiadczenia')
            vcoins = userAlive.dataUserProfil(giveuser, 'aktualne_vcoin')
            attack_failds = userAlive.dataUserProfil(giveuser, 'attack_failds')
            attack_success = userAlive.dataUserProfil(giveuser, 'attack_success')
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

            print("Uzyskano dostep przez exploit. Połaczenie nie jest stabilne i \nmoże zostać nieoczekiwanie zerwane.")
            print("POŁĄCZENIE ZDALNE")
            print()
            print('Zdobyłeś kolejny poziom')
            print("Na zhackowaniu tego IP zarobiłeś :V$" + str(zysk))
            print("Twoje doświadczenie zwiększa się o " + str(dos))
            userAlive.checking_bar('Zapisywanie wyniku ' + victimIP, 100, 0.1)

            attack_failds += 1
            attack_success += 1
            przychod = zysk + vcoins
            dosUp = dos + pktDos
            poziomUp = poziom + 1

            userAlive.dataUserUPDATE('users_main', '', 'attack_success', str(attack_success), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'aktualne_vcoin', str(przychod), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'punkty_doswiadczenia', str(dosUp), useridforchanged)
            userAlive.dataUserUPDATE('users_main', '', 'aktualny_poziom', str(poziomUp), useridforchanged)
            
            port = userAlive.dataUserSELECT('targets','','ip_url', str(victimIP), 'port')
            adress = '"http://' + port[0] +'"'
            userAlive.goTodo('StreethackerBrowser.py -a ' + adress)
            userAlive.exitSys()
        else:        
            userAlive.checking_bar('Budowanie środowiska QtpF dla ' + victimIP, 100, 0.1)
            userAlive.checking_bar('Wyszukiwanie Backdoors dla ' + victimIP, 100, 0.1)
            


    if victimuses == None:
        userAlive.clearConsole()
        userAlive.checking_bar('Wywoływanie serwera ' + victimIP, 100, 0.1)
        userAlive.checking_bar('Próba nawiązania połaczenia z ' + victimIP, 100, 0.1)
        userAlive.clearConsole()
        print('Nawiązywanie połaczenia z wybranym serwerem trawło zbyt długo. Ponawianie zostało przerwane. \nSprawdź ping dla ' + victimIP + ' lub upewnij się, że komputer jest podłaczony do sieci.')
        choice = input(" Czy chcesz użyć narzedzia IP scanner w poszukiwaniu podatności? [TAK / NIE] \n>>>")
        if choice == 'Tak' or choice == 'tak'or choice == 't' or choice == 'y' or choice == 'yes':
            userAlive.writeSS(giveuser)
            userAlive.sendUser(giveuser)
            userTool = userAlive.verifityTools('dostepne_tools', str(giveuser), 'kolumna1', 'IP scanner', 'kolumna4')        
            if userTool != None:            
                userAlive.goTodo('ipscanner.py')            
            else:            
                userAlive.goTodo('download.py -t ' + '"IP scanner"')            
        userAlive.exitSys()
 