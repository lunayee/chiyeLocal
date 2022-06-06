import socket
import time
import MySQLdb
from datetime import date
import datetime
import RaspDB


def connected():
    i=0
    while i!=1:
        try:
            i=1
            initial = getinitial()
            IP=initial[0][6]
            PORT=initial[0][7]
            ADDR = (IP, int(PORT))
            client.connect(ADDR)# 用來請求連接遠程服務器
            print("[successful connected]")
            return True
            
        except:
            print("[!cannot connect server or no wifi]")
            i=0
            time.sleep(5)
          
def realtime():
    while(1):
        now=datetime.datetime.now()
        time.sleep(1)
        if now.second == 0:
            return True
            
        
def getinitial():
    initial=RaspDB.read_mysql("REVISE","select * from `INITIAL`")
    return initial

def T01_socket():
    data={}
    Items=["Value{}".format(i) for i in range(1,27,1)]
    T01_value=RaspDB.read_mysql("SENSOR","SELECT * FROM `T01` ORDER BY `ID` DESC LIMIT 0,1 ")
    data['Time']=T01_value[0][1].strftime("%Y-%m-%d %H:%M:%S")
    data['ProjID']=T01_value[0][2]
    data['STID']=T01_value[0][3]
    for index,item in enumerate(Items):
        data[item]=T01_value[0][index+4]
    return data

def send(msg):
    try:
        initial = getinitial()
        IP=initial[0][6]
        PORT=initial[0][7]
        ADDR = (IP, int(PORT))
        client.sendto(msg.encode(FORMAT),ADDR)
    except:
        print("[!send fail!] retest after 5seconds")
        time.sleep(5)

def reboot():
    for i in range(5):
        all_data = T01_socket()
        Statuses=["Status{}".format(i) for i in range(1,27,1)]
        for Status in Statuses :
            all_data[Status]="p"
        send(str(all_data))
        print(all_data['Time'],"p")
        time.sleep(60)
        

def no_reboot():
    try:
        all_data = T01_socket()
        Statuses=["Status{}".format(i) for i in range(1,27,1)]
        for Status in Statuses :
            all_data[Status]=None
        send(str(all_data))
        print(all_data['Time'])
        time.sleep(60)
    except:
        print("retest mysocket after 60seconds")
        time.sleep(60)
        no_reboot()

def finished():        
    if connected()== True :
        reboot()
        while(1):
            no_reboot()
            

FORMAT = 'utf-8'


DISCONNECT_MESSAGE = "!DISCONNECT"
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # AF_INET:默認IPv4, SOCK_STREAM:UDP
'''
print("[!run mysocket!]")
if realtime() == True:
    finished()
'''       
reboot()
    

