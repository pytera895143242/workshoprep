import sqlite3

def reg_user(id,country):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(""" CREATE TABLE IF NOT EXISTS user_time (
        id,
        country,
        status
        ) """)
    db.commit()

    sql.execute(f"SELECT id FROM user_time WHERE id = {id}")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO user_time VALUES (?,?,?)", (id,country,'0'))
        db.commit()
    else:
        sql.execute(f"UPDATE user_time SET country = '{country}' WHERE id ={id}")
        db.commit()




    sql.execute(""" CREATE TABLE IF NOT EXISTS trafik (
                    chanel,
                    parametr,
                    chat_channel,
                    person
                    ) """)
    db.commit()
    sql.execute(f"SELECT chanel FROM trafik WHERE chanel = 'channel1'")
    if sql.fetchone() is None:
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?,?)", ('channel1', 'chennel', -111, 100))
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?,?)", ('channel2', 'chennel', -111, 100))
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?,?)", ('channel3', 'chennel', -111, 100))
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?,?)", ('channel4', 'chennel4', -111, 100))
        sql.execute(f"INSERT INTO trafik VALUES (?,?,?,?)", ('channel5', 'https://t.me/chennel4/', 0, 100))
        db.commit()


def members_list():
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    all = sql.execute(f"SELECT COUNT(*) FROM user_time" ).fetchone()[0]
    good = sql.execute(f"SELECT COUNT(*) FROM user_time WHERE status = '1'" ).fetchone()[0]

    return [all, good]




def update_country(id, country):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET country = '{country}' WHERE id = {id}")
    db.commit()


def update_status(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE user_time SET status = '1' WHERE id = {id}")
    db.commit()



def get_country(id):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    country = sql.execute(f"SELECT country FROM user_time WHERE id = {id}").fetchone()
    return country



def cheak_traf():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    c1 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel1'").fetchone()[0]
    c2 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel2'").fetchone()[0]
    c3 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel3'").fetchone()[0]
    c4 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel4'").fetchone()[0]
    c5 = sql.execute(f"SELECT parametr FROM trafik WHERE chanel = 'channel5'").fetchone()[0]
    list = [c1,c2,c3,c4,c5]
    return list


def obnovatrafika1(link_one,id_channel1):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE trafik SET parametr= '{link_one}' WHERE chanel = 'channel1'")
    sql.execute(f"UPDATE trafik SET chat_channel= '{id_channel1}' WHERE chanel = 'channel1'")
    db.commit()

def obnovatrafika2(link_one,id_channel1):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE trafik SET parametr= '{link_one}' WHERE chanel = 'channel2'")
    sql.execute(f"UPDATE trafik SET chat_channel= '{id_channel1}' WHERE chanel = 'channel2'")
    db.commit()


def obnovatrafika3(link_one,id_channel1):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE trafik SET parametr= '{link_one}' WHERE chanel = 'channel3'")
    sql.execute(f"UPDATE trafik SET chat_channel= '{id_channel1}' WHERE chanel = 'channel3'")
    db.commit()

def obnovatrafika4(link_one,id_channel1):
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    sql.execute(f"UPDATE trafik SET parametr= '{link_one}' WHERE chanel = 'channel4'")
    sql.execute(f"UPDATE trafik SET chat_channel= '{id_channel1}' WHERE chanel = 'channel4'")
    db.commit()

def cheak_chat_id():
    db = sqlite3.connect('server.db')
    sql = db.cursor()
    i1 = sql.execute(f"SELECT chat_channel FROM trafik WHERE chanel = 'channel1'").fetchone()[0]
    i2 = sql.execute(f"SELECT chat_channel FROM trafik WHERE chanel = 'channel2'").fetchone()[0]
    i3 = sql.execute(f"SELECT chat_channel FROM trafik WHERE chanel = 'channel3'").fetchone()[0]
    i4 = sql.execute(f"SELECT chat_channel FROM trafik WHERE chanel = 'channel4'").fetchone()[0]

    return i1,i2,i3,i4




