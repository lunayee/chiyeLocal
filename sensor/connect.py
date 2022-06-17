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

    return DATA


def getInitial():
    INITIAL = DBmysql.read_mysql("REVISE", "select * from INITIAL;")[0]
    return INITIAL


def cal_N(Noise):  # 第1個數字-Value1
    data = []
    for i in range(len(Noise)):
        cal = 10**(0.1*Noise[i][0])
        data.append(cal)
    cal = 10*math.log(sum(data)*(1/len(Noise)), 10)
    return cal


def All_mean(ago, aft):
    DATA = {}
    INITIAL = getInitial()
    range_data = DBmysql.read_mysql(
        "SENSOR", ("select Value1,Value2,Value3,Value4,Value5,Value6,Value7 from SENSOR_DB where Time >= '{}' and Time < '{}';").format(ago, aft))
    DATA['Proj_ID'] = INITIAL[1]
    DATA['STID'] = INITIAL[2]
    DATA['Value1'] = cal_N(range_data)
    DATA['Value2'] = 3
    DATA['Value3'] = 3
    DATA['Value4'] = 3
    DATA['Value5'] = 3
    DATA['Value6'] = 3
    DATA['Value7'] = 3
    return DATA


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

while(1):
    now = datetime.datetime.now()
    timstamps = int(now.timestamp())
    if judge_T001.range_second(timstamps, 2):
        DATA = getaDate()
        DBmysql.write_mysql("SENSOR", "SENSOR_DB", DATA)
    if judge_T01.range_second(timstamps, 60):
        ago = judge_T01.cal_time(now, -60, '%Y-%m-%d %H:%M:00')
        aft = judge_T01.cal_time(now, 0, '%Y-%m-%d %H:%M:00')
        DATA = All_mean(ago, aft)
        DATA['Time'] = ago
        print(DATA)
        DBmysql.write_mysql("SENSOR", "T01", DATA)
        print("T01", ago, aft)
    if judge_T05.range_second(timstamps, 300):
        ago = judge_T01.cal_time(now, -300, '%Y-%m-%d %H:%M:00')
        aft = judge_T01.cal_time(now, 0, '%Y-%m-%d %H:%M:00')
        DATA = All_mean(ago, aft)
        DATA['Time'] = ago
        DBmysql.write_mysql("SENSOR", "T05", DATA)
        print("T05", ago, aft)
    if judge_T60.range_second(timstamps, 3600):
        ago = judge_T01.cal_time(now, -3600, '%Y-%m-%d %H:00:00')
        aft = judge_T01.cal_time(now, 0, '%Y-%m-%d %H:00:00')
        DATA = All_mean(ago, aft)
        DATA['Time'] = ago
        DBmysql.write_mysql("SENSOR", "T60", DATA)
        print("T60", ago, aft)

'''
print(getaDate())
   '''
