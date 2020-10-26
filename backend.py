import mysql.connector

#def openConn(database, user, password, host)

def initiateTable():
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    #query0 = '''DROP DATABASE IF EXISTS Example3NF;'''
    query1 = '''DROP TABLE IF EXISTS quantact;'''
    query2 = '''
        CREATE TABLE IF NOT EXISTS quantact (prime_id INTEGER KEY AUTO_INCREMENT, first text, last text, number text, email text);
    '''
    cur.execute(query1)
    cur.execute(query2)
    conn.commit()
    conn.close()
    
def search(first,last,number, email):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    inputs = (first,last,number, email)
    query = "SELECT * FROM quantact WHERE first=%s OR last=%s OR number=%s OR email=%s"
    cur.execute(query, inputs)
    rows = cur.fetchall()
    conn.close()
    return rows

def insert(first,last,number, email):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    inputs = (first,last,number, email)
    #query = "INSERT INTO quantact (first,last,number,email) VALUES (%s,%s,%s,%s)"
    query = "INSERT INTO quantact (first,last,number,email) VALUES ('%s','%s','%s','%s')"
    #execute = cur.execute(query,inputs) #Try not to rely on mysql.connector library to format strings
    execute = cur.execute((query %inputs))
    conn.commit()
    conn.close()
    return search(first,last,number, email)
    
def view():
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    cur.execute('''
        SELECT * FROM quantact;
    ''')
    rows = cur.fetchall()
    conn.close()
    return rows
    
def delete(variable_id):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost",buffered=True)
    cur = conn.cursor()
    inputs = str(variable_id)
    query1= '''SELECT * FROM quantact;'''
    query2 = "DELETE FROM quantact WHERE prime_id = %s"#The EXTENDED PYTHON FORMAT CODE vs tuple in mysql.connect
    cur.execute(query1)
    cur.execute((query2 %inputs))#string formating needs tuple if not using function
    conn.commit()
    conn.close()
    return 
    
def update(variable_id, first, last, number, email):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost",buffered=True)
    cur = conn.cursor()
    inputs = (first, last, number, email, str(variable_id))
    query = "UPDATE quantact SET first= '%s',last= '%s', number= '%s', email= '%s' WHERE prime_id = %s;"
    cur.execute((query %inputs))
    conn.commit()
    conn.close()
    return search(first,last,number, email)

def reset():
    #potential design in running main script in a function module: refactor opportunity for .py
    return 