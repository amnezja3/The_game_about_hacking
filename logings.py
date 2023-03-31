import userAlive
import string

bazaUser = 'dostepne_tools'
wprowadzNick = 'admin' # pppopo
giveNickName = wprowadzNick
txt_user = wprowadzNick
giveuser = wprowadzNick
tool = """IP scanner"""
target = 'a'
givePass = '1234'


test = 1.1
print(type(test))

vcoins = userAlive.dataUserProfil(giveuser, 'aktualne_vcoin')
vcoinsSTR = float(vcoins)
vcoinsINT = int(vcoinsSTR)

print(vcoinsINT)



# list_oznaczone_tytul = userAlive.dataGeneral('fav_places' + str(txt_user), "kolumna1") 
# if list_oznaczone_tytul[0] == 'None':
#     print('to jej str None')
# else:
#     print('To nie jest str None')

# print(type(list_oznaczone_tytul))
# print(list_oznaczone_tytul[0])





# userid = userAlive.dataUserSELECT('users_main', '', 'user', str(txt_user), 'identyfikator')
# useridforchanged = userid[0]

# print(userid[0])
# print(userid)
# print(type(userid))



# dane = sca1[i]
# y = userAlive.dotLocation(str(dane[a]))
# x = userAlive.dotLocation(str(dane[a+1]))
# userAlive.dataUserINSERT6('terra_scan', txt_user, str(dane[a+2]), y, x, 'bankomat', '', 'del')


# otherPlayers = userAlive.detectOterHacker(txt_user)
# dataPasswords = userAlive.dataGeneral('users_main', "aktualna_lokalizacja_y")
# standardOne = dataPasswords[0]
# # std_pass = dataPasswords[1]
# standardOne = float(standardOne)
# print(otherPlayers)
# print(type(otherPlayers))

# userAlive.dataSuperUPDATE('selected_targets', str(txt_user), 'kolumna3', 'hacked', 'kolumna1' ,str(target))


# def autoOfensive(target):
#     listaLiczb = []
#     for i in range(25):
#         l = len(listaLiczb)
#         if l == 5:
#             break
#         los = userAlive.mixer(1,17)
#         if los in listaLiczb:
#             continue
#         else:
#             listaLiczb.append(los)
#     slowniczek = {}
#     listaPol = ['vpn', 'a1', 'a2', 'a3', 'a4', 'b1', 'b2', 'b3', 'b4', 'c1', 'c2', 'c3', 'c4', 'd1', 'd2', 'd3', 'd4']
#     for i in listaLiczb:
#         onOff = userAlive.mixer(0,2)
#         if onOff == 0:
#             wynik = 'OFF'
#         else:
#             wynik = 'ON'
#         x = int(i) 
#         slowniczek[listaPol[x]] = wynik
#     pobranySlownik = userAlive.usersFirewall(target)
#     pobranySlownikWynik = {}
#     x = 0
#     for i in listaPol:
#         if slowniczek.get(i) != None and pobranySlownik is not None:
#             pobranySlownikWynik[i] = pobranySlownik[x]
#         x += 1
#     trafienia = 0
#     oznaczenia = {}
#     for key1 in pobranySlownikWynik.items():    
#         for key2 in slowniczek.items():        
#             if key1 == key2:
#                 oznaczenia[key1[0]] = "SHOT"            
#                 trafienia += 1
#     # # buduje slownik załościowy
#     caloscSL = {}
#     zx = 0
#     for i in listaPol:
#         if pobranySlownik is not None:
#             caloscSL[i] = pobranySlownik[zx]
#             zx += 1

#     # # aktualizuje wyniki
#     for w in oznaczenia.keys():    
#         caloscSL[w] = 'SHOT'

#     # # generuje liste SHOT
#     listShot = []
#     for po in caloscSL.values():
#         listShot.append(po)
    
#     if listShot == []:
#         return None
#     else:
#         listShot.append(trafienia)
#         return listShot

# print(autoOfensive(target))

# lista = []

# try:
#     lista[0]
# except:
#     lista.append(None)


# if lista[0] == None:
#     lista.pop(0)
#     print('pusta')
#     l = input('dodaj: ')
#     x = l
#     lista.append(x)
    
# else:
#     print('not none')



# victimuses = userAlive.detectOterHacker(giveNickName)
# print(victimuses.keys())

# if target in victimuses.keys():
#     print('jest nick')
# else:
#     print('niema nicku')
# poka = userAlive.usersFirewall(giveNickName)
# if poka != None:
#     vpnTurn = poka[0]
#     try:
#         a1 = poka[1]
#         a2 = poka[2]
#         a3 = poka[3]
#         a4 = poka[4]

#         b1 = poka[5]
#         b2 = poka[6]
#         b3 = poka[7]
#         b4 = poka[8]

#         c1 = poka[9]
#         c2 = poka[10]
#         c3 = poka[11]
#         c4 = poka[12]

#         d1 = poka[13]
#         d2 = poka[14]
#         d3 = poka[15]
#         d4 = poka[16]

#         print(poka)
#     except:
#         if vpnTurn == "":
#             print('None security')


    


# zbr = userAlive.dataUserProfil(giveNickName, 'aktualna_zbroja')
# myDict = zbr
# myDict = str(myDict)
# s3 = myDict.strip("]")
# s4 = s3.strip("[")
# s5 = s4.split(", ")

# li = []

# for i in s5:    
#     iw = i
#     ix = iw.lstrip("""'""")
#     iy = ix.rstrip("""'""")
#     iz = iy.rstrip("""',""")
#     z = iz.strip()
#     li.append(z)



    

# print(li)
# print(type(li))


# ip = '255.7.123.123'
# def checkIpNumber(ip):
#     ipStrp = ip.split(".")
#     modulIp = []
#     for i in ipStrp:
#         try:
#             i = int(i)
#             if i < 256 and i > -1:
#                 modulIp.append(True)
#             else:
#                 modulIp.append(False)
#         except:
#             modulIp.append(None)
#     return modulIp

# print(checkIpNumber(ip))




# userTool2 = userAlive.dataUserSELECT('dostepne_tools', wprowadzNick, 'kolumna1', tool, 'kolumna4')

# listCol = userAlive.dataGeneral(bazaUser + wprowadzNick, 'kolumna1')
# listShow = userAlive.dataGeneral(bazaUser + wprowadzNick, 'kolumna4')

# userTool = userAlive.verifityTools('dostepne_tools', giveNickName, 'kolumna1', tool, 'kolumna4')
# print()
# print(giveNickName)
# print()
# print(userTool2)
# print()
# print(listCol[18])
# print()
# print(listShow)




# detector = userAlive.detectOterHacker(wprowadzNick)

# print(detector)
# checkLokY = 52
# akY = 21

# checkLokX = 49
# akX = 20

# dY = checkLokY - akY 
# dX = checkLokX - akX

# kwY = dY ** 2
# kwX = dX ** 2

# sumKw = kwY + kwX

# sqrt = sumKw ** (.5)

# print(sqrt)

# print(userAlive.dotLocation('-0.000111'))







# location = "Latitude: 68.9110\nLongitude: 124.4531"
# print(userAlive.gotLocation(location))




# pusty = set()
# pusty.add("lucyna")
# pusty.add("amanda")
# pusty.add("karolina")

# print(pusty)
# pusty.add("karolina")

# pusta = []
# for i in pusty:
#     pusta.append(i)

# print(pusta)



# scanResults = userAlive.scanningTerra(
#                 "hotel", 250, 
#                 userAlive.dataUserProfil(txt_user, 'aktualna_lokalizacja_y' ), 
#                 userAlive.dataUserProfil(txt_user, 'aktualna_lokalizacja_x' )
#                                         )
# print(scanResults)
# a = 0
# for i in range(len(scanResults)):
#     dane = scanResults[i]
#     print(str(dane[a+2]), " | " + str(dane[a]), str(dane[a+1]))
#     i += 1
    


# choice = 'Vegapol'

# lngLat = userAlive.dataUserSELECT('fav_places', txt_user, "kolumna1", choice, 'kolumna3')
# print((choice))
# print((lngLat))


# aktualna_lokalizacja_y = userAlive.dataUserProfil(txt_user, 'aktualna_lokalizacja_y')
# aktualna_lokalizacja_x = userAlive.dataUserProfil(txt_user, 'aktualna_lokalizacja_x') 

# lokalizacja_dom_y = userAlive.dataUserProfil(txt_user, 'lokalizacja_dom_y')
# lokalizacja_dom_x = userAlive.dataUserProfil(txt_user, 'lokalizacja_dom_x')


# def dotLocation(kropka):    
#     export = None
#     if kropka[1] == ".":
#         print("kropka jest na drugim miejscu")
#         c1 = kropka[1]
#         c2 = kropka[2:]
#         export = str(c1) + str(c2)
#     if kropka[2] == ".":
#         print("kropka jest na trzecim miejscu")
#         c1 = kropka[:2]
#         c2 = kropka[3:]
#         export = str(c1) + str(c2)
#     if kropka[3] == ".":
#         print("kropka jest na czwartym miejscu")
#         c1 = kropka[:3]
#         c2 = kropka[4:]
#         export = str(c1) + str(c2)
#     if kropka[4] == ".":
#         print("kropka jest na piątym miejscu")
#         c1 = kropka[:4]
#         c2 = kropka[5:]
#         export = str(c1) + str(c2)

#     intmcLY = int(export)
#     newlocY = intmcLY / 1000000

#     print(aktualna_lokalizacja_y, type(aktualna_lokalizacja_y))
#     print(aktualna_lokalizacja_x, type(aktualna_lokalizacja_x))
#     print(intmcLY, type(intmcLY))
#     print(newlocY, type(newlocY))
#     print(lokalizacja_dom_y, type(lokalizacja_dom_y))
#     print((lokalizacja_dom_x), type(lokalizacja_dom_x))
#     return newlocY

# results = dotLocation(aktualna_lokalizacja_y)
# print(type(results))



# saveName = 'Plaza'

# aktualna_lokalizacja_y = userAlive.dataUserProfil(txt_user, 'aktualna_lokalizacja_y')
# aktualna_lokalizacja_x = userAlive.dataUserProfil(txt_user, 'aktualna_lokalizacja_x')

# print(aktualna_lokalizacja_y, aktualna_lokalizacja_x)

# userAlive.dataUserINSERT6('fav_places', txt_user, saveName, str(aktualna_lokalizacja_y), str(aktualna_lokalizacja_x), "", "", "")
# print("Miejsce zostało zapisane")

# file = str(userAlive.checkMatrixIMG())
# loadedImg = file
# print(loadedImg)





# useridforchanged = userAlive.dataUserSELECT('users_main', '', 'user', txt_user, 'identyfikator')
# userid = int(useridforchanged[0])

# PunktyDoswiadczenia = userAlive.dataUserSELECT('users_main', '', 'user', txt_user, 'punkty_doswiadczenia')
# pointsadd = int(PunktyDoswiadczenia[0])

# points = 1000 + pointsadd
# userAlive.dataUserUPDATE("users_main", '', 'punkty_doswiadczenia', points, userid)
# print(useridforchanged)
# print(userid)
# print(pointsadd)


# ilosc = userAlive.dataGeneral('users_main', 'user')
# dlugosc = len(ilosc)
# identyfikator = dlugosc + 1
# print(ilosc)
# print(dlugosc)
# print(identyfikator)



# userid = userAlive.dataUserSELECT('users_main', '', 'user', txt_user, 'id')
# useridforchanged = int(userid[0])
# PunktyDoswiadczenia = userAlive.dataUserSELECT('users_main', '', 'user', txt_user, 'punkty_doswiadczenia')
# points = int(PunktyDoswiadczenia[0]) 
# userAlive.dataUserUPDATE("users_main", '', 'punkty_doswiadczenia', points + 50, useridforchanged)

# print(useridforchanged, points)

# atrybut = userAlive.dataGeneral('users_main', 'user')
# print(atrybut)

# userid = userAlive.dataUserSELECT('users_main', '', 'user', txt_user, 'identyfikator')
# useridforchanged = userid[0]
# PunktyDoswiadczenia = userAlive.dataUserSELECT('users_main', '', 'user', txt_user, 'punkty_doswiadczenia')
# points = int(PunktyDoswiadczenia[0])

# print(useridforchanged, points)


# id = 1

# for id in range(203):
#     may = (userAlive.mixer(200, 100001)) / 100000
#     mby = (userAlive.mixer(200, 10001)) / 100
#     userAlive.dataUserUPDATE("users_main", '', 'aktualne_vcrypto', may, id)
#     userAlive.dataUserUPDATE("users_main", '', 'aktualne_vcoin', mby, id)
#     userAlive.dataUserUPDATE("users_main", '', 'aktualne_usd', '0.25', id)
#     userAlive.dataUserUPDATE("users_main", '', 'aktualny_poziom', '1', id)

#     id += 1

# id = 2
# ay = 52295371 
# ax = 21025231
# dy = 52295171
# dx = 21025031



# for id in range(203):
#     may = ay / 1000000 
#     max = ax / 1000000
#     mdy = dy / 1000000
#     mdx = dx / 1000000

#     maty = (ay + 500) / 1000000
#     matx = (ax + 500) / 1000000
#     mbty = (ay + 500) / 1000000
#     mbtx = (ax - 500) / 1000000
#     mcty = (ay - 500) / 1000000
#     mctx = (ax + 500) / 1000000
#     mdty = (ay - 500) / 1000000
#     mdtx = (ax - 500) / 1000000


#     userAlive.dataUserUPDATE("users_main", '', 'aktualna_lokalizacja_y', may, id)
#     userAlive.dataUserUPDATE("users_main", '', 'aktualna_lokalizacja_x', max, id)
#     userAlive.dataUserUPDATE("users_main", '', 'lokalizacja_dom_y ', mdy, id)
#     userAlive.dataUserUPDATE("users_main", '', 'lokalizacja_dom_x ', mdx, id)

#     userAlive.dataUserUPDATE("users_main", '', 'lokalizacja_terenu_a_y ', maty, id)
#     userAlive.dataUserUPDATE("users_main", '', 'lokalizacja_terenu_a_x ', matx, id)

#     userAlive.dataUserUPDATE("users_main", '', 'lokalizacja_terenu_b_y ', mbty, id)
#     userAlive.dataUserUPDATE("users_main", '', 'lokalizacja_terenu_b_x ', mbtx, id)

#     userAlive.dataUserUPDATE("users_main", '', 'lokalizacja_terenu_c_y ', mcty, id)
#     userAlive.dataUserUPDATE("users_main", '', 'lokalizacja_terenu_c_x ', mctx, id)

#     userAlive.dataUserUPDATE("users_main", '', 'lokalizacja_terenu_d_y ', mdty, id)
#     userAlive.dataUserUPDATE("users_main", '', 'lokalizacja_terenu_d_x ', mdtx, id)


#     id += 1
#     ay -= 100
#     ax -= 200
#     dy -= 100
#     dx -= 200

# print(ay / 1000000)

# userTool = userAlive.verifityTools('dostepne_tools', txt_user, 'kolumna1', tool, 'kolumna4')

# kol2 = userAlive.dataUserSELECT('tools', '', "tool_name", tool, 'tool_descr')
# kolumna2 = kol2[0]
# kol3 = userAlive.dataUserSELECT('tools', '', "tool_name", tool, 'tool_category')
# kolumna3 = kol3[0]
# kol4 = userAlive.dataUserSELECT('tools', '', "tool_name", tool, 'tool_command')
# kolumna4 = kol4[0]

# print(userTool, kolumna2, kolumna3, kolumna4)

# userTool = userAlive.dataUserSELECT("dostepne_tools", wprowadzNick, 'kolumna1', "FTP Cracker", 'kolumna4')
# try:
#     verification = userTool[0]
# except:
#     verification = None
# enter = verification

# if verification != None:
#     print("isnieje")
# else:
#     print("nie isnieje")

# userAlive.dataUserCREATE6('dostepne_tools', 'admin')
# listKolumna1 = userAlive.dataGeneral('tools', 'tool_name')
# listKolumna2 = userAlive.dataGeneral('tools', 'tool_descr')
# listKolumna3 = userAlive.dataGeneral('tools', 'tool_category')
# listKolumna4 = userAlive.dataGeneral('tools', 'tool_command')

# kolumna5 = ""
# kolumna6 = ""

# for insert in range(len(listKolumna1)):
#     userAlive.dataUserINSERT6('dostepne_tools', 'admin', listKolumna1[insert], listKolumna2[insert], listKolumna3[insert], listKolumna4[insert], kolumna5, kolumna6)



# userAlive.dataUserUPDATE('oznaczone_cele', 'root', 'kolumna1', 'jankes', '7')

# userAlive.dataUserINSERT6
# userAlive.dataUserDELETE('today_news', 'admin', 'kolumna6', 'del')

# select = userAlive.dataUserSELECT('tools', '', 'tool_category', 'brutal', 'tool_name')

# print(select)

# pustaLista = ['dsfdf', '754tww']
# print(pustaLista.index('754tww'))

# profil = userAlive.dataGeneral('today_newsadmin', "kolumna3")
# print(profil)


# para = userAlive.dataUserLogin("panel")

# v1 = para[0]
# v2 = para[1]

# print(v1, v2)

# passwd = userAlive.dataPassLogin(v1, "1234")

# stdpass = passwd[0]
# passone = passwd[1]

# print(stdpass, passone)

# set1 = set()
# set1.add("admin")
# set1.add("admin")

# set2 = set()
# set2.add("root")
# set2.add("admin")

# elementsOut = str(set1.symmetric_difference(set2))

# print(type(elementsOut))

# elementsOutNext1 = elementsOut.strip("{")
# elementsOutNext2 = elementsOutNext1.strip("}")
# elementsOutNext3 = elementsOutNext2.strip("'")

# list1 = []
# list1.append(elementsOutNext3)


# print(list1[0])
