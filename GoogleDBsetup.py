import mysql.connector

a = input('Czy utworzyć tabelę <Users>? [y] / CTRL+C')
if a != 'y':
    quit()
else:
    connection = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = connection.cursor()
    connection.commit()
    try:
        createTable = "CREATE TABLE db_apka_python.users_main (id INT NOT NULL AUTO_INCREMENT, identyfikator INT, user TEXT, haslo TEXT, created DATETIME, punkty_doswiadczenia TEXT, aktualne_vcrypto TEXT, aktualne_vcoin TEXT, aktualne_usd TEXT, aktualne_rcrypto TEXT, aktualne_profesje TEXT, aktualna_zbroja TEXT, aktualne_uzbrojenie TEXT, aktualny_przedmiot TEXT, aktualna_lokalizacja_y TEXT, aktualna_lokalizacja_x TEXT, lokalizacja_dom_y TEXT, lokalizacja_dom_x TEXT, lokalizacja_terenu_a_y TEXT, lokalizacja_terenu_a_x TEXT, lokalizacja_terenu_b_y TEXT, lokalizacja_terenu_b_x TEXT, lokalizacja_terenu_c_y TEXT, lokalizacja_terenu_c_x TEXT, lokalizacja_terenu_d_y TEXT, lokalizacja_terenu_d_x TEXT, attack_success TEXT, attack_failds TEXT, robota_w_toku TEXT, aktualny_poziom TEXT, aktualna_ranga TEXT, PRIMARY KEY (id));"
        cursor.execute(createTable)
        print("dodano do bazy danych ")
    except:
        print("excepting script")
    connection.close()

a = input('Czy utworzyć tabelę <news>? [y] / CTRL+C ')
if a != 'y':
    quit()
else:
    connection = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = connection.cursor()
    connection.commit()
    try:
        createTable = "CREATE TABLE db_apka_python.news (id INT NOT NULL AUTO_INCREMENT, title TEXT, data TEXT, content TEXT, PRIMARY KEY (id));"
        cursor.execute(createTable)
        print("dodano do bazy danych ")
    except:
        print("excepting script")
    connection.close()

a = input('Czy utworzyć tabelę <targets>? [y] / CTRL+C ')
if a != 'y':
    quit()
else:
    connection = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = connection.cursor()
    connection.commit()
    try:
        createTable = "CREATE TABLE db_apka_python.targets (id INT NOT NULL AUTO_INCREMENT, ip_url TEXT, port TEXT, category TEXT, PRIMARY KEY (id));"
        cursor.execute(createTable)
        print("dodano do bazy danych ")
    except:
        print("excepting script")
    connection.close()

a = input('Czy utworzyć tabelę <tools>? [y] / CTRL+C ')
if a != 'y':
    quit()
else:
    connection = mysql.connector.connect(user='root', password='h16mwmw0018$100M', host='34.118.67.187', database='db_apka_python')
    cursor = connection.cursor()
    connection.commit()
    try:
        createTable = "CREATE TABLE db_apka_python.tools (id INT NOT NULL AUTO_INCREMENT, tool_name TEXT, tool_descr TEXT, tool_category TEXT, tool_command TEXT, PRIMARY KEY (id));"
        cursor.execute(createTable)
        print("dodano do bazy danych ")
    except:
        print("excepting script")
    connection.close()