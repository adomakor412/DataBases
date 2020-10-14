import mysql.connector

def connect():
    conn = mysql.connector.connect(database="mydb")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS quantacts (id INTEGER PRIMARY KEY, first text, last text, number text, email text);
    ''')
    conn.commit()
    conn.close()

def insert(first,last,number, email):
    conn = mysql.connector.connect("mydb.db")
    cur = conn.cursor()
    cur.execute(
        '''INSERT INTO quantacts VALUES (NULL,?,?,?)''',(first, last, number, email))
    conn.commit()
    conn.close()
    
def view():
    conn = mysql.connector.connect(database="mydb.db")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM quantacts
    ''')
    rows = cur.fetchall()
    conn.close()
    
def search(first,last,number, email):
    conn = mysql.connector.connect("mydb.db")
    cur = conn.cursor()
    cur.execute(
        '''SELECT * FROM quantacts WHERE first=? OR last=? OR number=? OR email=?''', (first, last, number, email)
   )
    rows = cur.fetchall()
    conn.close()
    
def delete(variable_id):
    conn = mysql.connector.connect("mydb.db")
    cur = conn.cursor()
    cur.execute(
        '''DELETE FROM quantacts WHERE id=?''', (variable_id)
   )
    rows = cur.fetchall()
    conn.close()
    
def update(variable_id,first,last,number, email):
    conn = mysql.connector.connect("mydb.db")
    cur = conn.cursor()
    cur.execute(
        '''UPDATE quantacts SET first=?,last=?,number=?, email=?, where variable_id=?''', 
        (variable_id,first, last, number, email)
   )
    rows = cur.fetchall()
    conn.close()