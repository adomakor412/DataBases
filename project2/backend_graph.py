import mysql.connector


def initiateTable(source,target):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    query = f'''
        CREATE TABLE DirectedEdges(f{source} INT, f{target} INT, PRIMARY KEY (f{source}, f{target}));

        LOAD DATA LOCAL INFILE 'question1/graph.csv'
        INTO TABLE DirectedEdges
        FIELDS TERMINATED BY ','
        ENCLOSED BY '"'
        LINES TERMINATED BY '\n'
        GNORE 1 ROWS;
        '''
    cur.execute(query)
    conn.commit()
    conn.close()
    return
    
def checkConnected(source,target,length):
    conn = mysql.connector.connect(database="mydb", user ="root", password = "password", host="localhost")
    cur = conn.cursor()
    query = f'''
        DROP PROCEDURE IF EXISTS checkConnected;
        DELIMITER $$
        CREATE PROCEDURE checkConnected(IN {source} INT, IN {target} INT, IN {length} INT, OUT connected CHAR(20))
        BEGIN
            declare len_count INT;
            SELECT COUNT(*)
            FROM
            (SELECT *
            FROM DirectedEdges 
            WHERE DirectedEdges.{source} between {source} and {target}
            and directededges.{target} = {target} 
            LIMIT {length}) as A
            INTO len_count;
            IF len_count - 1 < length and len_count > 0
            THEN
                SET connected = 'True';
            ELSE
                SET connected = 'False';
            END IF;
        END $$
        DELIMITER ;
        CALL checkConnected(3, 12, 3, @connected);
        SELECT @connected;
    '''
    connected = cur.execute(query)
    conn.close()
    return connected

    