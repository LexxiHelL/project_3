import sqlite3
con = sqlite3.connect("Common_base.sqlite")
cur = con.cursor()


def num_script(a):
    # Выполнение запроса и получение всех результатов
    result = cur.execute(f'''SELECT * FROM Numbers_of_hum Where num = {a}''').fetchall()

    # Вывод результатов на экран
    for elem in result:
        return f'Страна: {elem[1]}', f'Регион: {elem[2]}', f'Оператор: {elem[3]}', f'ФИО: {elem[4]}', \
                f'Возможный адрес: {elem[5]}', f'Дата рождения: {elem[6]}', f'Email: {elem[7]}', \
                f'Наличие госуслуг: {elem[8]}', f'VK: {elem[9]}', f'telegram: {elem[10]}', \
                f'WhatsApp: {elem[11]}', f'Tiktok: {elem[12]}'
    con.close()


def name_script(a):
    # Выполнение запроса и получение всех результатов
    result = cur.execute(f'''SELECT * FROM Numbers_of_hum Where Names = "{a}"''').fetchall()

    # Вывод результатов на экран
    for elem in result:
        return f'Номер телефона: {elem[0]}', f'Страна: {elem[1]}', f'Регион: {elem[2]}', f'Оператор: {elem[3]}', \
                f'Возможный адрес: {elem[5]}', f'Дата рождения: {elem[6]}', f'Email: {elem[7]}', \
                f'Наличие госуслуг: {elem[8]}', f'VK: {elem[9]}', f'telegram: {elem[10]}', \
                f'WhatsApp: {elem[11]}', f'Tiktok: {elem[12]}'
    con.close()


def email_script(a):
    # Выполнение запроса и получение всех результатов
    result = cur.execute(f'''SELECT * FROM Numbers_of_hum Where email = "{a}"''').fetchall()

    # Вывод результатов на экран
    for elem in result:
        return f'Номер телефона: {elem[0]}', f'Страна: {elem[1]}', f'Регион: {elem[2]}', f'Оператор: {elem[3]}', \
            f'ФИО: {elem[4]}', f'Возможный адрес: {elem[5]}', f'Дата рождения: {elem[6]}', \
            f'Наличие госуслуг: {elem[8]}', f'VK: {elem[9]}', f'telegram: {elem[10]}', \
            f'WhatsApp: {elem[11]}', f'Tiktok: {elem[12]}'
    con.close()


def VK_script(a):
    # Выполнение запроса и получение всех результатов
    result = cur.execute(f'''SELECT * FROM Numbers_of_hum Where VK_id = {a}''').fetchall()

    # Вывод результатов на экран
    for elem in result:
        return f'Номер телефона: {elem[0]}', f'Страна: {elem[1]}', f'Регион: {elem[2]}', f'Оператор: {elem[3]}', \
            f'ФИО: {elem[4]}', f'Возможный адрес: {elem[5]}', f'Дата рождения: {elem[6]}', f'Email: {elem[7]}',\
            f'Наличие госуслуг: {elem[8]}', f'telegram: {elem[10]}', \
            f'WhatsApp: {elem[11]}', f'Tiktok: {elem[12]}'
    con.close()


def add_user_data(a):
    # Если номера нет - добавляем
    cur.execute(f'''INSERT INTO Numbers_of_hum (num, Country, regeon, Operator, Names, date, adress, email, Gos, VK_id,\
            telegram, WhatsApp, TikTok) VALUES {(a, 'неизвестно', 'неизвестно', 'неизвестно', 'неизвестно', 
                                                 'неизвестно', 'неизвестно', 'неизвестно', 'Нет', 'Нет',
                                                 'Нет', 'Нет', 'Нет')}''')
    con.commit()
