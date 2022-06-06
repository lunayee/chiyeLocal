import sys
sys.path.append(".\\apps\\home")
import DBmysql
import sensor 

#print(DBmysql.read_mysql("REVISE","select `Label`,`NAME` from `LABEL` where `IsShow`='True'"))
DATA = sensor.Sensor()
AF_DATA = {}
i=13
for key in DATA.keys():
    i = i+1
    search=DBmysql.read_mysql_test("REVISE",("select * from RE_VALUE where `Va_Name` = '{}' ;").format(key))[0]
    
    cal= float(DATA[key])*search[6]+search[7]+search[8]
    AF_DATA["Value{}".format(i)]=cal
DATA.update(AF_DATA) #將計算後的合併成一個

print(DATA)
sqlReal = ("INSERT INTO `SENSOR_DB`(`Time`,`Proj_ID`,`STID`,`Value1`,`Value2`,`Value3`,`Value4`,`Value5`,`Value6`,`Value14`,`Value15`,`Value16`,`Value17`,`Value18`,`Value19`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')").format("2022-07-06 12:00:00","S200230","T202120",DATA['Value1'],DATA['Value2'],DATA['Value3'],DATA['Value4'],DATA['Value5'],DATA['Value6'],DATA['Value14'],DATA['Value15'],DATA['Value16'],DATA['Value17'],DATA['Value18'],DATA['Value19'])

DBmysql.write_mysql_test("SENSOR",sqlReal)

