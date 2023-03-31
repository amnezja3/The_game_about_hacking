import userAlive
import argparse
import time

#####################################        ARGUMETOWANIE SKRYPTU     #####################################
parser = argparse.ArgumentParser(description="Hacker GRA cRPG v1")
parser.add_argument("-t", "--tool", type=str, help="Wpowadź nazwe narzędzia w lini polecen, jeżeli są spacje użej cudzyslowów")
args = parser.parse_args()
tool = args.tool
##################################### ARGUMETOWANIE SKRYPTU ZAKONCZONE #####################################

txt_user = userAlive.giveUser()
session = userAlive.giveSS()

userTool = userAlive.verifityTools('dostepne_tools', txt_user, 'kolumna1', tool, 'kolumna4')
kol2 = userAlive.dataUserSELECT('tools', '', "tool_name", tool, 'tool_descr') 
kolumna2 = kol2[0]
kol3 = userAlive.dataUserSELECT('tools', '', "tool_name", tool, 'tool_category')
kolumna3 = kol3[0]
kol4 = userAlive.dataUserSELECT('tools', '', "tool_name", tool, 'tool_command')
kolumna4 = kol4[0]

userid = userAlive.dataUserSELECT('users_main', '', 'user', txt_user, 'identyfikator')
useridforchanged = userid[0]
PunktyDoswiadczenia = userAlive.dataUserSELECT('users_main', '', 'user', txt_user, 'punkty_doswiadczenia')
pointsadd = int(PunktyDoswiadczenia[0])



if userTool != None:
    print('Masz już zainstalowane narzędzie ' + tool)
    time.sleep(3)
    userAlive.exitSys()
else:
    userAlive.banner(session, "Uruchomiona instancja")
    userAlive.sysColorconsole("0", "B", "Uruchomiona instancja")
    userAlive.checking_bar("Downloading.. [ "+tool+" ]", userAlive.mixer(5000, 15000), 0.07)

    userAlive.literujTo("Narzędzie[ "+tool+" ] zostało pobrane prawidłowo.\nCzy chcesz zainstalować to narzedzie?", 0.002)
    userAlive.mowTo(tool + " is downloaded. Do you want install" + tool)
    install = input("Yes or No\n >>> ")    
    if install == "yes" or install == "Yes" or install == "YES":
        userAlive.mowTo("Sure .."+ tool + " is instaling now!")
        userAlive.checking_bar("Installing .. [ "+tool+" ]", userAlive.mixer(500, 2500), 0.03)
        userAlive.dataUserINSERT6('dostepne_tools', txt_user, tool, kolumna2, kolumna3, kolumna4, '', '')
        points = pointsadd + 10
        userAlive.dataUserUPDATE("users_main", '', 'punkty_doswiadczenia', points, useridforchanged)
        print("Narzędzie[ "+tool+" ] zostało prawidłowo zainstalowane.")
        time.sleep(10)

    elif install == "apt install * && apt upgrade *" or install == "apt install *" or install == "apt upgrade *":
        userAlive.mowTo("Yes master.."+tool + " is instaling now!")
        userAlive.checking_bar("Installing .. [ "+tool+" ]", userAlive.mixer(100, 300), 0.01)
        userAlive.dataUserINSERT6('dostepne_tools', txt_user, tool, kolumna2, kolumna3, kolumna4, '', '')
        points = pointsadd + 50
        userAlive.dataUserUPDATE("users_main", '', 'punkty_doswiadczenia', points, useridforchanged)
        print("Narzędzie[ "+tool+" ] zostało prawidłowo zainstalowane.")
        time.sleep(10)

    else:
        print("404 Connection off")
        time.sleep(3)

