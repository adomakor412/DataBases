import mysql.connector
import csv


def initiateTable():
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    query1 = '''DROP TABLE IF EXISTS DirectedEdges;'''
    query2 = '''
        CREATE TABLE DirectedEdges(source INT, target INT, PRIMARY KEY (source, target));
        '''
    cur.execute(query1) 
    cur.execute(query2)

    with open('question1/graph.csv', 'r') as file:
        csv_data = csv.reader(file)
        next(csv_data,None)
        for row in csv_data:
            source, target = int(row[0]), int(row[1])
            
            cur.execute("INSERT INTO DirectedEdges (source, target) VALUES (%s, %s)", (source, target))
    cur.execute('SELECT * FROM DirectedEdges;')
    rows = cur.fetchall()
    print(rows)
    conn.commit()
    conn.close()
    return
    
def checkConnected(source,target,length):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    inputs = (source,target,length)
    
    query0 = '''
        DROP PROCEDURE IF EXISTS checkConnected;
        '''
    query1 = '''
        CREATE PROCEDURE checkConnected(IN source INT, IN target INT, IN length INT, OUT connected CHAR(20))
        BEGIN
            DECLARE len_count INT;
            SELECT COUNT(*)
            FROM
            (SELECT *
            FROM DirectedEdges 
            WHERE DirectedEdges.source between source and target
            and directededges.target = target
            LIMIT length) as A
            INTO len_count;
            IF len_count - 1 < length and len_count > 0
            THEN
                SET connected := 'True';
            ELSE
                SET connected := 'False';
            END IF;
        END
       
        '''
    query2 = '''
        CALL checkConnected(%s, %s, %s, @connected);
        '''
    query3 = '''
        SELECT @connected;
        '''
    cur.execute(query0)
    cur.execute(query1)
    cur.execute(query2, inputs)
    #conn.commit()
    cur.execute(query3)
    rows = cur.fetchone()#YOU MUST DO A FETCH TO PRINT IN PYTHON!!!!
    print(rows[0])
    #conn.commit()
    conn.close()
    
    return 

    