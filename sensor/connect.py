import sensor
import time
import datetime
import DBmysql
import math


def getaDate():
    # Value1-6校正後的值 Value14-19校正前的值
    DATA = sensor.Sensor()
    AF_DATA = {}
    # Value1-7校正後 Value14-20校正前
    comparison = {'Value1': 'Value14', 'Value2': 'Value15', 'Value3': 'Value16',
                  'Value4': 'Value17', 'Value5': 'Value18', 'Value6': 'Value19', 'Value7': 'Value20'}

    for af, be in comparison.items():
        search = DBmysql.read_mysql(
            "REVISE", ("select * from RE_VALUE where `Va_Name` = '{}' ;").format(af))[0]  # 抓取a b offset
        cal = float(DATA[be])*search[6]+search[7]+search[8]
        AF_DATA[af] = cal
        
    
    DATA.update(AF_DATA)  # 將計算後的合併成一個
    INITIAL = getInitial()
    DATA['Proj_ID'] = INITIAL[1]
    DATA['STID'] = INITIAL[2]

    return DATA


def getInitial():
    INITIAL = DBmysql.read_mysql("REVISE", "select * from INITIAL;")[0]
    return INITIAL


def cal_N(Val):  # 第1個數字-Value1
    data = []
    if len(Val) == 0:
        cal = 0
        return cal
    for i in range(len(Val)):
        cal = 10**(0.1*Val[i][0]) #Value1
        data.append(cal)
    final = 10*math.log(sum(data)*(1/len(Val)), 10)
    return final


#print(cal_rain([[0,0,0,0,0,5,0],[0,0,0,0,0,9,0]]))

def cal_tmp(Val):#cal_tmp([[0,0,0,28.1,0,0,0]])
    data = []
    if len(Val) == 0:
        cal = 0
        return cal
    for i in range(len(Val)):
        data.append(Val[i][3]) #Value4
    final = sum(data)/len(data)
    return final

def cal_hum(Val):#cal_hum([[0,0,0,0,61.8,0,0]])
    data = []
    if len(Val) == 0:
        cal = 0
        return cal
    for i in range(len(Val)):
        data.append(Val[i][4]) #Value5
    final = sum(data)/len(data)
    return final

def cal_rain(Val):#cal_rain([[0,0,0,0,0,5,0]])
    data = []
    if len(Val) == 0:
        cal = 0
        return cal
    for i in range(len(Val)):
        data.append(Val[i][5]) #Value6
    final = max(data)
    return final

def cal_pre(Val):#cal_pre([[0,0,0,0,0,0,1013]])
    data = []
    if len(Val) == 0:
        cal = 0
        return cal
    for i in range(len(Val)):
        cal = (760*Val[i][6])/1013 #Value7
        data.append(cal)
    final = sum(data)/len(data)
    return final
  

def All_mean(ago, aft):
    DATA = {}
    INITIAL = getInitial()
    DATA['Proj_ID'] = INITIAL[1]
    DATA['STID'] = INITIAL[2]
    range_data = DBmysql.read_mysql( "SENSOR", ("select Value1,Value2,Value3,Value4,Value5,Value6,Value7 from SENSOR_DB where Time >= '{}' and Time < '{}';").format(ago, aft))
    DATA['Value1'] = cal_N(range_data)
    DATA['Value2'] = 3
    DATA['Value3'] = 3
    DATA['Value4'] = cal_tmp(range_data)
    DATA['Value5'] = cal_hum(range_data)
    DATA['Value6'] = cal_rain(range_data)
    DATA['Value7'] = cal_pre(range_data)
    return DATA

def realtime():
    while(1):
        now=datetime.datetime.now()
        if now.second == 0:
            return True

class time_judge:
    def __init__(self):
        self.second = None

    def range_second(self, timestamps, second):
        s = timestamps
        if self.second != s:
            if s % second == 0:
                self.second = s
                return True
        return False

    def cal_time(self, now, second, fmt):
        ago = now+datetime.timedelta(seconds=second)
        AGO = datetime.datetime.strftime(ago, fmt)
        return AGO


judge_T001 = time_judge()
judge_T01 = time_judge()
judge_T05 = time_judge()
judge_T60 = time_judge()

if realtime() ==  True:
    while(1):
        now = datetime.datetime.now()
        timstamps = int(now.timestamp())
        if judge_T001.range_second(timstamps, 3):
            aft = judge_T001.cal_time(now, 0, '%Y-%m-%d %H:%M:%S')
            DATA = getaDate()
            DATA['Time'] = aft
            DBmysql.write_mysql("SENSOR", "SENSOR_DB", DATA)
        if judge_T01.range_second(timstamps, 60):
            ago = judge_T01.cal_time(now, -60, '%Y-%m-%d %H:%M:00')
            aft = judge_T01.cal_time(now, 0, '%Y-%m-%d %H:%M:00')
            DATA = All_mean(ago, aft)
            DATA['Time'] = ago
            #print(DATA)
            DBmysql.write_mysql("SENSOR", "T01", DATA)
            print("LOCAL-T01", ago)
        if judge_T05.range_second(timstamps, 300):
            ago = judge_T05.cal_time(now, -300, '%Y-%m-%d %H:%M:00')
            aft = judge_T05.cal_time(now, 0, '%Y-%m-%d %H:%M:00')
            DATA = All_mean(ago, aft)
            DATA['Time'] = ago
            DBmysql.write_mysql("SENSOR", "T05", DATA)
            print("LOCAL-T05", ago)
        if judge_T60.range_second(timstamps, 3600):
            ago = judge_T60.cal_time(now, -3600, '%Y-%m-%d %H:00:00')
            aft = judge_T60.cal_time(now, 0, '%Y-%m-%d %H:00:00')
            DATA = All_mean(ago, aft)
            DATA['Time'] = ago
            DBmysql.write_mysql("SENSOR", "T60", DATA)
            print("LOCAL-T60", ago)