from asyncio.windows_events import NULL
import serial, time

ser = serial.Serial()  
ser.port = 'COM10'
ser.baudrate = 9600
ser.parity = serial.PARITY_NONE
ser.bytesize = serial.EIGHTBITS 
ser.stopbits = serial.STOPBITS_ONE
ser.xonxoff = False  #disable software flow control
ser.rtscts = False  #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False  #disable hardware (DSR/DTR) flow control
ser.timeout = 1
ser.open() # open serial port 



def NOISE():
    try:
        ser.write(b'DOD?\r\n')
        strvalue= ser.readall().decode('utf8')
        value = strvalue[9:-3].split(', ') #all_value
        list = {
            'Value1':value[0],
            'Value2':value[1],
            'Value3':value[2],
            'Value4':value[3],
            'Value5':value[4],
            'Value6':value[8],
        }
        #print("NOISE",value)
        #儀器沒抓到值，可以按按看start
        if list['Value2']=="--.-":
            return {'Value1': NULL,'S1': '#'}
        return {'Value1': value[1],'S1': NULL}
    except:
        #線沒接好
        return {'Value1': NULL,'S1': '--'}

def Sensor():
    N = NOISE()
    #原始值
    list = {
        #'Value14':N['Value1'],# 噪音
        'Value14':17,# 噪音
        'S1':N['S1'],
        'Value15':0,# 風速
        'S2':"**",
        'Value16':0,# 風向
        'S3':"**",
        'Value17':0,# 溫度
        'S4':"**",
        'Value18':0,# 濕度
        'S5':"**",
        'Value19':0,# 雨量
        'S6':"**",
        'Value20':0,# 大氣壓力
        'S7':"**",

    }
    return list
    

X="Value1"
y=X.split("Value")
Value14 = "Value"+str(int(y[1])+13)
print(Value14)

# if __name__=='__main__':
#     while(1):
#         print(Sensor())

    


