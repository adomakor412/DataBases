import mysql.connector


def initiateTable():
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    query1 = '''DROP TABLE IF EXISTS DirectedEdges;'''
    query2 = '''
        CREATE TABLE DirectedEdges(source INT, target INT, PRIMARY KEY (source, target));
        '''
    query3 = ''' 
        SET GLOBAL local_infile=1;
        SHOW VARIABLES LIKE "question1/graph.csv";
        LOAD DATA INFILE 'question1/graph.csv' INTO TABLE DirectedEdges
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY ''
        IGNORE 1 ROWS;
        '''
    cur.execute(query1) 
    cur.execute(query2)
    conn.commit()
    cur.execute(query3) #You cannot commit procedures, not a CRUD operation
    #conn.commit()
    conn.close()
    return
    
def checkConnected(source,target,length):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    inputs = (source,target,length)
    query = '''
        DROP PROCEDURE IF EXISTS checkConnected;
        DELIMITER $$
        CREATE PROCEDURE checkConnected(IN source INT, IN target INT, IN length INT, OUT connected CHAR(20))
        BEGIN
            declare len_count INT;
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
                SET connected = 'True';
            ELSE
                SET connected = 'False';
            END IF;
        END $$
        DELIMITER ;
        CALL checkConnected(%s, %s, %s, @connected);
        SELECT @connected;
    '''
    connected = cur.execute(query, inputs)
    conn.close()
    return connected

    