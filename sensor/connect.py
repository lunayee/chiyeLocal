import sensor
import time
import datetime
import DBmysql



def getaDate():
    str_now = str_time()
    INITIAL = getInitial()
    DATA = sensor.Sensor()

    DATA['Time'] = str_now
    DATA['Proj_ID'] = INITIAL[1]
    DATA['STID'] = INITIAL[2]


    AF_DATA = {}
    i = 0
    # Value1-7校正後 Value14-20校正前
    comparison = {'Value1': ['Value14','S1'], 'Value2': ['Value15','S2'], 'Value3': ['Value16','S3'],
                  'Value4': ['Value17','S4'], 'Value5': ['Value18','S5'], 'Value6': ['Value19','S6'], 'Value7': ['Value20','S7']}

    for af, be in comparison.items():
        i = i+1
        search = DBmysql.read_mysql(
            "REVISE", ("select * from RE_VALUE where `Va_Name` = '{}' ;").format(af))[0]  # 抓取a b offset
        cal = float(DATA[be[0]])*search[6]+search[7]+search[8]
        AF_DATA[af] = cal

    DATA.update(AF_DATA)  # 將計算後的合併成一個

    return DATA


def getInitial():
    INITIAL = DBmysql.read_mysql("REVISE", "select * from INITIAL;")[0]
    return INITIAL


def str_time():
    now = datetime.datetime.now()
    str_now = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    return str_now


def T001():
    # Value1-6校正後的值 Value14-19校正前的值
    DATA = getaDate()
    DBmysql.write_mysql("SENSOR","SENSOR_DB",DATA) 
    return DATA


def T01():
    str_now = str_time()
    INITIAL = getInitial()
    DATA = {
        'Time': str_now,
        'Proj_ID': INITIAL[1],
        'STID': INITIAL[2],
        'Value1': 0,  # 校正後
        'Value2': 0,
        'Value3': 0,
        'Value4': 0,
        'Value5': 0,
        'Value6': 0,
        'Value7': 0,
        'Value14': 2,  # 校正前
        'Value15': 2,
        'Value16': 2,
        'Value17': 2,
        'Value18': 2,
        'Value19': 2,
        'Value20': 2,
    }
    DBmysql.write_mysql("SENSOR","T01",DATA) 


def T05():
    str_now = str_time()
    INITIAL = getInitial()
    DATA = {
        'Time': str_now,
        'Proj_ID': INITIAL[1],
        'STID': INITIAL[2],
        'Value1': 5,
        'Value2': 2,
        'Value3': 2,
        'Value4': 2,
        'Value5': 2,
        'Value6': 2,
        'Value7': 2,
        'Value14': 2,
        'Value15': 2,
        'Value16': 2,
        'Value17': 2,
        'Value18': 2,
        'Value19': 2,
        'Value20': 2,
    }
    DBmysql.write_mysql("SENSOR","T05",DATA) 


def T60():
    str_now = str_time()
    INITIAL = getInitial()
    DATA = {
        'Time': str_now,
        'Proj_ID': INITIAL[1],
        'STID': INITIAL[2],
        'Value1': 60,
        'Value2': 2,
        'Value3': 2,
        'Value4': 2,
        'Value5': 2,
        'Value6': 2,
        'Value7': 2,
        'Value14': 2,
        'Value15': 2,
        'Value16': 2,
        'Value17': 2,
        'Value18': 2,
        'Value19': 2,
        'Value20': 2,
    }
    DBmysql.write_mysql("SENSOR","T60",DATA) 


T05()
'''
while(1):
    T001()
    time.sleep(5)
'''
