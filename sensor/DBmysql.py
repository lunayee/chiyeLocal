import MySQLdb
import datetime


def connected_mysql(DBNAME):##connected_mysql("SENSOR")
    
    #db_database = MySQLdb.connect(host="172.20.0.3",user ="root",passwd="123456789",db = DBNAME,charset='utf8')
    db_database = MySQLdb.connect(host="127.0.0.1",user ="root",passwd="123456789",db = DBNAME,charset='utf8')
    c_database = db_database.cursor()
    return db_database,c_database

def read_mysql(DBNAME,SQL):##read_mysql("SENSOR","select * from `T01`")
    db,c=connected_mysql(DBNAME)
    c.execute(SQL)
    return c.fetchall()

def read_mysql_column_name(DBNAME,SQL):##read_mysql("SENSOR","select * from `T01`")
    db,c=connected_mysql(DBNAME)
    c.execute(SQL)
    column_name = [i[0] for i in c.description]
    return column_name


def write_mysql(DBNAME,TABLE,DICT):##write_mysql("SENSOR","T01",DICT)
    now = datetime.datetime.now()
    METHOD = "INSERT INTO"
    SQL = produce_sql(METHOD,TABLE,DICT)
    db,c = connected_mysql(DBNAME)
    c.execute(SQL,DICT.values())
    db.commit()
    return SQL
    
def update_mysql(DBNAME,SQL):##update_mysql("REVISE","UPDATE `LABEL` SET `Name`=99 where `ID`=10 ")
    now = datetime.datetime.now()
    db,c = connected_mysql(DBNAME) 
    c.execute(SQL)
    db.commit()
    return now

def produce_sql(METHOD,TABLE,DICT): #produce_sql("INSERT INTO","SENSOR_DB",x)
    placeholders = ', '.join(['%s'] * len(DICT))
    columns = ', '.join(DICT.keys())
    sql = "%s %s ( %s ) VALUES ( %s )" % (METHOD,TABLE, columns, placeholders)
    return sql

if __name__=='__main__':
    print(connected_mysql("SENSOR"))