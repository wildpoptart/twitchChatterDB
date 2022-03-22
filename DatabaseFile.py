#Database File
import sqlite3

def createTable():
    conn = sqlite3.connect(r'C:\Users\Stas\Documents\coding\twitchChatterDB\chatterDB.db')
    c = conn.cursor()
    print("Opened db successfully")

    c.execute('CREATE TABLE IF NOT EXISTS USERS(Name TEXT, Type TEXT, Watches TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS BROADCASTERS (Name TEXT, Type TEXT, Watches TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS VIPS (Name TEXT, Type TEXT, Watches TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS MODERATORS (Name TEXT, Type TEXT, Watches TEXT)')
    c.execute('CREATE TABLE IF NOT EXISTS VIEWERS (Name TEXT, Type TEXT, Watches TEXT)')

    print("db created")
    conn.close()

def insertData(name,type,table,watches):
    #print(name,type)
    conn = sqlite3.connect(r'C:\Users\Stas\Documents\coding\twitchChatterDB\chatterDB.db')
    c = conn.cursor()
    #print("Opened db")
    c.execute("INSERT INTO "+table+"(Name, Type, Watches) VALUES(?,?,?)",(name,type,watches))
    conn.commit()
    conn.close()
    #print("Closed db")

def combineData():
    conn = sqlite3.connect(r'C:\Users\Stas\Documents\coding\twitchChatterDB\chatterDB.db')
    c = conn.cursor()
    c.execute('INSERT INTO USERS SELECT * FROM BROADCASTERS')
    c.execute('INSERT INTO USERS SELECT * FROM VIPS')
    c.execute('INSERT INTO USERS SELECT * FROM MODERATORS')
    c.execute('INSERT INTO USERS SELECT * FROM VIEWERS')
    conn.commit()
    conn.close()

def dupRemove():
    conn = sqlite3.connect(r'C:\Users\Stas\Documents\coding\twitchChatterDB\chatterDB.db')
    c = conn.cursor()
    with conn:
        c.execute("DELETE FROM BROADCASTERS WHERE EXISTS (SELECT 1 FROM BROADCASTERS p2 WHERE BROADCASTERS.Name = p2.Name AND BROADCASTERS.Type = p2.Type AND BROADCASTERS.Watches = p2.Watches AND  BROADCASTERS.ROWID > p2.ROWID)")
        c.execute("DELETE FROM VIPS WHERE EXISTS (SELECT 1 FROM VIPS p2 WHERE VIPS.Name = p2.Name AND VIPS.Type = p2.Type AND VIPS.ROWID > p2.ROWID)")
        c.execute("DELETE FROM MODERATORS WHERE EXISTS (SELECT 1 FROM MODERATORS p2 WHERE MODERATORS.Name = p2.Name AND MODERATORS.Type = p2.Type AND MODERATORS.Watches = p2.Watches AND MODERATORS.ROWID > p2.ROWID)")
        c.execute("DELETE FROM VIEWERS WHERE EXISTS (SELECT 1 FROM VIEWERS p2 WHERE VIEWERS.Name = p2.Name AND VIEWERS.Type = p2.Type AND VIEWERS.Watches = p2.Watches AND VIEWERS.ROWID > p2.ROWID)")
        c.execute("DELETE FROM USERS WHERE EXISTS (SELECT 1 FROM USERS p2 WHERE USERS.Name = p2.Name AND USERS.Type = p2.Type AND USERS.Watches = p2.Watches AND USERS.ROWID > p2.ROWID)")
        #print(c.fetchall())
    conn.close()