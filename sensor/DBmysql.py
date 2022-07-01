import MySQLdb
import datetime
import csv

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
    placeholders = ', '.join(['%s'] * len(DICT))
    columns = ', '.join(DICT.keys())
    METHOD = "INSERT INTO"
    SQL = "%s %s ( %s ) VALUES ( %s )" % (METHOD,TABLE, columns, placeholders)
    db,c = connected_mysql(DBNAME)
    c.execute(SQL,DICT.values())
    db.commit()
    return SQL

def write_many_mysql(DBNAME,TABLE,column,list):#write_many_mysql("SENSOR","T01",["Value2","Value3"],[[3,3],[3,6],[9,9]])
    column = ",".join(column)
    placeholders = ', '.join(['%s'] * len(list[0]))
    SQL = "%s %s ( %s ) VALUES ( %s )" % ("INSERT INTO",TABLE, column, placeholders)
    db,c = connected_mysql(DBNAME)
    c.executemany(SQL, list )
    db.commit()    
    return c
    
def update_mysql(DBNAME,SQL):##update_mysql("REVISE","UPDATE `LABEL` SET `Name`=99 where `ID`=10 ")
    now = datetime.datetime.now()
    db,c = connected_mysql(DBNAME) 
    c.execute(SQL)
    db.commit()
    return now


if __name__=='__main__':
    StartTime = "2022-06-28"
    EndTime = "2022-06-29"
    range_data = read_mysql( "SENSOR", ("select Value1,Value2,Value3,Value4 from SENSOR_DB where Time >= '{}' and Time < '{}' limit 2,3 ;").format(StartTime, EndTime))
    print(range_data)
