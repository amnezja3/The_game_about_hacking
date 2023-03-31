import os
import userAlive

txt_usr = userAlive.giveUser()

userAlive.clearConsole()
userAlive.sysColorconsole("0", "E", "Hacker Console Dos")
userAlive.banner('Zalogowano w systemie Hacker Dos', txt_usr)
userAlive.checking_bar("Generowanie wiersza poleceń Hacker Dos", 100, 0.001)
os.system('start prompt $T $B HC '+txt_usr +' HackClonsole#: ')
userAlive.mowTo('Enjoy, and the best hacking for you' + txt_usr)



