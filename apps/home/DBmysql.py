import MySQLdb
import datetime


def connected_mysql(DBNAME):##connected_mysql("SENSOR")
    
    db_database = MySQLdb.connect(host="172.19.0.2",user ="root",passwd="123456789",db = DBNAME,charset='utf8')
    c_database = db_database.cursor()
    return db_database,c_database
    

def read_mysql(DBNAME,SQL):##read_mysql("SENSOR","select * from `T01`")
    db,c=connected_mysql(DBNAME)
    c.execute(SQL)
    return c.fetchall()


def write_mysql(DBNAME,SQL):##write_mysql("REVISE","INSERT INTO `LABEL`(`Label`,`Name`) VALUES (%s,%s)")
    now = datetime.datetime.now()
    db,c = connected_mysql(DBNAME)
    c.execute(SQL)
    db.commit()
    return now
    
def update_mysql(DBNAME,SQL):##update_mysql("REVISE","UPDATE `LABEL` SET `Name`=99 where `ID`=10 ")
    now = datetime.datetime.now()
    db,c = connected_mysql(DBNAME) 
    c.execute(SQL)
    db.commit()
    return now

