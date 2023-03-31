import os
import userAlive

txt_usr = userAlive.giveUser()

userAlive.clearConsole()
userAlive.sysColorconsole("0", "E", "Hacker Console Dos")
userAlive.checking_bar("Generowanie wiersza poleceń Hacker Dos", 100, 0.003)
userAlive.clearConsole()
userAlive.czytajTo('\nStreet HackEr TriCks\n----------------------\nHej, ' + txt_usr +" tutaj zaprezentuję Ci kilka sztuczek hakerskich. \nNa poczatek coś łatwego. Musze wiedzieć jaką opcję wybierzesz. \n\nOdpowiedz, czy wolisz wersję głosową, czy tekstową?", 0.07)
userAlive.mowTo('hey, ' + txt_usr + ' I will present you some hacking tricks. Something easy to start with. I need to know whitch version do you like? Reply, do you prefer the voice or text version? \n')


version = str(input('\n\nWpisz [ TEXT / VOICE ] \n>> '))
userAlive.clearConsole()
if version == "text" or version == "TEXT" or version == "t" or version == "tekst" or version == "Text" or version == "v" or version == "voice" or version == "VOICE":

    
    if version == "text" or version == "TEXT" or version == "t" or version == "tekst" or version == "Text":
        userAlive.clearConsole()
        userAlive.czytajTo("TRICK #1\n----------------------\ncmd, hack line, terminal\n----------------------\nW głównym terminalu Street Hacker wywołaj \nkomendę cmd. Uzyskasz dostep do swojej konsoli \nhackerskiej. Tam pokażę Ci kilka sztuczek. Konsole \nmożesz wywołać również wpisując takie \nkomendy jak: console, hack line, command, \nkonsola, linia lub poprostu terminal. ", 0.07)
        a = input("\n\nWciśnij enter żeby przejść do nastepnego tricku\n[ ENTER ] -nastepny trick \n[ Ctrl + C ] - przerwij prezentację \n >>> ")        
    if version == "v" or version == "voice" or version == "VOICE":
        userAlive.clearConsole()
        print('"TRICK #1\n----------------------\ncmd, hack line, terminal \n----------------------\n')
        userAlive.mowTo("TRICK 1. We begin. In the main Street Hacker terminal, run the cmd command. You will gain access to your hacker console. There, I'll show you some tricks. You can also invoke Konsole by entering commands such as: console, hack line, command, console, line or just a terminal.")
        a = input("\n\nHit enter to go to the next trick \n [ENTER] -next trick \n [ Ctrl + C ] - stop the presentation \n >>> ")
        
    
    if version == "text" or version == "TEXT" or version == "t" or version == "tekst" or version == "Text":
        userAlive.clearConsole()      
        userAlive.czytajTo("TRICK #2\n----------------------\ncolor 0E, color help\n----------------------\nOtworzyłeś konsolę, w takim razie wszystko \nposzło pomyślnie. Gratulacje! Przejdz teraz \ndo swojej konsoli i wydaj komendę color 0E \nw wiersu poleceń. Obserwuj co się stanie. \nMożesz wybrać swój ulubiony kolor, pierwsza \ncyfra to kolor tła terminala, druga zaś \nto kolor tekstu. Możesz się dowiedzieć \nwięcej o koloroach wpisując color help.", 0.07)
        a = input("\n\nWciśnij enter żeby przejść do nastepnego tricku\n[ ENTER ] -nastepny trick \n[ Ctrl + C ] - przerwij prezentację \n >>> ")
        userAlive.clearConsole()
    if version == "v" or version == "voice" or version == "VOICE":
        userAlive.clearConsole()
        print('"TRICK #2\n----------------------\ncolor 0E, color help \n----------------------\n')
        userAlive.mowTo("TRICK 2. You opened the consoles, it all went well. Congrats! Now go to your hacker console. Issue the command color 0E in the command line of your hacker console. See what happens. You can choose your own color, the first number is the background color of the terminal and the second number is the color of the text. You can learn more about color by typing color help.")
        a = input("\n\nHit enter to go to the next trick \n [ENTER] -next trick \n [ Ctrl + C ] - stop the presentation \n >>> ")
    

    if version == "text" or version == "TEXT" or version == "t" or version == "tekst" or version == "Text":
        userAlive.clearConsole()      
        userAlive.czytajTo("TRICK #3\n----------------------\ncipher \n----------------------\nKolejną komendą w swojej konsoli hackerskiej \nzakodujesz swoje usuniete dane z kosza Windows,\npozostaną one w pełni poufne i zakodowane. \nW wiersu poleceń wydaj komendę cipher. \nSystem zabezpieczy Twoje usunięte pliki. \nMożesz się dowiedzieć więcej o tej komendzie \nwpisując cipher /?.", 0.07)
        a = input("\n\nWciśnij enter żeby przejść do nastepnego tricku\n[ ENTER ] -nastepny trick \n[ Ctrl + C ] - przerwij prezentację \n >>> ")
        userAlive.clearConsole()
    if version == "v" or version == "voice" or version == "VOICE":
        userAlive.clearConsole()
        print('"TRICK #3\n----------------------\ncipher \n----------------------\n')
        userAlive.mowTo("TRICK 3. With the next command in your hacker console, you will encode your deleted data from the Windows recycle bin, it will remain fully confidential and encrypted. At the command prompt, issue cipher. The system will protect your deleted files. You can learn more about this command by typing cipher /?.")
        a = input("\n\nHit enter to go to the next trick \n [ENTER] -next trick \n [ Ctrl + C ] - stop the presentation \n >>> ")
    

    if version == "text" or version == "TEXT" or version == "t" or version == "tekst" or version == "Text":
        userAlive.clearConsole()      
        userAlive.czytajTo("TRICK #4\n----------------------\ncls \n----------------------\nNastepna komenda którą wywołamy konsoli hackerskiej \nwyczyśi okno terminalu. W wiersu poleceń wydaj \nkomendę cls a wyczyścisz swoja konsole hackerską.", 0.07)
        a = input("\n\nWciśnij enter żeby przejść do nastepnego tricku\n[ ENTER ] -nastepny trick \n[ Ctrl + C ] - przerwij prezentację \n >>> ")
        userAlive.clearConsole()
    if version == "v" or version == "voice" or version == "VOICE":
        userAlive.clearConsole()
        print('"TRICK #4\n----------------------\ncls \n----------------------\n')
        userAlive.mowTo("TRICK 4. The next command we will call the hacker console will clear the terminal window. In the command line, type cls and you will clean your hacker console.")
        a = input("\n\nHit enter to go to the next trick \n [ENTER] -next trick \n [ Ctrl + C ] - stop the presentation \n >>> ")
    

    if version == "text" or version == "TEXT" or version == "t" or version == "tekst" or version == "Text":
        userAlive.clearConsole()      
        userAlive.czytajTo("TRICK #5\n----------------------\nsfc /scannow, sfc /? \n----------------------\nNastepna polecenie konsoli hackerskiej \nprzeskanuje Twoje pliki i naprawi je. \nW wiersu poleceń wydaj polecenie sfc /scannow \na system rozpocznie scan. Sprawdź wiecej opcji \ntego polecania wpisując w konsoli sfc /?.", 0.07)
        a = input("\n\nWciśnij enter żeby przejść do nastepnego tricku\n[ ENTER ] -nastepny trick \n[ Ctrl + C ] - przerwij prezentację \n >>> ")
        userAlive.clearConsole()
    if version == "v" or version == "voice" or version == "VOICE":
        userAlive.clearConsole()
        print('"TRICK #5\n----------------------\nsfc /scannow, sfc /? \n----------------------\n')
        userAlive.mowTo("TRICK 5. TThe hacker console's next command will scan your files and repair them. At the command prompt, run sfc / scannow and the system will start to scan. Check out more options for this command by typing sfc /?. ")
        a = input("\n\nHit enter to go to the next trick \n [ENTER] -next trick \n [ Ctrl + C ] - stop the presentation \n >>> ")


    if version == "text" or version == "TEXT" or version == "t" or version == "tekst" or version == "Text":
        userAlive.clearConsole()      
        userAlive.czytajTo("TRICK #6\n----------------------\ndriverquery, driverquery -v \n----------------------\nNastepną komendą uzyskasz informacje \nzainstalowanych sterownikach dla urządeń \nna Twojej maszynie. W wiersu poleceń \nwydaj polecenie driverquery a system pokaże \nCi zainstalowane starowniki. Sprawdź wiecej \ninformacji o sterownikach wpisując w konsoli \ndriverquery -v.", 0.07)
        a = input("\n\nWciśnij enter żeby przejść do nastepnego tricku\n[ ENTER ] -nastepny trick \n[ Ctrl + C ] - przerwij prezentację \n >>> ")
        userAlive.clearConsole()
    if version == "v" or version == "voice" or version == "VOICE":
        userAlive.clearConsole()
        print('"TRICK #6\n----------------------\ndriverquery, driverquery -v \n----------------------\n')
        userAlive.mowTo("TRICK 6. With the next command you will get information about the installed drivers for devices on your machine. At the command prompt, run the driverquery command and the system will show you the installed drivers. Check more about drivers by typing driverquery -v in the console. ")
        a = input("\n\nHit enter to go to the next trick \n [ENTER] -next trick \n [ Ctrl + C ] - stop the presentation \n >>> ")

    
    if version == "text" or version == "TEXT" or version == "t" or version == "tekst" or version == "Text":
        userAlive.clearConsole()      
        userAlive.czytajTo("TRICK #7\n----------------------\ntitle \n----------------------\nUstaw nagłówek swojego okna consoli. \nWykonaj komendę title<SPACE>twój tytuł \na tytuł twojego okna ustawi się.", 0.07)
        a = input("\n\nWciśnij enter żeby przejść do nastepnego tricku\n[ ENTER ] -nastepny trick \n[ Ctrl + C ] - przerwij prezentację \n >>> ")
        userAlive.clearConsole()
    if version == "v" or version == "voice" or version == "VOICE":
        userAlive.clearConsole()
        print('"TRICK #7\n----------------------\ntitle \n----------------------\n')
        userAlive.mowTo("TRICK 7. Set the header of your console window. Execute the command title <SPACE> your title, and your window title will be set. ")
        a = input("\n\nHit enter to go to the next trick \n [ENTER] -next trick \n [ Ctrl + C ] - stop the presentation \n >>> ")

    if version == "text" or version == "TEXT" or version == "t" or version == "tekst" or version == "Text":
        userAlive.clearConsole()      
        userAlive.czytajTo("TRICK #8\n----------------------\nipconfig, ipconfig /all\nipconfig /flushdns, ipconfig /relese\nipconfig /renew, ipconfig --help\n----------------------\nJedna z najbardziej podstawowych funkcji konsoli \nhackerskiej. Za pomocą ipconfig możesz uzyskać \ninformacje o własnym połączeniu sieciowym ale \nrównież pomyślnie opróżniono pamięć podręczną \nDNS Resolver lub ustawić nowe IP jeżeli używasz DHCP.\nPobaw się tą funcją pisując w konsoli ipconfig,\nipconfig /flushdns, ipconfig /relese\nipconfig /renew oraz ipconfig /all. Wiecej \no ipconfig dowiesz się z wykonując komendę \nipconfig --help.", 0.07)
        a = input("\n\nWciśnij enter żeby przejść do nastepnego tricku\n[ ENTER ] -nastepny trick \n[ Ctrl + C ] - przerwij prezentację \n >>> ")
        userAlive.clearConsole()
    if version == "v" or version == "voice" or version == "VOICE":
        userAlive.clearConsole()
        print('"TRICK #8\n----------------------\nipconfig, ipconfig /all\nipconfig /flushdns, ipconfig /relese\nipconfig /renew, ipconfig --help \n----------------------\n')
        userAlive.mowTo("TRICK 8. One of the most basic features of a hacker console. With ipconfig you can get information about your own network connection but also successfully flushed the DNS Resolver cache or set a new IP if you are using DHCP. Play around with this feature by typing ipconfig, ipconfig / flushdns, ipconfig / relese ipconfig / renew and ipconfig / all in the console. To learn more about ipconfig, see ipconfig --help. ")
        a = input("\n\nHit enter to go to the next trick \n [ENTER] -next trick \n [ Ctrl + C ] - stop the presentation \n >>> ")
    

    if version == "text" or version == "TEXT" or version == "t" or version == "tekst" or version == "Text":
        userAlive.clearConsole()      
        userAlive.czytajTo("TRICK #9\n----------------------\nping <addres>, ping <addres> -t \nping --help\n----------------------\nTeraz zaprazentuje Ci polecenie ping. To polecenie \npozwoli Ci zebrać informacje o adresach IP innych komputerów. \nUżyj komendy ping google.com a uzyskasz informacje \no płączeniu z google oraz adress IP google.com. Wykonując \npolecenie ping google.com -t, zapytanie będzie \ntwało aż je przerwiesz. Sprawdź również \nping --help a dowiesz się więcej.", 0.07)
        a = input("\n\nWciśnij enter żeby przejść do nastepnego tricku\n[ ENTER ] -nastepny trick \n[ Ctrl + C ] - przerwij prezentację \n >>> ")
        userAlive.clearConsole()
    if version == "v" or version == "voice" or version == "VOICE":
        userAlive.clearConsole()
        print('"TRICK #9\n----------------------\nping <addres>, ping <addres> -t \nping --help \n----------------------\n')
        userAlive.mowTo("TRICK 8. Now I will present the ping command to you. This command will allow you to collect information about the IP addresses of other computers. Use the ping google.com command and you will get information about connecting to google and google.com IP address. By doing ping google.com -t, your query will continue until you complete it. Also check ping --help for more information on this command.")
        a = input("\n\nHit enter to go to the next trick \n [ENTER] -next trick \n [ Ctrl + C ] - stop the presentation \n >>> ")

    
    if version == "text" or version == "TEXT" or version == "t" or version == "tekst" or version == "Text":
        userAlive.clearConsole()      
        userAlive.czytajTo("TRICK #10\n----------------------\npathping <ip or domain>\n----------------------\nWiesz już jak uzyskać adres IP dowolnej domeny. \nTeraz zaprezentuję Ci jak śledzieć ruch między Twoją \nmaszyną a serwerami w internecie. Wykonaj komendę \npathping google.com a zobaczysz którędy wędrują \npakiety danych. Sprawdź również pathping --help \na dowiesz się wiecej.", 0.07)
        a = input("\n\nWciśnij enter żeby przejść do nastepnego tricku\n[ ENTER ] -nastepny trick \n[ Ctrl + C ] - przerwij prezentację \n >>> ")
        userAlive.clearConsole()
    if version == "v" or version == "voice" or version == "VOICE":
        userAlive.clearConsole()
        print('"TRICK #10\n----------------------\npathping <ip or domain> \npathping --help \n----------------------\n')
        userAlive.mowTo("TRICK 10. You already know how to get an IP address for any domain. Now I will show you how to track the traffic between your machine and servers on the Internet. Run pathping google.com and you will see where the data packets travel. Also check pathping --help for more information.")
        a = input("\n\nHit enter to go to the next trick \n [ENTER] -next trick \n [ Ctrl + C ] - stop the presentation \n >>> ")

    
    if version == "text" or version == "TEXT" or version == "t" or version == "tekst" or version == "Text":
        userAlive.clearConsole()      
        userAlive.czytajTo("TRICK #11\n----------------------\nshutdown / h, shutdown / r / o \nshutdown --help \n----------------------\nKolejny trick w twojej konsoli hackerskiej, \npozwala zahibernować, zrestartować a nawet wyłączyć \nTwoją maszynę. Wykonaj polecenie shutdown /h \na zahibernujesz swoją maszynę w secundę. \nWykonując shutdown /r /o zrestatujesz sprzęt. Sprawdź \nrównież polecenie shutdown /? a uzyskasz informacje \no większej ilości opcji tego polecenia.", 0.07)
        a = input("\n\nWciśnij enter żeby przejść do nastepnego tricku\n[ ENTER ] -nastepny trick \n[ Ctrl + C ] - przerwij prezentację \n >>> ")
        userAlive.clearConsole()
    if version == "v" or version == "voice" or version == "VOICE":
        userAlive.clearConsole()
        print('"TRICK #11\n----------------------\nshutdown / h, shutdown / r / o \nshutdown --help \n----------------------\n')
        userAlive.mowTo("TRICK 11. Another trick in your hacker console allows you to hibernate, restart and even shut down your machine. Run shutdown / h and your machine will hibernate in a second. Doing shutdown / r / o will restart your hardware. Also check the shutdown /? and you will get information about more options for this command.")
        a = input("\n\nHit enter to go to the next trick \n [ENTER] -next trick \n [ Ctrl + C ] - stop the presentation \n >>> ")


userAlive.czytajTo("NEXT TRICKS ON HIGHER LEVEL \n----------------------\nLEVEL BASIC COMPLETE \n----------------------\nKolejny tricki ukażą się dla Ciebie gdy \nzbudujesz doświadczenie i poziom w Street Hacker, \nwykorzystując zdobyte umiejetności hackerskie. \nWitam w Street Hacker i życzę udanej zabawy. \n\nAI project 2021 OPEN SOURCE for every anong world.\n\n\nDziękuję za uwagę. Do usłyszenia.", 0.07)
userAlive.mowTo('The next tricks will appear for you when you build experience and level in Street Hacker, using the acquired hacking skills. Welcome to Street Hacker and have fun. AI project 2021 OPEN SOURCE for every one. Thank you for your attention. Speak soon.')
a = input("\n\nHit enter to go to the next trick \n [ENTER] - exit \n [ Ctrl + C ] - stop the presentation \n >>> ")

userAlive.exitSys()

