import socket
import time
import MySQLdb
from datetime import date
import datetime
import DBmysql
import requests

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


def connected():
    i = 0
    while i != 1:
        try:
            i = 1
            initial = getinitial()
            IP = initial[0][6]
            PORT = initial[0][7]
            ADDR = (IP, int(PORT))
            client.connect(ADDR)  # 用來請求連接遠程服務器
            print("[successful connected]")
            return True

        except:
            print("[!cannot connect server or no wifi]")
            i = 0
            time.sleep(5)


def getinitial():
    initial = DBmysql.read_mysql("REVISE", "select * from `INITIAL`")
    return initial


def getData(DATABASE,TABLE):  # getData('SENSOR','SENSOR_DB')
    data = {}
    value = DBmysql.read_mysql(
        DATABASE, ("SELECT * FROM `{}` ORDER BY `ID` DESC LIMIT 0,1 ").format(TABLE))[0]
    column_name = DBmysql.read_mysql_column_name(
        DATABASE, ("SELECT * FROM `{}` ORDER BY `ID` DESC LIMIT 0,1 ").format(TABLE))
    for index, item in enumerate(column_name):
        data[item] = value[index]
    data['Time'] = str(data['Time'])
    return data


def send(msg):
    try:
        initial = getinitial()
        IP = initial[0][6]
        PORT = initial[0][7]
        ADDR = (IP, int(PORT))
        client.sendto(msg.encode('utf-8'), ADDR)
    except:
        print("[!send fail!] retest after 5seconds")
        time.sleep(5)


def goEPA(DATABASE,TABLE):
    try:
        all_data = getData(DATABASE,TABLE)
        all_data['TABLE'] = TABLE
        all_data['DATABASE'] = DATABASE
        send(str(all_data))
        print(TABLE, all_data['Time'])
    except:
        print("retest mysocket after 30seconds")
        time.sleep(30)

def sendany(all_data):
    send(str(all_data))
    print(all_data)


# AF_INET:默認IPv4, SOCK_STREAM:UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

judge_T001 = time_judge()
judge_T01 = time_judge()
judge_T05 = time_judge()
judge_T60 = time_judge()

if connected() == True:
    while(1):
        now = datetime.datetime.now()
        timstamps = int(now.timestamp())
        if judge_T001.range_second(timstamps, 2):
            goEPA("SENSOR","SENSOR_DB")
        if judge_T01.range_second(timstamps, 60):
            goEPA("SENSOR","T01")
        if judge_T05.range_second(timstamps, 300):
            goEPA("SENSOR","T05")
        if judge_T60.range_second(timstamps, 3600):
            goEPA("SENSOR","T60")
