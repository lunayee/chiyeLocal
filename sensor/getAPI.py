import requests
import datetime
import DBmysql
import json

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

    def realtime(self):
        while(1):
            now=datetime.datetime.now()
            if now.second == 0:
                return True

def getData(DATABASE,TABLE):  # getData('SENSOR','SENSOR_DB')
    data = {}
    value = DBmysql.read_mysql(
        DATABASE, ("SELECT * FROM `{}` ORDER BY `ID` DESC LIMIT 0,1 ").format(TABLE))[0]
    column_name = DBmysql.read_mysql_column_name(
        DATABASE, ("SELECT * FROM `{}` ORDER BY `ID` DESC LIMIT 0,1 ").format(TABLE))
    for index, item in enumerate(column_name):
        data[item] = value[index]
    data['Time'] = str(data['Time'])
    data['TABLE'] = TABLE
    data['DATABASE'] = DATABASE
    return data

def goEPA(DATABASE,TABLE): #goEPA("SENSOR","T01")
    context = getData(DATABASE,TABLE)
    goEpaContext=json.dumps(context, indent=4, default=str)
    url = "http://192.168.3.107:8000/"
    requests.post(url+'SaveLoaclValue/', json=goEpaContext)

judge_T001 = time_judge()
judge_T01 = time_judge()
judge_T05 = time_judge()
judge_T60 = time_judge()

if judge_T001.realtime() ==  True:
    while(1):
        now = datetime.datetime.now()
        timstamps = int(now.timestamp())
        if judge_T001.range_second(timstamps, 3):
            goEPA("SENSOR","SENSOR_DB")
        if judge_T01.range_second(timstamps, 63):     
            goEPA("SENSOR","T01")
            print("GOEPA-T01",now)
        if judge_T05.range_second(timstamps, 303):
            goEPA("SENSOR","T05")
            print("GOEPA-T05",now)
        if judge_T60.range_second(timstamps, 3603):
            goEPA("SENSOR","T60")
            print("GOEPA-T60",now)