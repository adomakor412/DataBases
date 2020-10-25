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
    query = "SELECT * FROM quantact WHERE first='"+str(first)+"' OR last='"+str(last)+"' OR number='"+str(number)+"' OR email='"+str(email)+"';"
    cur.execute(query)
    rows = cur.fetchall()
    conn.close()
    return rows

def insert(first,last,number, email):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    query = "INSERT INTO quantact (first,last,number,email) VALUES ('" + first + "', '" + last + "', '" + str(number) + "', '" + email + "');"
    #query.format()
    #query = f'INSERT INTO ({first},{last},{number},{email}) VALUES (first, last, number, email)'
    #query.format( {first:'first'}, {last:'last'}, {number:'number'}, {email:'email'})
    #print(query)
    cur.execute(query)
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
    query1= '''SELECT * FROM quantact;'''
    query2 = "DELETE FROM quantact WHERE prime_id ="+str(variable_id)
    cur.execute(query1)
    cur.execute(query2)
    #rows = cur.fetchall()
    conn.commit()
    conn.close()
    #print('Your are deleting contact: ', rows)
    return 
    
def update(variable_id,first,last,number, email):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost",buffered=True)
    cur = conn.cursor()
    query = "UPDATE quantact SET first='"+first+"',last='"+last+"', number='"+number+"', email='"+email+"' where prime_id = "+str(variable_id)+";"
    cur.execute(query)
    #rows = cur.fetchone()
    conn.commit()
    conn.close()
    #return search(first,last,number, email)
    return

def reset():
    return 