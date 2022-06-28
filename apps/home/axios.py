from importlib.resources import contents
from django.shortcuts import redirect, render
from django.http import JsonResponse
import json
from . import DBmysql
import datetime
import math
import json
import socket
import time
import datetime
import requests

URL = "http://192.168.3.107:8000/"
#POST
def Inpsetting(request):
    if request.method == "POST":
        data =json.loads(request.body)
        if data['area']=="無":
            data['ip']=0
            data['port']=0
        if data['area']=="1":
            data['ip']='125.227.111.239'
            data['port']=3333
        SQL = ("UPDATE `INITIAL` SET `Proj_ID`='{}',`STID`='{}',`Address`='{}',`Lng`='{}',`Lat`='{}',`IP`='{}',`PORT`='{}' where `ID`=2").format(data['pjid'],data['stid'],data['address'],data['Lng'],data['Lat'],data['ip'],data['port'])
        DBmysql.update_mysql("REVISE",SQL)
        return JsonResponse(data)

def connect_server(request):
    if request.method == "POST":
        data =json.loads(request.body)
        ## i don't know how to check this problem
        print(data)
        return JsonResponse(data)

def SaveRevise(request):
    if request.method == "POST":
        data =json.loads(request.body)
        Label=DBmysql.read_mysql("REVISE","select `Label`,`NAME` from `LABEL` where `IsShow`='True'")
        for la in Label:
            if data['Item'] in la:
                data['Item']=la[0]
        x1=int(data['Value_zero'])
        x2=int(data['Value_span'])
        y1=int(data['Count_zero'])
        y2=int(data['Count_span'])
        data['a']=(x2-x1)/(y2-y1)
        data['b']=x1-(y1*data['a'])
        data['Offset']=int(data['Offset']) if data['Offset'] != "" else 0
        DBmysql.update_mysql("REVISE",("UPDATE `RE_VALUE` SET `Value_zero`='{}',`Value_span`='{}',`Count_zero`='{}',`Count_span`='{}',`a`='{}',`b`='{}',`offset`='{}' where `Va_Name`='{}'").format(data['Value_zero'],data['Value_span'],data['Count_zero'],data['Count_span'],data['a'],data['b'],data['Offset'],data['Item']))
        
        return JsonResponse(data)

def SaveTable(request):
    if request.method == "POST":
        data =json.loads(request.body)
        
        x1=int(data['Value_zero'])
        x2=int(data['Value_span'])
        y1=int(data['Count_zero'])
        y2=int(data['Count_span'])
        data['a']=(x2-x1)/(y2-y1)
        data['b']=x1-(y1*data['a'])
        data['Offset']=int(data['Offset']) if data['Offset'] != "" else 0
        DBmysql.update_mysql("REVISE",("UPDATE `ST_VALUE` SET `Value_zero`='{}',`Value_span`='{}',`Count_zero`='{}',`Count_span`='{}',`a`='{}',`b`='{}',`offset`='{}' where `Va_Name`='{}'").format(data['Value_zero'],data['Value_span'],data['Count_zero'],data['Count_span'],data['a'],data['b'],data['Offset'],data['Item']))
        return JsonResponse(data)

def item_check(request):
    if request.method == "POST":
        data =json.loads(request.body)['checkbox']
        print(data)
        for i in data:
            CheckData = [i.split('_')[0],data[i][1],data[i][0]]
            DBmysql.update_mysql("REVISE",("UPDATE `LABEL` SET `Name`='{}',`IsShow`='{}' where `Label`='{}' ").format(CheckData[1],CheckData[2],CheckData[0]))
        return JsonResponse(data)

def table1_0(request):
    if request.method == "POST":
        data =json.loads(request.body)
        print(data['Item'])
        DATA={"Date_Time":"2022-01-13 12:00:00","Item":"TVOC","Value1_be":"12121","Value1_af":"5263","a":"0.5555","b":"0.6666","offset":"0.7777"}
        context=DATA
        return JsonResponse(DATA)

def SaveHistory(request):
    if request.method == "POST":
        data =json.loads(request.body)
        StartTime=data['StartTime']
        EndTime=data['EndTime']
        Time=data['Time'] #T01 05 60
        obj_SwitchCheck=data['obj_SwitchCheck'] #複選格
         
        show_item=[] #複選格有選到的測項
        for i,j in obj_SwitchCheck.items():
            if j == True:
                show_item.append(i)
        print(data)
        return JsonResponse(data)


#show
def showHistory(request):
    ##show checkbox
    IsShow=DBmysql.read_mysql("REVISE","select `Label`,`NAME` from `LABEL` where `IsShow`='True'")
    Item=IsShow##全部項目
    context={"Item":Item}

    return render(request,'home/history.html',context)


def showDashboard(request):
    IsShow=DBmysql.read_mysql("REVISE","select `Label`,`NAME` from `LABEL` where `IsShow`='True'")
    IsShow=[i[0] for i in IsShow]
    print(IsShow)
    context={"Data":IsShow}
    
    return render(request,'home/DashBoard.html',context) 



def showSetting(request):
    Initial=DBmysql.read_mysql("REVISE","select * from `INITIAL`")
    print(Initial)
    context={"ProjID":Initial[0][1],"STID":Initial[0][2],"Address":Initial[0][3],"Lng":Initial[0][4],"Lat":Initial[0][5],"Area":"捷思伺服器","IP":Initial[0][6],"PORT":Initial[0][7]}
    return render(request,'home/settings.html',context)



def showRevise(request):
    Label=DBmysql.read_mysql("REVISE","select `Name` from `LABEL`") 
    LabelName={}
    for i in range(0,len(Label),1):
        LabelName[("Value{}").format(i+1)] = Label[i][0]
    print(LabelName)
    context={"Data":LabelName}
    return render(request,'home/page-revise.html',context)

#GET    
def GetDashboard(request):
    
    Data=[]
    GetData=DBmysql.read_mysql("SENSOR","select * from `SENSOR_DB` ORDER BY `ID` DESC LIMIT 0,1")[0]
    Re_Value=DBmysql.read_mysql("REVISE","select * from `RE_VALUE`,`LABEL` where `Va_Name` = `Label`") 
    number = int((len(GetData)-4)/2) #有多少測值
    
    isshowid=[]
    
    for i in Re_Value:
        if i[12] == 'True' :
            isshowid.append(i[0]-1)
    
    for i in isshowid: #[0,1, 2, 3, 4, 5, 6]
        Data.append({"Date_Time":GetData[1],"ProjID":str(GetData[2]),"STID":str(GetData[3]),"Item":str(Re_Value[i][11]),"Value_be":str(round(GetData[i+4+number],2)),"Value_af":str(round(GetData[i+4],2)),"a":str(round(Re_Value[i][6],3)),"b":str(round(Re_Value[i][7],3)),"offset":str(Re_Value[i][8]),"isshow":Re_Value[i][12]})
        
    
    context={"Data":Data}

    return JsonResponse(context)


def getHistory(request):
    if request.method == "GET":
        #data=json.loads(request.body)
        StartTime=request.GET['st']
        EndTime=request.GET['et']
        Table=request.GET['table']
        Page=int(request.GET['page'])
        Count=int(request.GET['count'])
        SwitchCheck_all=eval(request.GET['SwitchCheck_all'])     
        
        print(SwitchCheck_all)        
        check=[]
        checkname=[]
        
        for i,j in SwitchCheck_all.items():
            if j[1]=='true':
                check.append(i)
                checkname.append(j[0])
        str_check="`,`".join(check)
        
        GetData=DBmysql.read_mysql("SENSOR",("select `Time`,`{}` from `{}` WHERE `Time` >= '{}' and `Time` < '{}'").format(str_check,Table,StartTime,EndTime))
        #print(GetData)
        total = len(GetData)
        DATA=[]
        for i in range(total):
            dic_data={}
            Time=datetime.datetime.strftime(GetData[i][0],'%Y-%m-%d %H:%M:%S')
            dic_data["Date_Time"]=Time
            for num in range(len(check)):
                dic_data[check[num]]=GetData[i][num+1]
                
            DATA.append(dic_data)
            
        DATA = DATA[Count*(Page-1):Count*Page]
        totalPage=math.ceil(total / Count)
    
    return JsonResponse({'list':DATA,'total':total,'page':Page,'count':Count,'totalPage':totalPage,'check':[check,checkname]})



def GetLngLat(request):
    Re_Value=DBmysql.read_mysql("REVISE","select * from `INITIAL`") 
    corrd = {'lat': float(Re_Value[0][4]), 'lng': float(Re_Value[0][5])}
    context = corrd
    return JsonResponse(context)

def GetTable(request):
    if request.method == "GET":
        Item=request.GET['Item']
        ALL_ITEM=DBmysql.read_mysql("SENSOR",("select * from `SENSOR_DB` ORDER BY `ID` DESC LIMIT 0,1"))[0]
        number = int((len(ALL_ITEM)-4)/2)#判斷校正後的值在哪一欄位
        
        
        y=Item.split("Value")
        change_Item = "Value"+str(int(y[1])+number)
        #Item = "Value1"
        Value_be=DBmysql.read_mysql("SENSOR",("select `{}` from `SENSOR_DB` ORDER BY `ID` DESC LIMIT 0,1").format(change_Item))[0]
        
        ST_VALUE=DBmysql.read_mysql("REVISE",("select `a`,`b`,`offset` from `ST_VALUE` WHERE `Va_Name` = '{}' ").format(Item))[0]
        a=ST_VALUE[0]
        b=ST_VALUE[1]
        offset=ST_VALUE[2]
        calValue_af=Value_be[0]*a+b+offset
        
        context={"Value_be":Value_be[0],"calValue_af":calValue_af,"a":a,"b":b,"offset":offset}
    return JsonResponse(context)
    
def GetExport(request):
    if request.method == "GET":
        StartTime=request.GET['st']
        EndTime=request.GET['et']
        Table=request.GET['table']
        SwitchCheck_all=eval(request.GET['SwitchCheck_all']) 
        check=[]
        checkname=[]
        
        for i,j in SwitchCheck_all.items():
            if j[1]=='true':
                check.append(i)
                checkname.append(j[0])
        str_check="`,`".join(check)
        
        GetData=DBmysql.read_mysql("SENSOR",("select `Time`,`{}` from `{}` WHERE `Time` >= '{}' and `Time` < '{}'").format(str_check,Table,StartTime,EndTime))
        total = len(GetData)
        DATA=[]
        for i in range(total):
            dic_data={}
            Time=datetime.datetime.strftime(GetData[i][0],'%Y-%m-%d %H:%M:%S')
            dic_data["Date_Time"]=Time
            for num in range(len(check)):
                dic_data[check[num]]=GetData[i][num+1]
                
            DATA.append(dic_data)
        export_json(('/home/pi/High-Precision-AD-DA-Board-Code/RaspberryPI/ADS1256/python3/log/{} - {}').format(StartTime,EndTime),DATA)
    return JsonResponse({"Data":DATA})

def export_json(filename,json_data):
    with open(filename,'w') as f:
        json.dump(json_data,f)
        f.close()



def recover(request):#SaveBackup
    if request.method == "GET":
        StartTime=request.GET['st']
        EndTime=request.GET['et']
        Table=request.GET['table']
        GetData=DBmysql.read_mysql("SENSOR",("select * from `{}` WHERE `Time` >= '{}' and `Time` < '{}'").format(Table,StartTime,EndTime))
        column_name = DBmysql.read_mysql_column_name("SENSOR", ("SELECT * FROM `{}` ORDER BY `ID` DESC LIMIT 0,1 ").format(Table))

        context = {'DATABASE':'SENSOR','TABLE':Table,'column_name':column_name,'value':GetData}
        goEpaContext=json.dumps(context, indent=4, sort_keys=True, default=str)
        url = URL
        requests.post(url+'SaveBackup/', json=goEpaContext)

        
    return JsonResponse(context)