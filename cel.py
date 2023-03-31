import userAlive
import time
from time import sleep
import random

giveNickName = userAlive.giveUser()

userAlive.clearConsole()
userAlive.banner("Rozpoczete procesy zewnętrzne", "Autoryzacja: " + giveNickName)

userAlive.clearConsole()
userAlive.banner("Raport ze skanowania pozjazdu", "Autoryzacja: " + giveNickName)
userAlive.checking_bar("Generowanie Raportu", 20, 0.05)
userAlive.clearConsole()
userAlive.banner("Raport ze skanowania pozjazdu", "Autoryzacja: " + giveNickName)                                                        
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

userAlive.clearConsole()
userAlive.banner("Raport ze skanowania pozjazdu", "Autoryzacja: " + giveNickName)                                                                                                                                                          
userAlive.clearConsole()
userAlive.banner("Oznaczanie pozjazdu ofiary", "Autoryzacja: " + giveNickName)
oznacz_cel_nazwa = input("Wprowadź nazwe oznaczonego celu: ")
oznacz_cel_opis = input("Wprowadź opis dla celu o nazwie [" + oznacz_cel_nazwa + "]: ")  
userAlive.checking_bar("Oznaczanie pozjazdu ofiary" + "\n" + "Nazwa: [" + oznacz_cel_nazwa + "]" + "\n" + "Opis: [" + oznacz_cel_opis + "]", 100, 0.05)
sleep(0.1)