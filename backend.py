import mysql.connector

#def openConn(database, user, password, host)

def initiateTable():
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS quantact1 (id int NOT NULL AUTO_INCREMENT, first text, last text, number text, email text, PRIMARY KEY (id));
    ''')
    conn.commit()
    conn.close()

def insert(first,last,number, email):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    query = "INSERT INTO quantact1 (first,last,number,email) VALUES ('" + first + "', '" + last + "', '" + str(number) + "', '" + email + "')"
    #query.format()
    #query = f'INSERT INTO ({first},{last},{number},{email}) VALUES (first, last, number, email)'
    #query.format( {first:'first'}, {last:'last'}, {number:'number'}, {email:'email'})
    #print(query)
    cur.execute(query)
    conn.commit()
    conn.close()
    
def view():
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM quantact1
    ''')
    rows = cur.fetchall()
    conn.close()
    return rows
    
def search(first,last,number, email):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    query = "SELECT * FROM quantact1 WHERE first='"+first+"' OR last='"+last+"' OR number='"+number+"' OR email='"+email+"'"
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows
    
def delete(variable_id):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    cur.execute(
        '''DELETE FROM quantact1 WHERE id=?''', (variable_id)
    )
    rows = cur.fetchall()
    conn.close()
    
def update(variable_id,first,last,number, email):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    cur.execute(
        '''UPDATE quantact1 SET first=?,last=?,number=?, email=?, where variable_id=?''', 
        (variable_id,first, last, number, email)
   )
    rows = cur.fetchall()
    conn.close()