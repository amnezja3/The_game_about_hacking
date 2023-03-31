import userAlive

giveuser = userAlive.giveUser()
victimuses = userAlive.detectOterHacker(giveuser)

# userAlive.checking_bar('narzedzie w budowie', 100, 0.0025)

userAlive.clearConsole()
userAlive.sysColorconsole('0', '6', 'Air SCANNER 9000B')


loops = len(victimuses)
if loops == 0:
    userAlive.checking_bar('Wyszukiwanie aktywności', 100, 0.1)
    userAlive.sysColorconsole('0', '4', 'Air SCANNER 9000B')
    userAlive.clearConsole()
    userAlive.checking_bar('Nie wykryto aktywności! Zamykanie narzedzia...', 100, 0.1)
    userAlive.exitSys()

selectVictim = userAlive.mixer(0, loops)

victimus = []
for i in victimuses.keys():
    victimus.append(i)

for x in range(21):
    los = userAlive.mixer(0, 50)
    if los == 1:
        userAlive.clearConsole()
        userAlive.sysColorconsole('0', '2', 'Air SCANNER 9000B')
        victoruses = victimus[selectVictim]
        print('Znaleziono aktywność w kwadracie ' + str(x))
        print('racie ' + str(victoruses))
        userAlive.checking_bar('Szczególowe wyszukiwanie aktywności radiowej', 1000, 0.001)
        userAlive.checking_bar('Szczególowe badanie aktywności w sieciach WiFi', 1000, 0.001)
        userAlive.checking_bar('Szczególowe przeszukiwanie sieci lokalnych', 1000, 0.001)
        userAlive.checking_bar('Szczególowy scan aktywności GPS', 1000, 0.001)
        userAlive.checking_bar('Szczególowe wyszukiwanie aktywności satelitarnej', 1000, 0.001)       
        
        choice = input('Wykryto hackera ' + victoruses + " Czy chcesz go zaatakować narżedziem Victimus 888? [TAK / NIE] \n>>>")
        if choice == 'Tak' or choice == 'tak'or choice == 't' or choice == 'y' or choice == 'yes':
            userAlive.writeSS(giveuser)
            userAlive.sendUser(giveuser)
            userTool = userAlive.verifityTools('dostepne_tools', giveuser, 'kolumna1', 'Victimus 888', 'kolumna4')
            if userTool != None:
                print(userTool)
                userAlive.goTodo('victimus.py -v ' + victoruses)
            else:                
                userAlive.goTodo('download.py --tool ' + '"Victimus 888"')
                print('W procesie scanowania wykryto aktywność hackera ' + str(victoruses) + "\n Victimus 888 shout be downloading.. Wait")
                choice = input("[ ENTER ] Kontynuj po zainstalowaniu narzędzia Victimus 888\n>>>")
                


        userAlive.exitSys()

    else:        
        userAlive.sysColorconsole('0', '6', 'Air SCANNER 9000B')
        userAlive.checking_bar('Wyszukiwanie aktywności radiowej', 10, 0.001)
        userAlive.checking_bar('Wyszukiwanie aktywności w sieciach WiFi', 10, 0.001)
        userAlive.checking_bar('Przeszukiwanie sieci lokalnych', 10, 0.001)
        userAlive.checking_bar('Wyszukiwanie aktywności GPS', 10, 0.001)
        userAlive.checking_bar('Wyszukiwanie aktywności Satelitarnej', 10, 0.001)        
        userAlive.sysColorconsole('0', '6', 'Air SCANNER 9000B')
        userAlive.checking_bar('Wyszukiwanie aktywności radiowej', 10, 0.001)
        userAlive.checking_bar('Wyszukiwanie aktywności w sieciach WiFi', 10, 0.001)
        userAlive.checking_bar('Przeszukiwanie sieci lokalnych', 10, 0.001)
        userAlive.checking_bar('Wyszukiwanie aktywności GPS', 10, 0.001)
        userAlive.checking_bar('Wyszukiwanie aktywności Satelitarnej', 10, 0.001)        
        userAlive.sysColorconsole('0', '6', 'Air SCANNER 9000B')
        userAlive.checking_bar('Wyszukiwanie aktywności radiowej', 10, 0.001)
        userAlive.checking_bar('Wyszukiwanie aktywności w sieciach WiFi', 10, 0.001)
        userAlive.checking_bar('Przeszukiwanie sieci lokalnych', 10, 0.001)
        userAlive.checking_bar('Wyszukiwanie aktywności GPS', 10, 0.001)
        userAlive.checking_bar('Wyszukiwanie aktywności Satelitarnej', 10, 0.001)        
        userAlive.sysColorconsole('0', '6', 'Air SCANNER 9000B')
        userAlive.checking_bar('Wyszukiwanie aktywności radiowej', 10, 0.001)
        userAlive.checking_bar('Wyszukiwanie aktywności w sieciach WiFi', 10, 0.001)
        userAlive.checking_bar('Przeszukiwanie sieci lokalnych', 10, 0.001)
        userAlive.checking_bar('Wyszukiwanie aktywności GPS', 10, 0.001)
        userAlive.checking_bar('Wyszukiwanie aktywności Satelitarnej', 10, 0.001)

print('Nie wykryto żadnej aktywności hackerskiej')
choice = input("Czy chcesz scanować jeszcze raz? [TAK / NIE] \n>>>")
if choice == 'Tak' or choice == 'tak'or choice == 't' or choice == 'y' or choice == 'yes':
    userAlive.goTodo('airscanner9000b.py')
userAlive.exitSys()




