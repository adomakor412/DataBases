import mysql.connector

def connect():
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS quantacts (id INTEGER PRIMARY KEY, first text, last text, number text, email text);
    ''')
    conn.commit()
    conn.close()

def insert(first,last,number, email):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    query = f'INSERT INTO quantacts (first,last,number,email) VALUES ({first}, {last}, {number}, {email})'
    query.format( {first:'first'}, {last:'last'}, {number:'number'}, {email:'email'})
    cur.execute(query)
    conn.commit()
    conn.close()
    
def view():
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM quantacts
    ''')
    rows = cur.fetchall()
    conn.close()
    
def search(first,last,number, email):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    cur.execute(
        '''SELECT * FROM quantacts WHERE first=? OR last=? OR number=? OR email=?''', (first, last, number, email)
   )
    rows = cur.fetchall()
    conn.close()
    
def delete(variable_id):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    cur.execute(
        '''DELETE FROM quantacts WHERE id=?''', (variable_id)
   )
    rows = cur.fetchall()
    conn.close()
    
def update(variable_id,first,last,number, email):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    cur.execute(
        '''UPDATE quantacts SET first=?,last=?,number=?, email=?, where variable_id=?''', 
        (variable_id,first, last, number, email)
   )
    rows = cur.fetchall()
    conn.close()