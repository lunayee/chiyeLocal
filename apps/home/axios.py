from django.shortcuts import redirect, render
from django.http import JsonResponse
import json
from . import DBmysql
import datetime
import math
import json


#POST
def Inpsetting(request):
    if request.method == "POST":
        data =json.loads(request.body)
        if data['area']=="無":
            data['ip']=0
            data['port']=0
            DBmysql.update_mysql("REVISE",("UPDATE `INITIAL` SET `Proj_ID`='{}',`STID`='{}',`Address`='{}',`Lng`='{}',`Lat`='{}',`IP`='{}',`PORT`='{}' where `ID`=1").format(data['pjid'],data['stid'],data['address'],data['Lng'],data['Lat'],data['ip'],data['port']))
            print(data)
        if data['area']=="1":
            data['ip']='125.227.111.239'
            data['port']=3333
            DBmysql.update_mysql("REVISE",("UPDATE `INITIAL` SET `Proj_ID`='{}',`STID`='{}',`Address`='{}',`Lng`='{}',`Lat`='{}',`IP`='{}',`PORT`='{}' where `ID`=1").format(data['pjid'],data['stid'],data['address'],data['Lng'],data['Lat'],data['ip'],data['port']))
            print(data)
        if data['area']=="2":
            DBmysql.update_mysql("REVISE",("UPDATE `INITIAL` SET `Proj_ID`='{}',`STID`='{}',`Address`='{}',`Lng`='{}',`Lat`='{}',`IP`='{}',`PORT`='{}' where `ID`=1").format(data['pjid'],data['stid'],data['address'],data['Lng'],data['Lat'],data['ip'],data['port']))
            print(data)
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
        print(data)
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
        print(data)
        return JsonResponse(data)

def item_check(request):
    if request.method == "POST":
        data =json.loads(request.body)
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
    LabelName={"Value01Name":Label[0][0],"Value02Name":Label[1][0],"Value03Name":Label[2][0],"Value04Name":Label[3][0],"Value05Name":Label[4][0],"Value06Name":Label[5][0],"Value07Name":Label[6][0],"Value08Name":Label[7][0],"Value09Name":Label[8][0],"Value10Name":Label[9][0],"Value11Name":Label[10][0],"Value12Name":Label[11][0],"Value13Name":Label[12][0]}
    context=LabelName
    return render(request,'home/page-revise.html',context)

#GET    
def GetDashboard(request):
    
    Data=[]
    GetData=DBmysql.read_mysql("SENSOR","select * from `SENSOR_DB` ORDER BY `ID` DESC LIMIT 0,1")[0]
    Re_Value=DBmysql.read_mysql("REVISE","select * from `RE_VALUE`,`LABEL` where `Va_Name` = `Label`") 
    
    isshowid=[]
    for i in Re_Value:
        if i[12] == 'True' :
            isshowid.append(i[0]-14)

    for i in isshowid:
        Data.append({"Date_Time":GetData[1],"ProjID":str(GetData[2]),"STID":str(GetData[3]),"Item":str(Re_Value[i][11]),"Value_be":str(round(GetData[i+4],2)),"Value_af":str(round(GetData[i+17],2)),"a":str(round(Re_Value[i][6],3)),"b":str(round(Re_Value[i][7],3)),"offset":str(Re_Value[i][8]),"isshow":Re_Value[i][12]})
        #Data.append({"Date_Time":GetData[1],"ProjID":str(GetData[2]),"STID":str(GetData[3]),"Item":str(Re_Value[i][11]),"Value_be":str(GetData[i+4]),"Value_af":str(GetData[i+17]),"a":str(Re_Value[i][6]),"b":str(Re_Value[i][7]),"offset":str(Re_Value[i][8]),"isshow":Re_Value[i][12]})

    context={"Data":Data}
    print(round(GetData[5],2))
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
        
        #print(SwitchCheck_all)        
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
        #Item = "Value1"
        Value_af=DBmysql.read_mysql("SENSOR",("select `{}` from `STANDARD_DB` ORDER BY `ID` DESC LIMIT 0,1").format(Item))[0]
        Value_be=DBmysql.read_mysql("SENSOR",("select `{}` from `SENSOR_DB` ORDER BY `ID` DESC LIMIT 0,1").format(Item))[0]
        ST_VALUE=DBmysql.read_mysql("REVISE",("select `a`,`b`,`offset` from `ST_VALUE` WHERE `Va_Name` = '{}' ").format(Item))[0]
        a=ST_VALUE[0]
        b=ST_VALUE[1]
        offset=ST_VALUE[2]
        calValue_af=Value_be[0]*a+b+offset
        print(Value_be[0])
        
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
    