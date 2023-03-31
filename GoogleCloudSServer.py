import socket as s
import mysql.connector
import random

def victimusTool():
    polaczenie_DB = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = polaczenie_DB.cursor()
    gotDB = 'SELECT id, user, haslo, created FROM users_main'
    cursor.execute(gotDB)
    userDataGot = []
    passDataGot = []
    for (id, user, haslo, created) in cursor:
        userDataGot.append(f'{user}')
        passDataGot.append(f'{haslo}')
    polaczenie_DB.commit()
    polaczenie_DB.close()
    VictimusTargetted = random.randrange(50, 196) # od 50 do 195 sa fakeUser dodani
    VictimusName = userDataGot[VictimusTargetted]
    VictimusPass = passDataGot[VictimusTargetted]
    VictimusDone = [str(VictimusName), VictimusPass]
    return VictimusDone

def dataUserLogin(giveNickName):    
    polaczenie_DB = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = polaczenie_DB.cursor()
    userDataGot = set()
    dumpNicks= set()
    gotDB = 'SELECT id, user FROM users_main'
    cursor.execute(gotDB)
    for (id, user) in cursor:
        userDataGot.add(f'{user}')
        dumpNicks.add(f'{user}')
    polaczenie_DB.commit()
    polaczenie_DB.close()
    dumpNicks.discard(giveNickName)
    elementsOut = str(dumpNicks.symmetric_difference(userDataGot))
    converSteps1 = elementsOut.strip("{")
    converSteps2 = converSteps1.strip("}")
    converStepsLast = converSteps2.strip("'")
    login = giveNickName
    tem_set_login = []
    tem_set_login.append(login)
    real_login = tem_set_login[0]    
    elementsOutList = []
    elementsOutList.append(converStepsLast)
    v_login = elementsOutList[0]    
    para = [real_login, v_login]
    return para

def dataPassLogin(giveNickName, inputNickpass):    
    polaczenie_DB = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = polaczenie_DB.cursor()
    givePass = inputNickpass
    dic = {}
    getDataBase = 'SELECT id, user, haslo FROM users_main'
    cursor.execute(getDataBase)
    for (id, user, haslo) in cursor:        
        dic[(f'{user}')] = (f'{haslo}')
    polaczenie_DB.commit()
    giveuser = dic.get(giveNickName)
    std_pass = []
    std_pass.append(givePass)
    standardOne = []
    standardOne.append(giveuser)
    para = []
    para.append(standardOne)
    para.append(std_pass)
    return para

def dataUserAdd(giveNickName, newUserPass):
    ilosc = dataGeneral('users_main', 'user')
    
    if ilosc != None:
        dlugosc = len(ilosc)
    else:
        dlugosc = 0
    identyfikator = dlugosc + 1
    connection = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = connection.cursor()
    # comit byl tutaj
    # punkty_doswiadczenia, aktualne_vcrypto , aktualne_vcoin, aktualne_usd, aktualne_rcrypto, aktualne_profesje, aktualna_zbroja, aktualne_uzbrojenie, aktualny_przedmiot, aktualna_lokalizacja_y, aktualna_lokalizacja_x, lokalizacja_dom_y, lokalizacja_dom_x, lokalizacja_terenu_a_y, lokalizacja_terenu_a_x, lokalizacja_terenu_b_y, lokalizacja_terenu_b_x, , lokalizacja_terenu_c_y, lokalizacja_terenu_c_x, , lokalizacja_terenu_d_y, lokalizacja_terenu_d_x, attack_success, attack_failds, robota_w_toku, aktualny_poziom, aktualna_ranga 
    instartQuery = "INSERT INTO users_main(identyfikator, user, haslo, punkty_doswiadczenia, aktualne_vcrypto , aktualne_vcoin, aktualne_usd, aktualne_rcrypto, aktualne_profesje, aktualna_zbroja, aktualne_uzbrojenie, aktualny_przedmiot, aktualna_lokalizacja_y, aktualna_lokalizacja_x, lokalizacja_dom_y, lokalizacja_dom_x, lokalizacja_terenu_a_y, lokalizacja_terenu_a_x, lokalizacja_terenu_b_y, lokalizacja_terenu_b_x, lokalizacja_terenu_c_y, lokalizacja_terenu_c_x, lokalizacja_terenu_d_y, lokalizacja_terenu_d_x, attack_success, attack_failds, robota_w_toku, aktualny_poziom, aktualna_ranga) VALUES(%(identyfikator)s, %(user)s, %(haslo)s, %(punkty_doswiadczenia)s, %(aktualne_vcrypto)s , %(aktualne_vcoin)s, %(aktualne_usd)s, %(aktualne_rcrypto)s, %(aktualne_profesje)s, %(aktualna_zbroja)s, %(aktualne_uzbrojenie)s, %(aktualny_przedmiot)s, %(aktualna_lokalizacja_y)s, %(aktualna_lokalizacja_x)s, %(lokalizacja_dom_y)s, %(lokalizacja_dom_x)s, %(lokalizacja_terenu_a_y)s, %(lokalizacja_terenu_a_x)s, %(lokalizacja_terenu_b_y)s, %(lokalizacja_terenu_b_x)s, %(lokalizacja_terenu_c_y)s, %(lokalizacja_terenu_c_x)s, %(lokalizacja_terenu_d_y)s, %(lokalizacja_terenu_d_x)s, %(attack_success)s, %(attack_failds)s, %(robota_w_toku)s, %(aktualny_poziom)s, %(aktualna_ranga)s)"
    mojeDane = {
        'identyfikator' : str(identyfikator),
        'user' : str(giveNickName),
        'haslo' : str(newUserPass),
        'punkty_doswiadczenia' : str(1),
        'aktualne_vcrypto' : str(1),
        'aktualne_vcoin' : str(0),
        'aktualne_usd' : str(0),
        'aktualne_rcrypto' : str(0),
        'aktualne_profesje' : str('Hacker Adept'),
        'aktualna_zbroja' : str("['ON', 'ON', 'OFF', 'ON', 'OFF', 'ON', 'OFF', 'OFF', 'ON', 'OFF', 'ON', 'OFF', 'ON', 'ON', 'OFF', 'ON', 'OFF']"),
        'aktualne_uzbrojenie' : str('Nóż myśliwskie'),
        'aktualny_przedmiot' : str('Telefon'),
        'aktualna_lokalizacja_y' : str('52.294111'),
        'aktualna_lokalizacja_x' : str('21.022641'),
        'lokalizacja_dom_y' : str('52.294246'), 
        'lokalizacja_dom_x' : str('21.022661'),
        'lokalizacja_terenu_a_y' : str('52.294206'),
        'lokalizacja_terenu_a_x' : str('22.284125'),
        'lokalizacja_terenu_b_y' : str('52.294296'),
        'lokalizacja_terenu_b_x' : str('22.284125'),
        'lokalizacja_terenu_c_y' : str('52.294256'),
        'lokalizacja_terenu_c_x' : str('22.284125'),
        'lokalizacja_terenu_d_y' : str('52.294226'),
        'lokalizacja_terenu_d_x' : str('22.284125'),
        'attack_success' : str(0),
        'attack_failds' : str(0),
        'robota_w_toku' : str(0),
        'aktualny_poziom' : str(1),
        'aktualna_ranga' : str('Uczeń hakerstwa')
                }
    cursor.execute(instartQuery, mojeDane)
    connection.commit()
    connection.close()

def dataUserProfil(giveNickName, profil):    
    polaczenie_DB = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = polaczenie_DB.cursor()    
    dic = {}     
    getDataBase = 'SELECT id, user, '+ profil +' FROM users_main'
    cursor.execute(getDataBase)
    for (id, user, profil) in cursor:        
        dic[(f'{user}')] = (f'{profil}')
    polaczenie_DB.commit()
    giveuser = dic.get(giveNickName)      
    return str(giveuser)

def dataGeneral(baza, atrybut):    
    polaczenie_DB = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = polaczenie_DB.cursor()           
    getDataBase = 'SELECT id, '+ atrybut +' FROM ' + baza
    cursor.execute(getDataBase)
    atrybutList = []
    for (id, atrybut) in cursor:        
        atrybutList.append(str(atrybut))
    polaczenie_DB.commit()  
    polaczenie_DB.close()
    try:
        atrybutList[0] 
    except:
        atrybutList = None
    return atrybutList

def dataUserCREATE6(bazaUser, wprowadzNick):    
    connection = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = connection.cursor()
    connection.commit()
    try:
        createTable = "CREATE TABLE db_apka_python."+ bazaUser + wprowadzNick + " ( id INT NOT NULL AUTO_INCREMENT, kolumna1 TEXT, kolumna2 TEXT, kolumna3 TEXT, kolumna4 TEXT, kolumna5 TEXT, kolumna6 TEXT, PRIMARY KEY (id));"
        cursor.execute(createTable)
        print("dodano tabele do bazy danych ")
    except:
        print(wprowadzNick, " Posiada autoryzację")
    connection.close()

def dataUserINSERT6(bazaUser, wprowadzNick, kolumna1, kolumna2, kolumna3, kolumna4, kolumna5, kolumna6):    
    connection = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = connection.cursor()
    instartQuery = "INSERT INTO "+ bazaUser + wprowadzNick + "(kolumna1, kolumna2, kolumna3, kolumna4, kolumna5, kolumna6) VALUES(%(kolumna1)s,%(kolumna2)s,%(kolumna3)s,%(kolumna4)s,%(kolumna5)s,%(kolumna6)s);"
    mojeDane = {
        'kolumna1' : str(kolumna1),
        'kolumna2' : str(kolumna2),
        'kolumna3' : str(kolumna3),
        'kolumna4' : str(kolumna4),
        'kolumna5' : str(kolumna5),
        'kolumna6' : str(kolumna6)
                }
    print(kolumna1)
    cursor.execute(instartQuery, mojeDane)    
    connection.commit()
    connection.close()

def dataUserUPDATE(bazaUser, wprowadzNick, kolumna, updateKol, idforchanged):    
    connection = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = connection.cursor()
    instartQuery = "UPDATE "+ bazaUser + wprowadzNick + " SET " + kolumna + " = %s WHERE identyfikator = %s;" 
    updateData = (updateKol, idforchanged)
    cursor.execute(instartQuery, updateData)    
    connection.commit()
    connection.close()

def dataSuperUPDATE(bazaUser, wprowadzNick, kolumna, updateKol, identyfikator, idforchanged):    
    connection = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = connection.cursor()
    UPDATE = "UPDATE "
    SET = " SET "
    WHERE = " = %s WHERE "
    END = " = %s;"
    instartQuery = UPDATE + bazaUser + wprowadzNick + SET + kolumna + WHERE + identyfikator + END
    updateData = (updateKol, idforchanged)
    cursor.execute(instartQuery, updateData)    
    connection.commit()
    connection.close()

def dataUserDELETE(bazaUser, wprowadzNick, kolumna6, delrow):    
    connection = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = connection.cursor()
    instartQuery = "DELETE FROM "+ bazaUser + wprowadzNick + " WHERE " + kolumna6 + " = %(kolumna6)s;" 
    updateData = {        
        'kolumna6' : delrow
                }
    cursor.execute(instartQuery, updateData)    
    connection.commit()
    connection.close()

SEP = "|"

HOST = "" #s.gethostbyname(s.gethostname()) 
PORT = 3389
BUFFER = 3072

server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(2048)
export = ''
while True:
    print(f'LISTENING ON {HOST}')
    client_socket, address = server_socket.accept()
    print(f'Uzyskano połączenie od {address}')
 
    name = client_socket.recv(BUFFER).decode('utf8')
    commandLine = name.split(SEP)

    commmandList = []
    for i in commandLine:
        commmandList.append(i)    

    if commmandList[0] == 'victimusTool':
        args = int(len(commmandList) - 1)
        print(f'[{address[0]} : {address[1]} ] KOMENDA: {commmandList[0]}')
        print(str(args) + ' przekazano argumentów')
        try:
            halfProduct = victimusTool()
        
            export = halfProduct[0] + SEP + halfProduct[1]
        except:
            export = 'FAILED MISSION 508F'

        msg = str(export).encode('utf8')
        client_socket.send(msg)

    elif commmandList[0] == 'dataUserLogin':        
        args = int(len(commmandList) - 1)
        print(f'[{address[0]} : {address[1]} ] KOMENDA: {commmandList[0]}')
        giveNickName = commmandList[1]
        try:
            para = dataUserLogin(giveNickName)
            export = str(para[0]+SEP+str(para[1]))

            msg = str(export).encode('utf8')
            client_socket.send(msg)
        except:
            pass

    elif commmandList[0] == 'dataPassLogin':
        args = int(len(commmandList) - 1)
        print(f'[{address[0]} : {address[1]} ] KOMENDA: {commmandList[0]}')
        giveNickName = commmandList[1]
        inputNickpass = commmandList[2]
        try:
            para = dataPassLogin(giveNickName, inputNickpass)
            para0 = para[0]
            para1 = para[1]

            para0 = str(para0)
            para1 = str(para1)
            export = para0+SEP+para1

            msg = str(export).encode('utf8')
            client_socket.send(msg)
        except:
            pass
    elif commmandList[0] == 'dataUserAdd':
        args = int(len(commmandList) - 1)
        print(f'[{address[0]} : {address[1]} ] KOMENDA: {commmandList[0]}')
        giveNickName = commmandList[1]
        newUserPass = commmandList[2]
        try:
            dataUserAdd(giveNickName, newUserPass)
        except:
            pass
        export = 'OPERATION END'

        msg = str(export).encode('utf8')
        client_socket.send(msg)

    elif commmandList[0] == 'dataUserProfil':
        args = int(len(commmandList) - 1)
        print(f'[{address[0]} : {address[1]} ] KOMENDA: {commmandList[0]}')
        giveNickName = commmandList[1]
        profil = commmandList[2]
        try:
            export = dataUserProfil(giveNickName, profil)
            print(export)
            msg = str(export).encode('utf8')        
            client_socket.send(msg)
        except:
            pass

    elif commmandList[0] == 'dataGeneral':
        args = int(len(commmandList) - 1)
        baza = commmandList[1]
        atrybut = commmandList[2]
        print(f'[{address[0]} : {address[1]} ] KOMENDA: {commmandList[0]}')
        print(baza, atrybut)
        try:
            lista = dataGeneral(baza, atrybut)
            strlista = str(lista)
            
            print("string lista "+ strlista)

            listaLstrip = strlista.lstrip('[')
            listaRstrip = listaLstrip.rstrip(']')
            splitLista = listaRstrip.split("', '")
            newString = ""
            for i in splitLista:
                il = i.lstrip("'")
                ir = il.rstrip("'")
                newString += ir+SEP
            newString = newString.rstrip(SEP)
            export = newString
            print(export)
            msg = str(export).encode('utf8')
            client_socket.send(msg)
        except:
            pass

    elif commmandList[0] == 'dataUserCREATE6':
        print(f'[{address[0]} : {address[1]} ] KOMENDA: {commmandList[0]}')
        args = int(len(commmandList) - 1)
        bazaUser = commmandList[1]
        wprowadzNick = commmandList[2]
        try:
            dataUserCREATE6(bazaUser, wprowadzNick)
        except:
            pass
        export = 'OPERATION END'
        print(bazaUser, wprowadzNick)
        msg = str(export).encode('utf8')
        client_socket.send(msg)

    elif commmandList[0] == 'dataUserINSERT6':
        args = int(len(commmandList) - 1)
        print(f'[{address[0]} : {address[1]} ] KOMENDA: {commmandList[0]}')
        bazaUser = commmandList[1]
        wprowadzNick = commmandList[2]
        kolumna1 = commmandList[3]
        kolumna2 = commmandList[4]
        kolumna3 = commmandList[5]
        kolumna4 = commmandList[6]
        kolumna5 = commmandList[7]
        kolumna6 = commmandList[8]
        try:
            dataUserINSERT6(bazaUser, wprowadzNick, str(kolumna1), str(kolumna2), str(kolumna3), str(kolumna4), str(kolumna5), str(kolumna6))
        except:
            pass
        export = 'OPERATION END'
        print(bazaUser, wprowadzNick)
        msg = str(export).encode('utf8')
        client_socket.send(msg)

    elif commmandList[0] == 'dataUserUPDATE':
        args = int(len(commmandList) - 1)
        print(f'[{address[0]} : {address[1]} ] KOMENDA: {commmandList[0]}')
        bazaUser = commmandList[1]
        wprowadzNick = commmandList[2]
        kolumna = commmandList[3]
        updateKol = commmandList[4]
        idforchanged = commmandList[5]
        try:
            dataUserUPDATE(bazaUser, wprowadzNick, kolumna, updateKol, idforchanged)
        except:
            pass
        export = 'OPERATION END'
        print(bazaUser, wprowadzNick)
        msg = str(export).encode('utf8')
        client_socket.send(msg)

    elif commmandList[0] == 'dataSuperUPDATE':
        print(f'[{address[0]} : {address[1]} ] KOMENDA: {commmandList[0]}')
        args = int(len(commmandList) - 1)
        bazaUser = commmandList[1]
        wprowadzNick = commmandList[2]
        kolumna = commmandList[3]
        updateKol = commmandList[4]
        identyfikator = commmandList[5]
        idforchanged = commmandList[6]
        try:
            dataSuperUPDATE(bazaUser, wprowadzNick, kolumna, updateKol, identyfikator, idforchanged)
        except:
            pass
        export = 'OPERATION END'
        print(bazaUser, wprowadzNick)
        msg = str(export).encode('utf8')
        client_socket.send(msg)

    elif commmandList[0] == 'dataUserDELETE':
        
        args = int(len(commmandList) - 1)
        bazaUser = commmandList[1]
        wprowadzNick = commmandList[2]
        kolumna6 = commmandList[3]
        delrow = commmandList[4]
        try:
            dataUserDELETE(bazaUser, wprowadzNick, kolumna6, delrow)
        except:
            pass
        print(f'[{address[0]} : {address[1]} ] KOMENDA: {commmandList[0]}')
        print(str(args) + ' przekazano argumentów')
        export = 'OPERATION END'
        print(bazaUser, wprowadzNick)
        msg = str(export).encode('utf8')
        client_socket.send(msg)
    else:
        print(f'[{address[0]} : {address[1]} ] KOMENDY: {commmandList}')

    

    
