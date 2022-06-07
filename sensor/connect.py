import sys
sys.path.append(".\\apps\\home")
import DBmysql
import sensor 
import datetime
import time




def getaDate():
    DATA = sensor.Sensor()
    AF_DATA = {}
    i=13
    for key in DATA.keys():
        i = i+1
        search=DBmysql.read_mysql_test("REVISE",("select * from RE_VALUE where `Va_Name` = '{}' ;").format(key))[0]
        cal= float(DATA[key])*search[6]+search[7]+search[8]
        AF_DATA["Value{}".format(i)]=cal
    DATA.update(AF_DATA) #將計算後的合併成一個
    return DATA

def getInitial():
    INITIAL=DBmysql.read_mysql_test("REVISE","select * from INITIAL;")[0]
    return INITIAL

def str_time():
    now = datetime.datetime.now()
    str_now = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    return str_now

def T001():
    str_now = str_time()
    INITIAL = getInitial()
    DATA = getaDate()
    DATA['Time'] =  str_now
    DATA['Proj_ID'] = INITIAL[1]
    DATA['STID'] = INITIAL[2]
    print(DATA)
    sqlReal = ("INSERT INTO `SENSOR_DB`(`Time`,`Proj_ID`,`STID`,`Value1`,`Value2`,`Value3`,`Value4`,`Value5`,`Value6`,`Value14`,`Value15`,`Value16`,`Value17`,`Value18`,`Value19`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')").format(DATA['Time'],DATA['Proj_ID'],DATA['STID'],DATA['Value1'],DATA['Value2'],DATA['Value3'],DATA['Value4'],DATA['Value5'],DATA['Value6'],DATA['Value14'],DATA['Value15'],DATA['Value16'],DATA['Value17'],DATA['Value18'],DATA['Value19'])
    DBmysql.write_mysql_test("SENSOR",sqlReal)

def T01():
    str_now = str_time()
    INITIAL = getInitial()
    DATA ={
        'Time':str_now,
        'Proj_ID':INITIAL[1],
        'STID':INITIAL[2],
        'Value1':2,
        'Value2':2,
        'Value3':2,
        'Value4':2,
        'Value5':2,
        'Value6':2,
        'Value14':2,
        'Value15':2,
        'Value16':2,
        'Value17':2,
        'Value18':2,
        'Value19':2,
    }
    sqlReal = ("INSERT INTO `T01`(`Time`,`Proj_ID`,`STID`,`Value1`,`Value2`,`Value3`,`Value4`,`Value5`,`Value6`,`Value14`,`Value15`,`Value16`,`Value17`,`Value18`,`Value19`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')").format(DATA['Time'],DATA['Proj_ID'],DATA['STID'],DATA['Value1'],DATA['Value2'],DATA['Value3'],DATA['Value4'],DATA['Value5'],DATA['Value6'],DATA['Value14'],DATA['Value15'],DATA['Value16'],DATA['Value17'],DATA['Value18'],DATA['Value19'])
    DBmysql.write_mysql_test("SENSOR",sqlReal)

def T05():
    str_now = str_time()
    INITIAL = getInitial()
    DATA ={
        'Time':str_now,
        'Proj_ID':INITIAL[1],
        'STID':INITIAL[2],
        'Value1':5,
        'Value2':2,
        'Value3':2,
        'Value4':2,
        'Value5':2,
        'Value6':2,
        'Value14':2,
        'Value15':2,
        'Value16':2,
        'Value17':2,
        'Value18':2,
        'Value19':2,
    }
    sqlReal = ("INSERT INTO `T05`(`Time`,`Proj_ID`,`STID`,`Value1`,`Value2`,`Value3`,`Value4`,`Value5`,`Value6`,`Value14`,`Value15`,`Value16`,`Value17`,`Value18`,`Value19`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')").format(DATA['Time'],DATA['Proj_ID'],DATA['STID'],DATA['Value1'],DATA['Value2'],DATA['Value3'],DATA['Value4'],DATA['Value5'],DATA['Value6'],DATA['Value14'],DATA['Value15'],DATA['Value16'],DATA['Value17'],DATA['Value18'],DATA['Value19'])
    DBmysql.write_mysql_test("SENSOR",sqlReal)

def T60():
    str_now = str_time()
    INITIAL = getInitial()
    DATA ={
        'Time':str_now,
        'Proj_ID':INITIAL[1],
        'STID':INITIAL[2],
        'Value1':60,
        'Value2':2,
        'Value3':2,
        'Value4':2,
        'Value5':2,
        'Value6':2,
        'Value14':2,
        'Value15':2,
        'Value16':2,
        'Value17':2,
        'Value18':2,
        'Value19':2,
    }
    sqlReal = ("INSERT INTO `T60`(`Time`,`Proj_ID`,`STID`,`Value1`,`Value2`,`Value3`,`Value4`,`Value5`,`Value6`,`Value14`,`Value15`,`Value16`,`Value17`,`Value18`,`Value19`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')").format(DATA['Time'],DATA['Proj_ID'],DATA['STID'],DATA['Value1'],DATA['Value2'],DATA['Value3'],DATA['Value4'],DATA['Value5'],DATA['Value6'],DATA['Value14'],DATA['Value15'],DATA['Value16'],DATA['Value17'],DATA['Value18'],DATA['Value19'])
    DBmysql.write_mysql_test("SENSOR",sqlReal)

now = datetime.datetime.now()
s = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')

while(1):
    T001()
    time.sleep(30)

