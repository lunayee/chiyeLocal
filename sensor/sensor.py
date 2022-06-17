import serial, time,datetime

ser = serial.Serial()  
ser.port = 'COM2'
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
        return value[0]
    except:
        #線沒接好
        return -9999

def Sensor():
    # Value1-6校正後的值 Value14-19校正前的值
    now = datetime.datetime.now()
    str_now = datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
    N = NOISE()
    #原始值
    list = {
        'Time':str_now,
        'Value14':N,# 噪音
        'Value15':0,# 風速
        'Value16':0,# 風向
        'Value17':0,# 溫度
        'Value18':0,# 濕度
        'Value19':0,# 雨量
        'Value20':0,# 大氣壓力
    }
    return list
    


if __name__=='__main__':
    while(1):
        print(Sensor())



