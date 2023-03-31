import cv2
import userAlive
import random

txt_user = userAlive.giveUser()
session = userAlive.giveSS()

userAlive.clearConsole()
userAlive.banner(session, "Uruchomiona instancja")
userAlive.sysColorconsole("0", "2", "Uruchomiona instancja")

def videoEffect(mark, filter):
    RES = 600 , 300
    main_capture = cv2.VideoCapture(mark)
    background_capture = cv2.VideoCapture(filter)
    subtractor = cv2.createBackgroundSubtractorKNN()

    while True:
        try:
            frame = main_capture.read()[1]
            frame = cv2.resize(frame, RES, interpolation = cv2.INTER_AREA)

            bg_frame = background_capture.read()[1]
            bg_frame = cv2.resize(bg_frame, RES, interpolation = cv2.INTER_AREA)

            mask = subtractor.apply(frame, 1)
            bitwise = cv2.bitwise_and(bg_frame, bg_frame, mask=mask)

            cv2.imshow('', bitwise)

            if cv2.waitKey(1) == 27:
                # pass
                break
        except:
            break

dom = [userAlive.dataUserProfil(txt_user, 'lokalizacja_dom_y'), userAlive.dataUserProfil(txt_user, 'lokalizacja_dom_x')]
aktualna_lok = [userAlive.dataUserProfil(txt_user, 'aktualna_lokalizacja_y'), userAlive.dataUserProfil(txt_user, 'aktualna_lokalizacja_x')]

if dom == aktualna_lok:
    userAlive.checking_bar("[ Musisz wyjść z domu, żeby scanować pojazdy! \n Zamykanie CarScaner ]", 100, 0.05)
    userAlive.exitSys()


mercedeses = ['CLA', 'SLK', 'Klasa C', 'GLA', 'Vaneo', 'GL', 'Sprinter', 'ML']
fords = ['Capri', 'Galaxy', 'Kuga', 'Mustang', 'Mondeo', 'Focus C-Max', 'Fiesta', 'Ka']
bmws = ['X3', '5GT', 'M5', '3GT', 'i3', 'X4', 'M3', 'Z4']
carColor = ['niebieski', 'biały', 'czarny', 'bordowy', 'czerwony', 'żółty', 'czarny', 'srebrny']

userAlive.checking_bar("[ Ładowanie instancji narzędzia CarSnacnner v1 ]", 100, 0.01)
userAlive.checking_bar("[ Wyszukiwanie pojadów w Twojej okolicy ]", 100, 0.03)
scanResults = userAlive.scanningTerra(
                "bankomat", 50, 
                userAlive.dataUserProfil(txt_user, 'aktualna_lokalizacja_y'), 
                userAlive.dataUserProfil(txt_user, 'aktualna_lokalizacja_x')
                                        )
                                        
maxlos = len(scanResults)
losmerc = userAlive.mixer(0, maxlos)
losFord = userAlive.mixer(0, maxlos)
losBmw = userAlive.mixer(0, maxlos)
los = losmerc + losFord + losBmw
bmwMercFords = "W okolicy znaleziono pozadów: " + str(int(len(scanResults) + int(los)))

print(bmwMercFords)
userAlive.czytajTo("Witaj w CarSnacnner v1\n", 0.07)
userAlive.czytajTo("[ 1 ] - Mercedes ("+ str(losmerc)+")\n", 0.07)
userAlive.czytajTo("[ 2 ] - Ford ("+ str(losFord)+")\n", 0.07)
userAlive.czytajTo("[ 3 ] - BMW ("+ str(losBmw)+")\n", 0.07)
userAlive.czytajTo("Wybierz markę pojazdu\n", 0.07)
userChoice = input(">>> ")

if userChoice == "1" and losmerc > 0:
    userAlive.clearConsole()
    userAlive.banner(session, "Uruchomiona instancja")
    print('Wybierz target')
    for i in range(losmerc):
        selecting = i + 1        
        print("[" + str(selecting) + "] - " + str(carColor[random.randrange(0, 8)]) + " " + str(mercedeses[random.randrange(0, 8)]), ' w odelgłości (' + str(random.randrange(0, 50)) + ' m)')
        i += 1
    x = int(input(' >>> '))
    
    if x > 0 and x <= losmerc:
        userAlive.goTodo('carscannerbars.py')
        videoEffect('video/benc37.mp4', 'video/matrix37.mp4')
    
elif userChoice == "2" and losFord > 0:
    userAlive.clearConsole()
    userAlive.banner(session, "Uruchomiona instancja")
    print('Wybierz target')
    for i in range(losFord):
        selecting = i + 1        
        print("[" + str(selecting) + "] - " + str(carColor[random.randrange(0, 8)]) + " " + str(fords[random.randrange(0, 8)]), ' w odelgłości (' + str(random.randrange(0, 50)) + ' m)')
        i += 1
    x = int(input(' >>> '))
    
    if x > 0 and x <= losFord:
        userAlive.goTodo('carscannerbars.py')
        videoEffect('video/mustang43.mp4', 'video/matrix43.mp4')

elif userChoice == "3" and losBmw > 0:
    userAlive.clearConsole()
    userAlive.banner(session, "Uruchomiona instancja")
    print('Wybierz target')
    for i in range(losBmw):
        selecting = i + 1        
        print("[" + str(selecting) + "] - " + str(carColor[random.randrange(0, 8)]) + " " + str(bmws[random.randrange(0, 8)]), ' w odelgłości (' + str(random.randrange(0, 50)) + ' m)')
        i += 1
    x = int(input(' >>> '))
    
    if x > 0 and x <= losBmw:
        userAlive.goTodo('carscannerbars.py')
        videoEffect('video/mustang43.mp4', 'video/matrix43.mp4')
   
else:
    userAlive.czytajTo("Goodbye Error!")
    userAlive.exitSys()

userAlive.exitSys()
